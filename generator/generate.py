import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Tuple, Optional
import urllib.request

# Try to import PyGithub; fall back to REST API if unavailable
try:
	from github import Github  # type: ignore
	from github.GithubException import GithubException  # type: ignore
except Exception:
	Github = None  # type: ignore
	GithubException = Exception  # type: ignore

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


def fetch_repo_metadata_via_rest(full_name: str, token: Optional[str]) -> Dict[str, Any]:
	url = f"https://api.github.com/repos/{full_name}"
	req = urllib.request.Request(url)
	req.add_header("Accept", "application/vnd.github+json")
	if token:
		req.add_header("Authorization", f"Bearer {token}")
	try:
		with urllib.request.urlopen(req, timeout=20) as resp:
			data = json.loads(resp.read().decode("utf-8"))
	except Exception as e:
		return {
			"name": full_name.split("/")[-1],
			"html_url": f"https://github.com/{full_name}",
			"stars": 0,
			"last_active": None,
			"error": str(e),
		}
	last_active = parse_iso8601_z(data.get("pushed_at"))
	if last_active.tzinfo is None:
		last_active = last_active.replace(tzinfo=timezone.utc)
	return {
		"name": data.get("name") or full_name.split("/")[-1],
		"html_url": data.get("html_url") or f"https://github.com/{full_name}",
		"stars": int(data.get("stargazers_count") or 0),
		"last_active": last_active,
	}


def fetch_repo_metadata(gh: Optional[Any], full_name: str, token: Optional[str]) -> Dict[str, Any]:
	if gh is None:
		return fetch_repo_metadata_via_rest(full_name, token)
	try:
		repo = gh.get_repo(full_name)
	except GithubException as e:  # type: ignore
		return {
			"name": full_name,
			"html_url": f"https://github.com/{full_name}",
			"stars": 0,
			"last_active": None,
			"error": str(e),
		}
	last_active = safe_get_last_activity(repo)
	return {
		"name": full_name,
		"html_url": repo.html_url,
		"stars": int(repo.stargazers_count or 0),
		"last_active": last_active,
	}


def normalize_description(desc_field: Any) -> str:
	if isinstance(desc_field, list):
		return "<br> ".join(str(x).strip() for x in desc_field if str(x).strip())
	if isinstance(desc_field, str):
		return desc_field.strip()
	return ""


def build_markdown_table(rows: List[Dict[str, Any]], now: datetime) -> str:
	lines: List[str] = []
	lines.append("| Repository | Description | Stars | Last Active |")
	lines.append("| --- | --- | --- | --- |")
	for row in rows:
		repo_link = f"[{row['name']}]({row['html_url']})"
		description = row.get("description", "")
		stars = f"{row.get('stars', 0):,}"
		last_active_dt: datetime = row.get("last_active")
		last_active = humanize_since(last_active_dt, now) if isinstance(last_active_dt, datetime) else "unknown"
		lines.append(f"| {repo_link} | {description} | {stars} | {last_active} |")
	return "\n".join(lines)


def manifest_to_placeholder(manifest_filename: str) -> str:
	name_no_ext = manifest_filename.rsplit(".", 1)[0]
	return "$" + name_no_ext.replace("-", "_").upper()

def main() -> None:
	# Setup GitHub client
	token = os.environ.get("GITHUB_TOKEN")
	gh = Github(login_or_token=token) if (Github is not None and token) else (Github() if Github is not None else None)  # type: ignore

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
	for manifest_path in sorted(MANIFESTS_DIR.glob("*.json")):
		entries = parse_manifest(manifest_path)
		rows: List[Dict[str, Any]] = []
		stats_rows: List[Dict[str, Any]] = []
		for entry in entries:
			repo_full_name = str(entry.get("repo", "")).strip()
			if not repo_full_name:
				continue
			meta = fetch_repo_metadata(gh, repo_full_name, token)
			meta["description"] = normalize_description(entry.get("description", ""))
			rows.append(meta)
			pushed_at_dt: Optional[datetime] = meta.get("last_active")
			pushed_at_iso = pushed_at_dt.isoformat() if isinstance(pushed_at_dt, datetime) else None
			stats_rows.append({
				"repo": repo_full_name,
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
	last_update_human = humanize_since(last_update_dt, now)
	total_runtime_human = humanize_duration(int((now - project_start).total_seconds()))

	output_text = output_text.replace("$LAST_UPDATE", last_update_human)
	output_text = output_text.replace("$RUNNING_TIME", total_runtime_human)

	# Write README
	write_text_file(README_MD, output_text)

	# Update tag file with new last_update
	new_tag_data = update_last_update(tag_data)
	write_json_file(TAG_FILE, new_tag_data)

	print(f"README generated at {README_MD}")


if __name__ == "__main__":
	main()
