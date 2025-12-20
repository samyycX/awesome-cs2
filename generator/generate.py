import json
import os
import sys
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Tuple, Optional
import asyncio
import aiohttp

REPO_ROOT = Path(__file__).resolve().parents[1]
MANIFESTS_DIR = REPO_ROOT / "manifests"
TEMPLATE_MD = REPO_ROOT / "TEMPLATE.md"
README_MD = REPO_ROOT / "README.md"
TAG_FILE = REPO_ROOT / "current.tag"
DATA_DIR = REPO_ROOT / "data"


def read_json_file(file_path: Path) -> Any:
	with file_path.open("r", encoding="utf-8") as f:
		return json.load(f)


def write_text_file(file_path: Path, content: str) -> None:
	with file_path.open("w", encoding="utf-8", newline="\n") as f:
		f.write(content)


def write_json_file(file_path: Path, obj: Any) -> None:
	with file_path.open("w", encoding="utf-8", newline="\n") as f:
		json.dump(obj, f, ensure_ascii=False, indent=2)


def load_or_init_tags(tag_path: Path) -> Dict[str, str]:
	now_iso = datetime.now(timezone.utc).isoformat()
	if tag_path.exists():
		content = tag_path.read_text(encoding="utf-8").strip()
		if content:
			try:
				data = json.loads(content)
				# Backfill missing fields
				if "project_start" not in data:
					data["project_start"] = now_iso
				if "last_update" not in data:
					data["last_update"] = now_iso
				return data
			except json.JSONDecodeError:
				pass
	# Initialize
	return {"project_start": now_iso, "last_update": now_iso}


def update_last_update(tag_data: Dict[str, str]) -> Dict[str, str]:
	updated = dict(tag_data)
	updated["last_update"] = datetime.now(timezone.utc).isoformat()
	return updated


def parse_manifest(file_path: Path) -> List[Dict[str, Any]]:
	data = read_json_file(file_path)
	if not isinstance(data, list):
		raise ValueError(f"Manifest {file_path} must be a JSON array")
	return data


def humanize_duration(delta_seconds: int) -> str:
	# Simple humanizer without extra deps
	units: List[Tuple[int, str]] = [
		(365 * 24 * 3600, "year"),
		(30 * 24 * 3600, "month"),
		(7 * 24 * 3600, "week"),
		(24 * 3600, "day"),
		(3600, "hour"),
		(60, "minute"),
		(1, "second"),
	]
	abs_seconds = max(0, int(delta_seconds))
	for unit_seconds, unit_name in units:
		if abs_seconds >= unit_seconds:
			value = abs_seconds // unit_seconds
			plural = "s" if value != 1 else ""
			return f"{value} {unit_name}{plural}"
	return "0 seconds"


def humanize_since(dt: datetime, now: datetime) -> str:
	return f"{humanize_duration(int((now - dt).total_seconds()))} ago"


def parse_iso8601_z(s: Optional[str]) -> Optional[datetime]:
	if not s:
		return None
	try:
		# GitHub returns like 2024-08-12T12:34:56Z
		if s.endswith("Z"):
			return datetime.fromisoformat(s.replace("Z", "+00:00"))
		return datetime.fromisoformat(s)
	except Exception:
		return None


def safe_get_last_activity(repo_obj: Any) -> datetime:
	return getattr(repo_obj, "pushed_at", None)

# Fetch repository metadata via GitHub REST
async def _fetch_repo_aiohttp(session: "aiohttp.ClientSession", full_name: str) -> Dict[str, Any]:  # type: ignore
	url = f"https://api.github.com/repos/{full_name}"
	async with session.get(url, timeout=aiohttp.ClientTimeout(total=20)) as resp:  # type: ignore
		data = await resp.json()
		pushed_at = data.get("pushed_at")
		last_active = parse_iso8601_z(pushed_at) or datetime.now(timezone.utc)
		if last_active.tzinfo is None:
			last_active = last_active.replace(tzinfo=timezone.utc)
		owner_obj = data.get("owner") or {}
		owner_login = owner_obj.get("login") if isinstance(owner_obj, dict) else None
		owner_html_url = (owner_obj.get("html_url") if isinstance(owner_obj, dict) else None) or (f"https://github.com/{owner_login}" if owner_login else None)
		owner_avatar_url = owner_obj.get("avatar_url") if isinstance(owner_obj, dict) else None
		owner_type = owner_obj.get("type") if isinstance(owner_obj, dict) else None
		return {
			"name": data.get("full_name") or full_name,
			"html_url": data.get("html_url") or f"https://github.com/{full_name}",
			"stars": int(data.get("stargazers_count") or 0),
			"last_active": last_active,
			"owner": {
				"login": owner_login,
				"html_url": owner_html_url,
				"avatar_url": owner_avatar_url,
				"type": owner_type,
			},
		}

async def fetch_many_async(full_names: List[str], token: Optional[str]) -> Dict[str, Dict[str, Any]]:
	headers = {
		"Accept": "application/vnd.github+json",
	}
	if token:
		headers["Authorization"] = f"Bearer {token}"
	connector = aiohttp.TCPConnector(limit=10) if aiohttp else None  # type: ignore
	async with aiohttp.ClientSession(headers=headers, connector=connector) as session:  # type: ignore
		tasks = [_fetch_repo_aiohttp(session, full_name) for full_name in full_names]
		results = await asyncio.gather(*tasks, return_exceptions=True)
		out: Dict[str, Dict[str, Any]] = {}
		for full_name, res in zip(full_names, results):
			if isinstance(res, Exception):
				out[full_name] = {
					"name": full_name,
					"html_url": f"https://github.com/{full_name}",
					"stars": 0,
					"last_active": None,
					"error": str(res),
				}
			else:
				out[full_name] = res
		return out

def fetch_many(full_names: List[str], token: Optional[str]) -> Dict[str, Dict[str, Any]]:
		return asyncio.run(fetch_many_async(full_names, token))

# Fetch repository contributors via GitHub REST
async def _fetch_contributors_aiohttp(session: "aiohttp.ClientSession", full_name: str) -> List[Dict[str, Any]]:  # type: ignore
	url = f"https://api.github.com/repos/{full_name}/contributors?per_page=100"
	async with session.get(url, timeout=aiohttp.ClientTimeout(total=20)) as resp:  # type: ignore
		data = await resp.json()
		contributors: List[Dict[str, Any]] = []
		if isinstance(data, list):
			for item in data:
				login = item.get("login")
				if not login:
					continue
				contributors.append({
					"login": login,
					"html_url": item.get("html_url") or f"https://github.com/{login}",
					"avatar_url": item.get("avatar_url") or f"https://github.com/{login}.png",
					"type": item.get("type") or "User",
				})
		return contributors

async def fetch_contributors_many_async(full_names: List[str], token: Optional[str]) -> Dict[str, List[Dict[str, Any]]]:
	headers = {
		"Accept": "application/vnd.github+json",
	}
	if token:
		headers["Authorization"] = f"Bearer {token}"
	connector = aiohttp.TCPConnector(limit=10) 
	async with aiohttp.ClientSession(headers=headers, connector=connector) as session: 
		tasks = [_fetch_contributors_aiohttp(session, full_name) for full_name in full_names]
		results = await asyncio.gather(*tasks, return_exceptions=True)
		out: Dict[str, List[Dict[str, Any]]] = {}
		for full_name, res in zip(full_names, results):
			if isinstance(res, Exception):
				out[full_name] = []
			else:
				out[full_name] = res
		return out

def fetch_contributors_many(full_names: List[str], token: Optional[str]) -> Dict[str, List[Dict[str, Any]]]:
	return asyncio.run(fetch_contributors_many_async(full_names, token))


def normalize_description(desc_field: Any) -> str:
	if isinstance(desc_field, list):
		return "<br> ".join(str(x).strip() for x in desc_field if str(x).strip())
	if isinstance(desc_field, str):
		return desc_field.strip()
	return ""


def build_markdown_table(rows: List[Dict[str, Any]], now: datetime) -> str:
	lines: List[str] = []
	for row in rows:
		repo_link = f"[{row['name']}]({row['html_url']})"
		description = row.get("desc", "")
		stars = f"{row.get('stars', 0):,}"
		last_active_dt: datetime = row.get("last_active")
		last_active = humanize_since(last_active_dt, now) if isinstance(last_active_dt, datetime) else "unknown"
		lines.append(f"- **{repo_link}**<br>")
		lines.append(f"  ⭐ {stars}<br>")
		lines.append(f"  ⏱️ updated {last_active}<br>")
		lines.append(f"  *{description}*")
		lines.append("")
	return "\n".join(lines)

# Build an HTML table grid of contributors (avatar on top, handle link below)
def build_contributors_table(contributors: List[Dict[str, Any]], columns: int = 10) -> str:
	lines: List[str] = []
	lines.append("<table>")
	for idx, c in enumerate(contributors):
		if idx % columns == 0:
			if idx != 0:
				lines.append("  </tr>")
			lines.append("  <tr>")
		login = str(c.get("login", "")).strip()
		html_url = str(c.get("html_url") or (f"https://github.com/{login}" if login else "")).strip()
		avatar_url = str(c.get("avatar_url") or (f"https://github.com/{login}.png?size=100" if login else "")).strip()
		lines.append("    <td align=\"center\" valign=\"top\" width=\"80\">")
		lines.append(f"      <a href=\"{html_url}\"><img src=\"{avatar_url}\" width=\"64\" height=\"64\" alt=\"{login}\" /></a><br/>")
		lines.append(f"      <a href=\"{html_url}\">@{login}</a>")
		lines.append("    </td>")
	if contributors:
		lines.append("  </tr>")
	lines.append("</table>")
	lines.append("")
	return "\n".join(lines)


def manifest_to_placeholder(manifest_filename: str) -> str:
	name_no_ext = manifest_filename.rsplit(".", 1)[0]
	return "$" + name_no_ext.replace("-", "_").upper()


async def fetch_swiftlys2_posts(bypass_key: Optional[str]) -> List[Dict[str, Any]]:
	if not bypass_key:
		print("Warning: BYPASS_KEY not set, skipping SwiftlyS2 plugins")
		return []

	url = "https://forum.swiftlys2.net/posts.json"
	params = {"bypass_key": bypass_key}

	try:
		async with aiohttp.ClientSession() as session:
			async with session.get(url, params=params, timeout=aiohttp.ClientTimeout(total=30)) as resp:
				if resp.status != 200:
					print(f"Failed to fetch SwiftlyS2 posts: {resp.status}")
					return []
				data = await resp.json()
	except Exception as e:
		print(f"Error fetching SwiftlyS2 posts: {e}")
		return []

	posts = data.get("latest_posts", [])
	plugins = []

	for post in posts:
		raw = post.get("raw", "")
		
		# Extract repo
		matches = re.findall(r"github\.com/([a-zA-Z0-9_.-]+/[a-zA-Z0-9_.-]+)", raw)
		repo_full_name = None
		for match in matches:
			if match.lower() in ["site/terms", "site/privacy", "github/site"]:
				continue
			if match.endswith(".git"):
				match = match[:-4]
			repo_full_name = match
			break
			
		if not repo_full_name:
			continue

		# Extract description
		desc = ""
		desc_match = re.search(r"### Description\s+(.+?)(?=\n#|$)", raw, re.DOTALL)
		if desc_match:
			desc = desc_match.group(1).strip()
			desc = desc.split('\n')[0]

		plugins.append({
			"repo": repo_full_name,
			"desc": desc
		})

	return plugins


def main() -> None:
	# Setup GitHub client
	token = os.environ.get("GITHUB_TOKEN")

	# Ensure data directory exists
	DATA_DIR.mkdir(parents=True, exist_ok=True)

	# Load and update tag data
	tag_data = load_or_init_tags(TAG_FILE)
	now = datetime.now(timezone.utc)
	project_start_iso = tag_data["project_start"]
	try:
		project_start = datetime.fromisoformat(project_start_iso)
	except Exception:
		project_start = now

	# Build per-manifest tables and write stats
	placeholder_to_table: Dict[str, str] = {}
	# Accumulators for global contributors/owners
	all_repo_full_names: List[str] = []
	all_owners: Dict[str, Dict[str, Any]] = {}
	for manifest_path in sorted(MANIFESTS_DIR.glob("*.json")):
		entries = parse_manifest(manifest_path)
		rows: List[Dict[str, Any]] = []
		stats_rows: List[Dict[str, Any]] = []
		full_names: List[str] = []
		entry_map: Dict[str, Dict[str, Any]] = {}
		for entry in entries:
			repo_full_name = str(entry.get("repo", "")).strip()
			if not repo_full_name:
				continue
			full_names.append(repo_full_name)
			entry_map[repo_full_name] = entry
		# Concurrent fetch
		meta_map = fetch_many(full_names, token)
		# Capture owners globally
		for meta in meta_map.values():
			owner = meta.get("owner") or {}
			owner_login = owner.get("login") if isinstance(owner, dict) else None
			if owner_login:
				all_owners[owner_login] = {
					"login": owner_login,
					"html_url": owner.get("html_url") or f"https://github.com/{owner_login}",
					"avatar_url": owner.get("avatar_url") or f"https://github.com/{owner_login}.png",
					"type": owner.get("type") or "User",
				}
		for repo_full_name in full_names:
			meta = meta_map.get(repo_full_name)
			meta["desc"] = normalize_description(entry_map[repo_full_name].get("desc", ""))
			rows.append(meta)
		# Sort by stars desc
		rows.sort(key=lambda r: int(r.get("stars", 0) or 0), reverse=True)
		for meta in rows:
			pushed_at_dt: Optional[datetime] = meta.get("last_active")
			pushed_at_iso = pushed_at_dt.isoformat() if isinstance(pushed_at_dt, datetime) else None
			stats_rows.append({
				"repo": meta.get("name"),
				"stars": meta.get("stars", 0),
				"pushed_at": pushed_at_iso,
				"fetched_at": now.isoformat(),
			})
		placeholder = manifest_to_placeholder(manifest_path.name)
		placeholder_to_table[placeholder] = build_markdown_table(rows, now)
		# Write stats file per manifest
		manifest_base = manifest_path.stem  # e.g., metamod-plugins
		stats_path = DATA_DIR / f"{manifest_base}.stats.json"
		write_json_file(stats_path, stats_rows)
		# Accumulate for global contributor fetch
		all_repo_full_names.extend(full_names)

	# Handle SwiftlyS2 Plugins specially
	bypass_key = os.environ.get("BYPASS_KEY")
	swiftlys2_entries = asyncio.run(fetch_swiftlys2_posts(bypass_key))
	if swiftlys2_entries:
		rows: List[Dict[str, Any]] = []
		stats_rows: List[Dict[str, Any]] = []
		full_names: List[str] = []
		entry_map: Dict[str, Dict[str, Any]] = {}
		for entry in swiftlys2_entries:
			repo_full_name = str(entry.get("repo", "")).strip()
			if not repo_full_name:
				continue
			full_names.append(repo_full_name)
			entry_map[repo_full_name] = entry
		
		meta_map = fetch_many(full_names, token)
		for meta in meta_map.values():
			owner = meta.get("owner") or {}
			owner_login = owner.get("login") if isinstance(owner, dict) else None
			if owner_login:
				all_owners[owner_login] = {
					"login": owner_login,
					"html_url": owner.get("html_url") or f"https://github.com/{owner_login}",
					"avatar_url": owner.get("avatar_url") or f"https://github.com/{owner_login}.png",
					"type": owner.get("type") or "User",
				}
		
		for repo_full_name in full_names:
			meta = meta_map.get(repo_full_name)
			meta["desc"] = normalize_description(entry_map[repo_full_name].get("desc", ""))
			rows.append(meta)
		
		rows.sort(key=lambda r: int(r.get("stars", 0) or 0), reverse=True)
		
		for meta in rows:
			pushed_at_dt: Optional[datetime] = meta.get("last_active")
			pushed_at_iso = pushed_at_dt.isoformat() if isinstance(pushed_at_dt, datetime) else None
			stats_rows.append({
				"repo": meta.get("name"),
				"stars": meta.get("stars", 0),
				"pushed_at": pushed_at_iso,
				"fetched_at": now.isoformat(),
			})
			
		placeholder_to_table["$SWIFTLYS2_PLUGINS"] = build_markdown_table(rows, now)
		write_json_file(DATA_DIR / "swiftlys2-plugins.stats.json", stats_rows)
		all_repo_full_names.extend(full_names)
	else:
		placeholder_to_table["$SWIFTLYS2_PLUGINS"] = ""

	# Build global contributors table and write data
	if all_repo_full_names:
		contribs_by_repo = fetch_contributors_many(all_repo_full_names, token)
		login_to_contributor: Dict[str, Dict[str, Any]] = {}
		# include owners
		for login, info in all_owners.items():
			login_to_contributor[login] = info
		# include contributors
		for _repo, contribs in contribs_by_repo.items():
			for c in contribs:
				login = c.get("login")
				if not login:
					continue
				login_to_contributor[login] = {
					"login": login,
					"html_url": c.get("html_url") or f"https://github.com/{login}",
					"avatar_url": c.get("avatar_url") or f"https://github.com/{login}.png",
					"type": c.get("type") or "User",
				}
						# include manual contributors from manifests/contributors.json
		manual_contribs_path = REPO_ROOT / "contributors.json"
		if manual_contribs_path.exists():
			try:
				manual = read_json_file(manual_contribs_path)
				if isinstance(manual, list):
					for item in manual:
						if isinstance(item, str):
							login = item.strip()
							if not login:
								continue
							login_to_contributor[login] = {
								"login": login,
								"html_url": f"https://github.com/{login}",
								"avatar_url": f"https://github.com/{login}.png",
								"type": "User",
							}
						elif isinstance(item, dict):
							login = str(item.get("login") or "").strip()
							if not login:
								continue
							html_url = item.get("html_url") or f"https://github.com/{login}"
							avatar_url = item.get("avatar_url") or f"https://github.com/{login}.png"
							type_ = item.get("type") or "User"
							login_to_contributor[login] = {
								"login": login,
								"html_url": html_url,
								"avatar_url": avatar_url,
								"type": type_,
							}
			except Exception:
				pass
		sorted_contribs = sorted(login_to_contributor.values(), key=lambda d: str(d.get("login", "")).lower())
		placeholder_to_table["$CONTRIBUTORS"] = build_contributors_table(sorted_contribs, columns=5)
		# Persist raw contributors list
		write_json_file(DATA_DIR / "contributors.json", {
			"generated_at": now.isoformat(),
			"count": len(sorted_contribs),
			"contributors": sorted_contribs,
		})
	else:
		placeholder_to_table["$CONTRIBUTORS"] = ""

	# Read template
	template_text = TEMPLATE_MD.read_text(encoding="utf-8")

	# Replace placeholders
	output_text = template_text
	for placeholder, table_md in placeholder_to_table.items():
		output_text = output_text.replace(placeholder, table_md)

	# Prepare stats
	last_update_iso = tag_data.get("last_update", now.isoformat())
	try:
		last_update_dt = datetime.fromisoformat(last_update_iso)
	except Exception:
		last_update_dt = now
	last_update_abs = last_update_dt.astimezone(timezone.utc).strftime("%Y/%m/%d %H:%M:%S")
	total_runtime_human = humanize_duration(int((now - project_start).total_seconds()))
	output_text = output_text.replace("$LAST_UPDATE", last_update_abs)
	output_text = output_text.replace("$RUNNING_TIME", total_runtime_human)

	# Write README
	write_text_file(README_MD, output_text)

	# Update tag file with new last_update
	new_tag_data = update_last_update(tag_data)
	write_json_file(TAG_FILE, new_tag_data)

	print(f"README generated at {README_MD}")


if __name__ == "__main__":
	main()
