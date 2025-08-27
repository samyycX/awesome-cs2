<div align="center" style="text-align: center">
<h3>Awesome CS2</h3>
<p>
  An awesome list for all available cs2 development information, including modding frameworks, development resources, plugins and etc.
</p>
<p>
  Last Sync: <strong>9 minutes ago</strong>
</p>
<p>
  Project Uptime: <strong>14 hours</strong>
</p>

</div>

# Contents
- [General](#general)
- [Tools](#tools)
- [Status Trackers](#status-trackers)
- [Modding Frameworks](#modding-frameworks)
- [Development Resources](#development-resources)
- [Communities](#communities)
- [Plugins](#plugins)
  - [Metamod Plugins](#metamod-plugins)
  - [CounterStrikeSharp Plugins](#counterstrikesharp-plugins)
  - [Swiftly Plugins](#swiftly-plugins)
- [Contributors](#contributors)
- [Contributing](#contributing)

# General
- **[Source2 Wiki](https://source2.wiki)**\
  *An actively maintained source2 wiki, where you can learn information about workshop tools and entities.*

- **[cs2browser.net](https://cs2browser.net)**\
  *A clean and live cs2 community server browser without fake servers and advertisements.*

- **[Valve Official Documentation](https://developer.valvesoftware.com/)**\
  *Valve's official documentation for cs2 and other source games.*\
  ***Not recommended for checking cs2 information, most of them are outdated or absent.***

- **[gamebanana.com](https://gamebanana.com/games/18134)**\
  *A workshop resource website that contains cs2 models, maps and etc.*

# Tools
- **[Source2Viewer](https://s2v.app/)**\
  *A powerful tool to unpack and decompile resources from vpk files.*

- **[VPulse Editor](https://github.com/LionDoge/vpulse-editor)**\
  *A visual programming tool to write the vpulse script, which is a new unreleased visualized script system for source2 to replace vscript.*

- **[Schema Dumper](https://github.com/GAMMACASE/Source2SchemaDumper)**\
  *A metamod plugin for dumping schemas from game binary, and also able to generate a header file that can be imported in IDA for reverse engineering.*

- **[DepotDownloader](https://github.com/SteamRE/DepotDownloader)**\
  *A tool to download game files of a specific version.*

- **[PltPatcher](https://github.com/GAMMACASE/PltPatcher)**\
  *A IDA python plugin to patch plt sections when IDA fails to do so automatically, you might encounter such problem when decompiling linux binaries, made by GAMMACASE.*

# Status Trackers

- **[SteamDB](https://steamdb.info/app/730/charts/)**\
  *A website tracking steam games information.*

- **[cs2-signatures](https://github.com/ianlucas/cs2-signatures)**\
  *A github repo for tracking gamedata status after a game update.*

# Modding Frameworks
- **[Metamod](https://github.com/alliedmodders/metamod-source)** [[Website](https://www.sourcemm.net/downloads.php?branch=dev)] [[Discord](https://discord.com/invite/HUc67zN)]\
  *The cobblestone of all of the current open source framework since source1, written in C++, hard to develop but have access to fundamental things.*\
  ***Please notice that it's the dev branch that support cs2, make sure you download the right version.***
  
- **[CounterStrikeSharp](https://github.com/roflmuffin/CounterStrikeSharp)** [[Website](https://docs.cssharp.dev/)] [[Discord](https://discord.com/invite/eAZU3guKWU)]\
  *The most popular modding framework for cs2, the plugins are written in c#.*\
  *Alias: CS#, cssharp*

- **[Swiftly](https://github.com/swiftly-solution/swiftly)** [[Website](https://swiftlys2.net)] [[Discord](https://discord.com/invite/Yv7hAM6erd)]\
  *A modding framework that support c#, cpp and lua as scripting language with more feature than counterstrikesharp.*

- **[Plugify](https://github.com/untrustedmodders/plugify)** [[Website](https://plugify.net)] [[Discord](https://discord.gg/untrustedmodders)]\
  *A modding framework that support tons of programming languages, more information can be found in there discord channel and website.*

# Development Resources
These are the websites with resources that you might need to check during development.

- **[ConVars](https://github.com/SteamDatabase/GameTracking-CS2/blob/master/DumpSource2/convars.txt)**\
  *A list of all cs2 convars, directly dumped from latest cs2 binary.*

- **[Commands](https://github.com/SteamDatabase/GameTracking-CS2/blob/master/DumpSource2/commands.txt)**\
  *A list of all cs2 commands, directly dumped from latest cs2 binary.*

- **[Game Events](https://cs2.poggu.me/dumped-data/game-events)**\
  *A list of all cs2 game events.*\
  *The data might be outdated, if so, you can find the latest ones here:*\
  *[core.gameevents](https://github.com/SteamDatabase/GameTracking-CS2/blob/master/game/core/pak01_dir/resource/core.gameevents)*
  *[game.gameevents](https://github.com/SteamDatabase/GameTracking-CS2/blob/master/game/csgo/pak01_dir/resource/game.gameevents)*
  *[mod.gameevents](https://github.com/SteamDatabase/GameTracking-CS2/blob/master/game/csgo/pak01_dir/resource/mod.gameevents)*

- **[Schemas](https://github.com/SteamDatabase/GameTracking-CS2/tree/master/DumpSource2/schemas)**\
  *A list of all cs2 schema classes and fields, directly dumped from latest cs2 binary.*

- **[Entities](https://source2.wiki)**\
  *A list of all cs2 entities.*

- **[Protobufs](https://github.com/SteamDatabase/GameTracking-CS2/blob/master/Protobufs)**\
  *A list of all cs2 protobuf definitions.*

- **[gdc.eternar.dev](https://gdc.eternar.dev)**\
  *A online gamedata tracker and validator, maintaining an active list for function signatures and offsets. If there's an game update that break your server, you might find the new gamedata here.*

- **[wiki.alliedmods.net](https://wiki.alliedmods.net/)**\
  *Alliedmodders' wiki. You can find documentation about metamod, ambuild and sourcehook development here.*

- **[HL2SDK](https://github.com/alliedmodders/hl2sdk/tree/cs2)**\
  *Actively maintained SDK for cs2.*

- **[HL2SDK Wend4r's fork](https://github.com/Wend4r/sourcesdk)**\
  *A fork of hl2sdk, if there's a game update, you might find what have changed in here or in pull requests.*

- **[cstrike15_src](https://github.com/perilouswithadollarsign/cstrike15_src)**\
  *CSGO Leaked source code in 2020, cs2 is still using some codes from it.*

- **[cs2.poggu.me](https://cs2.poggu.me/)**\
  *A general information website made by poggu.*

- **[Source2ZE Map Porting Guide](https://docs.google.com/document/d/1buKzjP-2com9GcXVxCfyRBi6sDiKmzMoVy9RNbYQqIo)**\
  *A guide about porting map from csgo, written by s2ze community.*

# Communities
- **[Alliedmodders Discord](https://discord.com/invite/HUc67zN)**\
  *Official discord for alliedmodders, you can find discussions about metamod and sdk here.*

- **[Source2ZE Discord](https://discord.gg/QsSGf9ZEVs)**\
  *Official discord for source2ze community, mainly targeting workshop developers, you can find discussions including maps, models and cs2fixes here.*

- **[CounterStrikeSharp Discord](https://discord.com/invite/eAZU3guKWU)**\
  *Official discord for counterstrikesharp, you can find plugins, code snippets and development discussion here.*

- **[ModSharp Discord](https://discord.gg/wKarAjHm2G)**\
  *Official discord for modsharp, which is a currently unreleased modding framework.*

- **[Swiftly Discord](https://discord.com/invite/Yv7hAM6erd)**\
  *Official discord for swiftly, you can find swiftly plugins, code snippets, and discuss about swiftly modding framework here.*

- **[Plugify Discord](https://discord.gg/untrustedmodders)**\
  *Official discord for plugify, you can find plugify plugins, code snippets, and discuss about plugify modding framework here.*

- **[bbs.csgocn.net](https://bbs.csgocn.net/)**\
  *A Chinese forum for cs2 server development.*

- **[hlmod.net](https://hlmod.net/)**\
  *A Russian forum for source games development.*

# Plugins

## Metamod Plugins

- **[Source2ZE/CS2Fixes](https://github.com/Source2ZE/CS2Fixes)**<br>
  ⭐ 316<br>
  ⏱️ updated 6 hours ago<br>
  *A plugin with tons of fixes and features aimed but not limited to zombie escape.*

- **[Source2ZE/MultiAddonManager](https://github.com/Source2ZE/MultiAddonManager)**<br>
  ⭐ 104<br>
  ⏱️ updated 1 week ago<br>
  *A plugin that allows you to use multiple workshop addons at once and have clients download them.*

- **[Source2ZE/CleanerCS2](https://github.com/Source2ZE/CleanerCS2)**<br>
  ⭐ 54<br>
  ⏱️ updated 1 week ago<br>
  *A simple plugin that allows you to filter out console prints with regular expressions.*

- **[Source2ZE/ServerListPlayersFix](https://github.com/Source2ZE/ServerListPlayersFix)**<br>
  ⭐ 53<br>
  ⏱️ updated 1 week ago<br>
  *Populates the user information inside the steam api, as a result this fixes the players not showing up in the server browser.*

- **[Source2ZE/MovementUnlocker](https://github.com/Source2ZE/MovementUnlocker)**<br>
  ⭐ 52<br>
  ⏱️ updated 3 weeks ago<br>
  *A plugin that removes the max speed limitation from players on the ground, feels like CS:S. Useful for zombie knockback, several movement gamemodes, or just easier bhop.*

- **[Source2ZE/CS2ServerGUI](https://github.com/Source2ZE/CS2ServerGUI)**<br>
  ⭐ 48<br>
  ⏱️ updated 1 week ago<br>
  *A plugin that shows entities, net messages, events and etc with a GUI.*

- **[Source2ZE/StripperCS2](https://github.com/Source2ZE/StripperCS2)**<br>
  ⭐ 45<br>
  ⏱️ updated 1 week ago<br>
  *A plugin that allows server operators to manage map lump data similarly to how Stripper:Source worked.*

- **[Cruze03/FakeRanks-RevealAll](https://github.com/Cruze03/FakeRanks-RevealAll)**<br>
  ⭐ 42<br>
  ⏱️ updated 3 weeks ago<br>
  *A metamod plugin that reveals ranks of all players in server for player who presses tab*

- **[Source2ZE/AcceleratorCS2](https://github.com/Source2ZE/AcceleratorCS2)**<br>
  ⭐ 28<br>
  ⏱️ updated 2 weeks ago<br>
  *A plugin that generate a crash dump when there's a crash.*

- **[samyycX/Audio](https://github.com/samyycX/Audio)**<br>
  ⭐ 13<br>
  ⏱️ updated 5 days ago<br>
  *A demo and a metamod lib to provide similar functions to the previous SM-Ext-Audio extension in csgo, that is, sending custom audio streams such as a song through a bot's voice chat.*

- **[GAMMACASE/Source2SchemaDumper](https://github.com/GAMMACASE/Source2SchemaDumper)**<br>
  ⭐ 11<br>
  ⏱️ updated 5 days ago<br>
  *A plugin that can dump the schemas and generate a header file.*

- **[Cruze03/GameBanFix](https://github.com/Cruze03/GameBanFix)**<br>
  ⭐ 10<br>
  ⏱️ updated 1 week ago<br>
  *Fixes issue where if a player with game ban joins, other players even without a ban are then unable to join.*


## CounterStrikeSharp Plugins

- **[shobhit-pathak/MatchZy](https://github.com/shobhit-pathak/MatchZy)**<br>
  ⭐ 368<br>
  ⏱️ updated 2 days ago<br>
  *MatchZy is a plugin for CS2 (Counter Strike 2) for running and managing practice/pugs/scrims/matches with easy configuration!*

- **[Nereziel/cs2-WeaponPaints](https://github.com/Nereziel/cs2-WeaponPaints)**<br>
  ⭐ 313<br>
  ⏱️ updated 1 week ago<br>
  *A plugin to change weapon paints, gloves, agents and etc.*

- **[B3none/cs2-retakes](https://github.com/B3none/cs2-retakes)**<br>
  ⭐ 278<br>
  ⏱️ updated 5 days ago<br>
  *CS2 implementation of retakes written in C# for CounterStrikeSharp. Based on the version for CS:GO by Splewis.*

- **[daffyyyy/CS2-SimpleAdmin](https://github.com/daffyyyy/CS2-SimpleAdmin)**<br>
  ⭐ 148<br>
  ⏱️ updated 3 days ago<br>
  *Manage your Counter-Strike 2 server with simple commands!*

- **[samyycX/CS2-PlayerModelChanger](https://github.com/samyycX/CS2-PlayerModelChanger)**<br>
  ⭐ 105<br>
  ⏱️ updated 7 months ago<br>
  *A cssharp plugin to change player models.*

- **[NockyCZ/CS2-Deathmatch](https://github.com/NockyCZ/CS2-Deathmatch)**<br>
  ⭐ 101<br>
  ⏱️ updated 3 weeks ago<br>
  *A plugin to implement deathmatch gamemode.*

- **[schwarper/cs2-store](https://github.com/schwarper/cs2-store)**<br>
  ⭐ 66<br>
  ⏱️ updated 1 week ago<br>
  *A store plugin designed to enhance your gameplay by providing a dynamic credit system that allows players to purchase essential items directly from the store.*

- **[partiusfabaa/cs2-ranks](https://github.com/partiusfabaa/cs2-ranks)**<br>
  ⭐ 60<br>
  ⏱️ updated 3 weeks ago<br>
  *Each player is assigned a rank based on their accumulated experience points. Ranks range from "None" to the prestigious "The Global Elite."*

- **[daffyyyy/CS2-Tags](https://github.com/daffyyyy/CS2-Tags)**<br>
  ⭐ 52<br>
  ⏱️ updated 1 year ago<br>
  *Adds tags to the server that can be easily edited, tags can be assigned via permission or steamid64.*

- **[Cruze03/FortniteEmotesNDances](https://github.com/Cruze03/FortniteEmotesNDances)**<br>
  ⭐ 50<br>
  ⏱️ updated 1 week ago<br>
  *This plugin allows players to use Emotes & Dances just like Fortnite.*

- **[schwarper/cs2-tags](https://github.com/schwarper/cs2-tags)**<br>
  ⭐ 41<br>
  ⏱️ updated 2 weeks ago<br>
  *A tag plugin designed to enhance your CS2 experience with a dynamic tagging system. Customise and manage player tags effortlessly for a more interactive and engaging game environment.*

- **[schwarper/CS2MenuManager](https://github.com/schwarper/CS2MenuManager)**<br>
  ⭐ 35<br>
  ⏱️ updated 3 weeks ago<br>
  *CS2MenuManager is a modern, extensible and easy to use menu system for Counter-Strike 2 based on the CounterStrikeSharp library.*

- **[darkerz7/EntWatchSharp](https://github.com/darkerz7/EntWatchSharp)**<br>
  ⭐ 26<br>
  ⏱️ updated 2 weeks ago<br>
  *Notify players about entity interactions.*

- **[schwarper/CS2TraceRay](https://github.com/schwarper/CS2TraceRay)**<br>
  ⭐ 20<br>
  ⏱️ updated 1 day ago<br>
  *A trace ray library developed for use in Counter Strike 2, in conjunction with the CounterStrikeSharp API. This enables the use of trace ray with TraceMask, Contents and skip enums.*

- **[qstage/CS2-HidePlayers](https://github.com/qstage/CS2-HidePlayers)**<br>
  ⭐ 20<br>
  ⏱️ updated 3 days ago<br>
  *Allows you to hide player models.*

- **[KillStr3aK/CS2-AntiDLL](https://github.com/KillStr3aK/CS2-AntiDLL)**<br>
  ⭐ 19<br>
  ⏱️ updated 4 months ago<br>
  *This plugin is similar to the CS:GO version.*

- **[Cruze03/Clientprefs](https://github.com/Cruze03/Clientprefs)**<br>
  ⭐ 19<br>
  ⏱️ updated 1 week ago<br>
  *This plugin exposes some natives for developers to save player data to SQLite / MySQL without actually adding sql code to your plugin giving developers easy access to save player cookie to database.*

- **[samyycX/CS2-SkyboxChanger](https://github.com/samyycX/CS2-SkyboxChanger)**<br>
  ⭐ 17<br>
  ⏱️ updated 2 weeks ago<br>
  *A plugin allow player to change their own skybox material, color and brightness on every map dynamically and seamlessly.*

- **[zakriamansoor47/SLAYER_Duel](https://github.com/zakriamansoor47/SLAYER_Duel)**<br>
  ⭐ 16<br>
  ⏱️ updated 1 week ago<br>
  *This Plugin allows Players to do 1vs1 Duel*

- **[qstage/CS2-FixRandomSpawn](https://github.com/qstage/CS2-FixRandomSpawn)**<br>
  ⭐ 16<br>
  ⏱️ updated 3 days ago<br>
  *Fixes convar `mp_randomspawn` for any game mode.*

- **[phara1/advanced-ff-cs2](https://github.com/phara1/advanced-ff-cs2)**<br>
  ⭐ 15<br>
  ⏱️ updated 1 week ago<br>
  *This plugin implements advanced control of friendly fire.*

- **[schwarper/cs2-anticheat](https://github.com/schwarper/cs2-anticheat)**<br>
  ⭐ 14<br>
  ⏱️ updated 15 hours ago<br>
  *cs2-anticheat is an anti-cheat system in development for CounterStrike 2.*

- **[K4ryuu/K4-AlwaysWeaponSkins](https://github.com/K4ryuu/K4-AlwaysWeaponSkins)**<br>
  ⭐ 12<br>
  ⏱️ updated 6 days ago<br>
  *This plugin enhances weapon skin visibility by ensuring your equipped Steam inventory skins are displayed consistently across both teams.*

- **[T3Marius/T3Menu-API](https://github.com/T3Marius/T3Menu-API)**<br>
  ⭐ 11<br>
  ⏱️ updated 19 hours ago<br>
  *T3Menu-API is a plugin created on counterstrikesharp with purpose of creating a better, refined menu controlled with player buttons.*

- **[zakriamansoor47/SLAYER_AntiCamp](https://github.com/zakriamansoor47/SLAYER_AntiCamp)**<br>
  ⭐ 9<br>
  ⏱️ updated 4 months ago<br>
  *This Plugin Detect player who is camping for a specific time.*

- **[T3Marius/MVP-Anthem](https://github.com/T3Marius/MVP-Anthem)**<br>
  ⭐ 9<br>
  ⏱️ updated 2 days ago<br>
  *A plugin that add custom mvp sound to the game.*

- **[samyycX/CSSharpPatcher](https://github.com/samyycX/CSSharpPatcher)**<br>
  ⭐ 8<br>
  ⏱️ updated 1 week ago<br>
  *A plugin with various patches for cs2.*

- **[darkerz7/CS2-HideTeammates](https://github.com/darkerz7/CS2-HideTeammates)**<br>
  ⭐ 8<br>
  ⏱️ updated 1 week ago<br>
  *Hides Teammates on the entire map or distance.*

- **[zakriamansoor47/SLAYER_UnrestrictedFOV](https://github.com/zakriamansoor47/SLAYER_UnrestrictedFOV)**<br>
  ⭐ 7<br>
  ⏱️ updated 4 months ago<br>
  *This simple plugin allow players to Change their FOV. Ported this plugin*

- **[darkerz7/CS2-EntityFix](https://github.com/darkerz7/CS2-EntityFix)**<br>
  ⭐ 7<br>
  ⏱️ updated 2 weeks ago<br>
  *Fixes game_player_equip, game_ui, IgniteLifeTime, point_viewcontrol, trigger_gravity. Idea taken from cs2fixes.*

- **[zakriamansoor47/SLAYER_HeadshotOnly](https://github.com/zakriamansoor47/SLAYER_HeadshotOnly)**<br>
  ⭐ 5<br>
  ⏱️ updated 4 months ago<br>
  *This plugin enables Headshot Only to all players OR Enables Headshot Only on Players themselves by using Public Command !hs.*

- **[zakriamansoor47/SLAYER_Noscope](https://github.com/zakriamansoor47/SLAYER_Noscope)**<br>
  ⭐ 5<br>
  ⏱️ updated 4 months ago<br>
  *This is my first plugin for CounterStrikeSharp. This plugin disables Scope of Scope Weapons like AWP, scout, etc..*

- **[Letaryat/CS2-Poor-MapPropAds](https://github.com/Letaryat/CS2-Poor-MapPropAds)**<br>
  ⭐ 3<br>
  ⏱️ updated 1 day ago<br>
  *This plugin allows for server owners to create billboard type advertisements that are placed on wall.*

- **[zakriamansoor47/SLAYER_Revive](https://github.com/zakriamansoor47/SLAYER_Revive)**<br>
  ⭐ 2<br>
  ⏱️ updated 5 days ago<br>
  *Revive teammates with 'E' (+use button)*

- **[TICHOJEBEC-SK/cs2-WeaponRestrict](https://github.com/TICHOJEBEC-SK/cs2-WeaponRestrict)**<br>
  ⭐ 2<br>
  ⏱️ updated 1 week ago<br>
  *A plugin that lets you restrict weapons by rules.*

- **[TICHOJEBEC-SK/cs2-WarnSystem](https://github.com/TICHOJEBEC-SK/cs2-WarnSystem)**<br>
  ⭐ 1<br>
  ⏱️ updated 14 hours ago<br>
  *A plugin that allows admins to warn players.*


## Swiftly Plugins

- **[swiftly-solution/admins](https://github.com/swiftly-solution/admins)**<br>
  ⭐ 4<br>
  ⏱️ updated 5 months ago<br>
  *A simple plugin for swiftly that implements an admin system.*


# Contributors

<table>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/1370533448"><img src="https://avatars.githubusercontent.com/u/53643730?v=4" width="64" height="64" alt="1370533448" /></a><br/>
      <a href="https://github.com/1370533448">@1370533448</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/1Mack"><img src="https://avatars.githubusercontent.com/u/60943107?v=4" width="64" height="64" alt="1Mack" /></a><br/>
      <a href="https://github.com/1Mack">@1Mack</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/2vg"><img src="https://avatars.githubusercontent.com/u/17700125?v=4" width="64" height="64" alt="2vg" /></a><br/>
      <a href="https://github.com/2vg">@2vg</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/akxcv"><img src="https://avatars.githubusercontent.com/u/17192674?v=4" width="64" height="64" alt="akxcv" /></a><br/>
      <a href="https://github.com/akxcv">@akxcv</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/AloneElxy"><img src="https://avatars.githubusercontent.com/u/74292375?v=4" width="64" height="64" alt="AloneElxy" /></a><br/>
      <a href="https://github.com/AloneElxy">@AloneElxy</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/AlphaKeks"><img src="https://avatars.githubusercontent.com/u/85143381?v=4" width="64" height="64" alt="AlphaKeks" /></a><br/>
      <a href="https://github.com/AlphaKeks">@AlphaKeks</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/AmnesiaLemon"><img src="https://avatars.githubusercontent.com/u/103835174?v=4" width="64" height="64" alt="AmnesiaLemon" /></a><br/>
      <a href="https://github.com/AmnesiaLemon">@AmnesiaLemon</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/AnshumanRohella"><img src="https://avatars.githubusercontent.com/u/6627611?v=4" width="64" height="64" alt="AnshumanRohella" /></a><br/>
      <a href="https://github.com/AnshumanRohella">@AnshumanRohella</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/ar1a"><img src="https://avatars.githubusercontent.com/u/8436007?v=4" width="64" height="64" alt="ar1a" /></a><br/>
      <a href="https://github.com/ar1a">@ar1a</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/asapverneri"><img src="https://avatars.githubusercontent.com/u/142944488?v=4" width="64" height="64" alt="asapverneri" /></a><br/>
      <a href="https://github.com/asapverneri">@asapverneri</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/asensionacher"><img src="https://avatars.githubusercontent.com/u/7094577?v=4" width="64" height="64" alt="asensionacher" /></a><br/>
      <a href="https://github.com/asensionacher">@asensionacher</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/audiomaster99"><img src="https://avatars.githubusercontent.com/u/116572799?v=4" width="64" height="64" alt="audiomaster99" /></a><br/>
      <a href="https://github.com/audiomaster99">@audiomaster99</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/B3none"><img src="https://avatars.githubusercontent.com/u/24966460?v=4" width="64" height="64" alt="B3none" /></a><br/>
      <a href="https://github.com/B3none">@B3none</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/blu133721"><img src="https://avatars.githubusercontent.com/u/73272097?v=4" width="64" height="64" alt="blu133721" /></a><br/>
      <a href="https://github.com/blu133721">@blu133721</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/borzaka"><img src="https://avatars.githubusercontent.com/u/1230402?v=4" width="64" height="64" alt="borzaka" /></a><br/>
      <a href="https://github.com/borzaka">@borzaka</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/brkvlr"><img src="https://avatars.githubusercontent.com/u/50466021?v=4" width="64" height="64" alt="brkvlr" /></a><br/>
      <a href="https://github.com/brkvlr">@brkvlr</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/CasaRica"><img src="https://avatars.githubusercontent.com/u/156474752?v=4" width="64" height="64" alt="CasaRica" /></a><br/>
      <a href="https://github.com/CasaRica">@CasaRica</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/CeLicat"><img src="https://avatars.githubusercontent.com/u/19570348?v=4" width="64" height="64" alt="CeLicat" /></a><br/>
      <a href="https://github.com/CeLicat">@CeLicat</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/characharm"><img src="https://avatars.githubusercontent.com/u/123120856?v=4" width="64" height="64" alt="characharm" /></a><br/>
      <a href="https://github.com/characharm">@characharm</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Cherno-Beliy"><img src="https://avatars.githubusercontent.com/u/143458283?v=4" width="64" height="64" alt="Cherno-Beliy" /></a><br/>
      <a href="https://github.com/Cherno-Beliy">@Cherno-Beliy</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/crashzk"><img src="https://avatars.githubusercontent.com/u/32937653?v=4" width="64" height="64" alt="crashzk" /></a><br/>
      <a href="https://github.com/crashzk">@crashzk</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/criskkky"><img src="https://avatars.githubusercontent.com/u/36176343?v=4" width="64" height="64" alt="criskkky" /></a><br/>
      <a href="https://github.com/criskkky">@criskkky</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Cruze03"><img src="https://avatars.githubusercontent.com/u/31343375?v=4" width="64" height="64" alt="Cruze03" /></a><br/>
      <a href="https://github.com/Cruze03">@Cruze03</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/daffyyyy"><img src="https://avatars.githubusercontent.com/u/41084667?v=4" width="64" height="64" alt="daffyyyy" /></a><br/>
      <a href="https://github.com/daffyyyy">@daffyyyy</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/darkerz7"><img src="https://avatars.githubusercontent.com/u/25752428?v=4" width="64" height="64" alt="darkerz7" /></a><br/>
      <a href="https://github.com/darkerz7">@darkerz7</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/deafps"><img src="https://avatars.githubusercontent.com/u/170218118?v=4" width="64" height="64" alt="deafps" /></a><br/>
      <a href="https://github.com/deafps">@deafps</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/DearCrazyLeaf"><img src="https://avatars.githubusercontent.com/u/124550277?v=4" width="64" height="64" alt="DearCrazyLeaf" /></a><br/>
      <a href="https://github.com/DearCrazyLeaf">@DearCrazyLeaf</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/DeonduPreez"><img src="https://avatars.githubusercontent.com/u/23405975?v=4" width="64" height="64" alt="DeonduPreez" /></a><br/>
      <a href="https://github.com/DeonduPreez">@DeonduPreez</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/apps/dependabot"><img src="https://avatars.githubusercontent.com/in/29110?v=4" width="64" height="64" alt="dependabot[bot]" /></a><br/>
      <a href="https://github.com/apps/dependabot">@dependabot[bot]</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/dollannn"><img src="https://avatars.githubusercontent.com/u/50216897?v=4" width="64" height="64" alt="dollannn" /></a><br/>
      <a href="https://github.com/dollannn">@dollannn</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/dr3fty"><img src="https://avatars.githubusercontent.com/u/12001194?v=4" width="64" height="64" alt="dr3fty" /></a><br/>
      <a href="https://github.com/dr3fty">@dr3fty</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Dying-Ducks"><img src="https://avatars.githubusercontent.com/u/109040754?v=4" width="64" height="64" alt="Dying-Ducks" /></a><br/>
      <a href="https://github.com/Dying-Ducks">@Dying-Ducks</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/e-n-v-i"><img src="https://avatars.githubusercontent.com/u/112311421?v=4" width="64" height="64" alt="e-n-v-i" /></a><br/>
      <a href="https://github.com/e-n-v-i">@e-n-v-i</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/e54385991"><img src="https://avatars.githubusercontent.com/u/19951346?v=4" width="64" height="64" alt="e54385991" /></a><br/>
      <a href="https://github.com/e54385991">@e54385991</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/EasterLee"><img src="https://avatars.githubusercontent.com/u/34824423?v=4" width="64" height="64" alt="EasterLee" /></a><br/>
      <a href="https://github.com/EasterLee">@EasterLee</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/ehwhattaugonnado"><img src="https://avatars.githubusercontent.com/u/54551926?v=4" width="64" height="64" alt="ehwhattaugonnado" /></a><br/>
      <a href="https://github.com/ehwhattaugonnado">@ehwhattaugonnado</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/exababy"><img src="https://avatars.githubusercontent.com/u/44870116?v=4" width="64" height="64" alt="exababy" /></a><br/>
      <a href="https://github.com/exababy">@exababy</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/exkludera"><img src="https://avatars.githubusercontent.com/u/51145038?v=4" width="64" height="64" alt="exkludera" /></a><br/>
      <a href="https://github.com/exkludera">@exkludera</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/fabiosantoscode"><img src="https://avatars.githubusercontent.com/u/1611595?v=4" width="64" height="64" alt="fabiosantoscode" /></a><br/>
      <a href="https://github.com/fabiosantoscode">@fabiosantoscode</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/FadelAlwan"><img src="https://avatars.githubusercontent.com/u/117265682?v=4" width="64" height="64" alt="FadelAlwan" /></a><br/>
      <a href="https://github.com/FadelAlwan">@FadelAlwan</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Faramour"><img src="https://avatars.githubusercontent.com/u/44729057?v=4" width="64" height="64" alt="Faramour" /></a><br/>
      <a href="https://github.com/Faramour">@Faramour</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/FlowingSPDG"><img src="https://avatars.githubusercontent.com/u/30292185?v=4" width="64" height="64" alt="FlowingSPDG" /></a><br/>
      <a href="https://github.com/FlowingSPDG">@FlowingSPDG</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/fltuna"><img src="https://avatars.githubusercontent.com/u/47306029?v=4" width="64" height="64" alt="fltuna" /></a><br/>
      <a href="https://github.com/fltuna">@fltuna</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/freakexeuLow"><img src="https://avatars.githubusercontent.com/u/32603929?v=4" width="64" height="64" alt="freakexeuLow" /></a><br/>
      <a href="https://github.com/freakexeuLow">@freakexeuLow</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Frozen-H2O"><img src="https://avatars.githubusercontent.com/u/43626458?v=4" width="64" height="64" alt="Frozen-H2O" /></a><br/>
      <a href="https://github.com/Frozen-H2O">@Frozen-H2O</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/GabrielBigardi"><img src="https://avatars.githubusercontent.com/u/42253181?v=4" width="64" height="64" alt="GabrielBigardi" /></a><br/>
      <a href="https://github.com/GabrielBigardi">@GabrielBigardi</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/GAMMACASE"><img src="https://avatars.githubusercontent.com/u/31375974?v=4" width="64" height="64" alt="GAMMACASE" /></a><br/>
      <a href="https://github.com/GAMMACASE">@GAMMACASE</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Geekvcn"><img src="https://avatars.githubusercontent.com/u/20044214?v=4" width="64" height="64" alt="Geekvcn" /></a><br/>
      <a href="https://github.com/Geekvcn">@Geekvcn</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/geison66"><img src="https://avatars.githubusercontent.com/u/17097504?v=4" width="64" height="64" alt="geison66" /></a><br/>
      <a href="https://github.com/geison66">@geison66</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/GekasD"><img src="https://avatars.githubusercontent.com/u/67982775?v=4" width="64" height="64" alt="GekasD" /></a><br/>
      <a href="https://github.com/GekasD">@GekasD</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/apps/github-actions"><img src="https://avatars.githubusercontent.com/in/15368?v=4" width="64" height="64" alt="github-actions[bot]" /></a><br/>
      <a href="https://github.com/apps/github-actions">@github-actions[bot]</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/grrhn"><img src="https://avatars.githubusercontent.com/u/105857708?v=4" width="64" height="64" alt="grrhn" /></a><br/>
      <a href="https://github.com/grrhn">@grrhn</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Hichatu"><img src="https://avatars.githubusercontent.com/u/47224085?v=4" width="64" height="64" alt="Hichatu" /></a><br/>
      <a href="https://github.com/Hichatu">@Hichatu</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/himenekocn"><img src="https://avatars.githubusercontent.com/u/9393126?v=4" width="64" height="64" alt="himenekocn" /></a><br/>
      <a href="https://github.com/himenekocn">@himenekocn</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/hzqst"><img src="https://avatars.githubusercontent.com/u/12287588?v=4" width="64" height="64" alt="hzqst" /></a><br/>
      <a href="https://github.com/hzqst">@hzqst</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/idk1703"><img src="https://avatars.githubusercontent.com/u/64554241?v=4" width="64" height="64" alt="idk1703" /></a><br/>
      <a href="https://github.com/idk1703">@idk1703</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Interesting-exe"><img src="https://avatars.githubusercontent.com/u/52731127?v=4" width="64" height="64" alt="Interesting-exe" /></a><br/>
      <a href="https://github.com/Interesting-exe">@Interesting-exe</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/ipsvn"><img src="https://avatars.githubusercontent.com/u/80017804?v=4" width="64" height="64" alt="ipsvn" /></a><br/>
      <a href="https://github.com/ipsvn">@ipsvn</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Iwhite67"><img src="https://avatars.githubusercontent.com/u/9698964?v=4" width="64" height="64" alt="Iwhite67" /></a><br/>
      <a href="https://github.com/Iwhite67">@Iwhite67</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/JackJack3231"><img src="https://avatars.githubusercontent.com/u/26525530?v=4" width="64" height="64" alt="JackJack3231" /></a><br/>
      <a href="https://github.com/JackJack3231">@JackJack3231</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Julienhqr"><img src="https://avatars.githubusercontent.com/u/43007197?v=4" width="64" height="64" alt="Julienhqr" /></a><br/>
      <a href="https://github.com/Julienhqr">@Julienhqr</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/jwsharpe"><img src="https://avatars.githubusercontent.com/u/23224124?v=4" width="64" height="64" alt="jwsharpe" /></a><br/>
      <a href="https://github.com/jwsharpe">@jwsharpe</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/K4ryuu"><img src="https://avatars.githubusercontent.com/u/104531589?v=4" width="64" height="64" alt="K4ryuu" /></a><br/>
      <a href="https://github.com/K4ryuu">@K4ryuu</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Katarina-E"><img src="https://avatars.githubusercontent.com/u/153746513?v=4" width="64" height="64" alt="Katarina-E" /></a><br/>
      <a href="https://github.com/Katarina-E">@Katarina-E</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/KillerRoi"><img src="https://avatars.githubusercontent.com/u/54289708?v=4" width="64" height="64" alt="KillerRoi" /></a><br/>
      <a href="https://github.com/KillerRoi">@KillerRoi</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/KillStr3aK"><img src="https://avatars.githubusercontent.com/u/19509520?v=4" width="64" height="64" alt="KillStr3aK" /></a><br/>
      <a href="https://github.com/KillStr3aK">@KillStr3aK</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/komashchenko"><img src="https://avatars.githubusercontent.com/u/22940384?v=4" width="64" height="64" alt="komashchenko" /></a><br/>
      <a href="https://github.com/komashchenko">@komashchenko</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/kraigher"><img src="https://avatars.githubusercontent.com/u/4018223?v=4" width="64" height="64" alt="kraigher" /></a><br/>
      <a href="https://github.com/kraigher">@kraigher</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Kroytz"><img src="https://avatars.githubusercontent.com/u/33564475?v=4" width="64" height="64" alt="Kroytz" /></a><br/>
      <a href="https://github.com/Kroytz">@Kroytz</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Kxnrl"><img src="https://avatars.githubusercontent.com/u/3905845?v=4" width="64" height="64" alt="Kxnrl" /></a><br/>
      <a href="https://github.com/Kxnrl">@Kxnrl</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/lanslide-team"><img src="https://avatars.githubusercontent.com/u/122711296?v=4" width="64" height="64" alt="lanslide-team" /></a><br/>
      <a href="https://github.com/lanslide-team">@lanslide-team</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Letaryat"><img src="https://avatars.githubusercontent.com/u/69041891?v=4" width="64" height="64" alt="Letaryat" /></a><br/>
      <a href="https://github.com/Letaryat">@Letaryat</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/m-arcuri"><img src="https://avatars.githubusercontent.com/u/124469923?v=4" width="64" height="64" alt="m-arcuri" /></a><br/>
      <a href="https://github.com/m-arcuri">@m-arcuri</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/m3ntorsky"><img src="https://avatars.githubusercontent.com/u/98771679?v=4" width="64" height="64" alt="m3ntorsky" /></a><br/>
      <a href="https://github.com/m3ntorsky">@m3ntorsky</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/mAa4a97"><img src="https://avatars.githubusercontent.com/u/34139457?v=4" width="64" height="64" alt="mAa4a97" /></a><br/>
      <a href="https://github.com/mAa4a97">@mAa4a97</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/marqdevx"><img src="https://avatars.githubusercontent.com/u/11246294?v=4" width="64" height="64" alt="marqdevx" /></a><br/>
      <a href="https://github.com/marqdevx">@marqdevx</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/mavproductions"><img src="https://avatars.githubusercontent.com/u/6368850?v=4" width="64" height="64" alt="mavproductions" /></a><br/>
      <a href="https://github.com/mavproductions">@mavproductions</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/maxime1907"><img src="https://avatars.githubusercontent.com/u/19607336?v=4" width="64" height="64" alt="maxime1907" /></a><br/>
      <a href="https://github.com/maxime1907">@maxime1907</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/MerakW"><img src="https://avatars.githubusercontent.com/u/34398344?v=4" width="64" height="64" alt="MerakW" /></a><br/>
      <a href="https://github.com/MerakW">@MerakW</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Mesharsky"><img src="https://avatars.githubusercontent.com/u/30102036?v=4" width="64" height="64" alt="Mesharsky" /></a><br/>
      <a href="https://github.com/Mesharsky">@Mesharsky</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/milkywayfarer"><img src="https://avatars.githubusercontent.com/u/17110335?v=4" width="64" height="64" alt="milkywayfarer" /></a><br/>
      <a href="https://github.com/milkywayfarer">@milkywayfarer</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/mrc4tt"><img src="https://avatars.githubusercontent.com/u/5301047?v=4" width="64" height="64" alt="mrc4tt" /></a><br/>
      <a href="https://github.com/mrc4tt">@mrc4tt</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/MSWS"><img src="https://avatars.githubusercontent.com/u/14448584?v=4" width="64" height="64" alt="MSWS" /></a><br/>
      <a href="https://github.com/MSWS">@MSWS</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/NaathySz"><img src="https://avatars.githubusercontent.com/u/97997774?v=4" width="64" height="64" alt="NaathySz" /></a><br/>
      <a href="https://github.com/NaathySz">@NaathySz</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Nereziel"><img src="https://avatars.githubusercontent.com/u/8618825?v=4" width="64" height="64" alt="Nereziel" /></a><br/>
      <a href="https://github.com/Nereziel">@Nereziel</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/nicedayzhu"><img src="https://avatars.githubusercontent.com/u/5286862?v=4" width="64" height="64" alt="nicedayzhu" /></a><br/>
      <a href="https://github.com/nicedayzhu">@nicedayzhu</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/NikolaJyun"><img src="https://avatars.githubusercontent.com/u/22559124?v=4" width="64" height="64" alt="NikolaJyun" /></a><br/>
      <a href="https://github.com/NikolaJyun">@NikolaJyun</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/NockyCZ"><img src="https://avatars.githubusercontent.com/u/63038995?v=4" width="64" height="64" alt="NockyCZ" /></a><br/>
      <a href="https://github.com/NockyCZ">@NockyCZ</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/nokkvireyr"><img src="https://avatars.githubusercontent.com/u/60022455?v=4" width="64" height="64" alt="nokkvireyr" /></a><br/>
      <a href="https://github.com/nokkvireyr">@nokkvireyr</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/notkoen"><img src="https://avatars.githubusercontent.com/u/45914779?v=4" width="64" height="64" alt="notkoen" /></a><br/>
      <a href="https://github.com/notkoen">@notkoen</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/nry1337"><img src="https://avatars.githubusercontent.com/u/40671068?v=4" width="64" height="64" alt="nry1337" /></a><br/>
      <a href="https://github.com/nry1337">@nry1337</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Nubston"><img src="https://avatars.githubusercontent.com/u/15358552?v=4" width="64" height="64" alt="Nubston" /></a><br/>
      <a href="https://github.com/Nubston">@Nubston</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/nuclearsilo583"><img src="https://avatars.githubusercontent.com/u/58926275?v=4" width="64" height="64" alt="nuclearsilo583" /></a><br/>
      <a href="https://github.com/nuclearsilo583">@nuclearsilo583</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/NYSHUN"><img src="https://avatars.githubusercontent.com/u/175985294?v=4" width="64" height="64" alt="NYSHUN" /></a><br/>
      <a href="https://github.com/NYSHUN">@NYSHUN</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/OniquirAK"><img src="https://avatars.githubusercontent.com/u/84151839?v=4" width="64" height="64" alt="OniquirAK" /></a><br/>
      <a href="https://github.com/OniquirAK">@OniquirAK</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/originalaidn"><img src="https://avatars.githubusercontent.com/u/45371311?v=4" width="64" height="64" alt="originalaidn" /></a><br/>
      <a href="https://github.com/originalaidn">@originalaidn</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/oscar-wos"><img src="https://avatars.githubusercontent.com/u/29248751?v=4" width="64" height="64" alt="oscar-wos" /></a><br/>
      <a href="https://github.com/oscar-wos">@oscar-wos</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/oylsister"><img src="https://avatars.githubusercontent.com/u/57207701?v=4" width="64" height="64" alt="oylsister" /></a><br/>
      <a href="https://github.com/oylsister">@oylsister</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Oz-Lin"><img src="https://avatars.githubusercontent.com/u/36224575?v=4" width="64" height="64" alt="Oz-Lin" /></a><br/>
      <a href="https://github.com/Oz-Lin">@Oz-Lin</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/panikajo"><img src="https://avatars.githubusercontent.com/u/4964185?v=4" width="64" height="64" alt="panikajo" /></a><br/>
      <a href="https://github.com/panikajo">@panikajo</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/partiusfabaa"><img src="https://avatars.githubusercontent.com/u/96542489?v=4" width="64" height="64" alt="partiusfabaa" /></a><br/>
      <a href="https://github.com/partiusfabaa">@partiusfabaa</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/pc-dongles"><img src="https://avatars.githubusercontent.com/u/79170834?v=4" width="64" height="64" alt="pc-dongles" /></a><br/>
      <a href="https://github.com/pc-dongles">@pc-dongles</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/PhantomYopta"><img src="https://avatars.githubusercontent.com/u/129750207?v=4" width="64" height="64" alt="PhantomYopta" /></a><br/>
      <a href="https://github.com/PhantomYopta">@PhantomYopta</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/phara1"><img src="https://avatars.githubusercontent.com/u/129111509?v=4" width="64" height="64" alt="phara1" /></a><br/>
      <a href="https://github.com/phara1">@phara1</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Poggicek"><img src="https://avatars.githubusercontent.com/u/45881722?v=4" width="64" height="64" alt="Poggicek" /></a><br/>
      <a href="https://github.com/Poggicek">@Poggicek</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/poggicek"><img src="https://github.com/poggicek.png" width="64" height="64" alt="poggicek" /></a><br/>
      <a href="https://github.com/poggicek">@poggicek</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/qq410525209"><img src="https://avatars.githubusercontent.com/u/47157419?v=4" width="64" height="64" alt="qq410525209" /></a><br/>
      <a href="https://github.com/qq410525209">@qq410525209</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/qstage"><img src="https://avatars.githubusercontent.com/u/166386817?v=4" width="64" height="64" alt="qstage" /></a><br/>
      <a href="https://github.com/qstage">@qstage</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Ravid-A"><img src="https://avatars.githubusercontent.com/u/72127473?v=4" width="64" height="64" alt="Ravid-A" /></a><br/>
      <a href="https://github.com/Ravid-A">@Ravid-A</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/rcon420"><img src="https://avatars.githubusercontent.com/u/47292145?v=4" width="64" height="64" alt="rcon420" /></a><br/>
      <a href="https://github.com/rcon420">@rcon420</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/ReneRebsdorf"><img src="https://avatars.githubusercontent.com/u/44376705?v=4" width="64" height="64" alt="ReneRebsdorf" /></a><br/>
      <a href="https://github.com/ReneRebsdorf">@ReneRebsdorf</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/rodopoulos1"><img src="https://avatars.githubusercontent.com/u/101236856?v=4" width="64" height="64" alt="rodopoulos1" /></a><br/>
      <a href="https://github.com/rodopoulos1">@rodopoulos1</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/roflmuffin"><img src="https://github.com/roflmuffin.png" width="64" height="64" alt="roflmuffin" /></a><br/>
      <a href="https://github.com/roflmuffin">@roflmuffin</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/roxyrekt"><img src="https://avatars.githubusercontent.com/u/87309991?v=4" width="64" height="64" alt="roxyrekt" /></a><br/>
      <a href="https://github.com/roxyrekt">@roxyrekt</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/RoyZ-iwnl"><img src="https://avatars.githubusercontent.com/u/24809366?v=4" width="64" height="64" alt="RoyZ-iwnl" /></a><br/>
      <a href="https://github.com/RoyZ-iwnl">@RoyZ-iwnl</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/rsKliPPy"><img src="https://avatars.githubusercontent.com/u/9073673?v=4" width="64" height="64" alt="rsKliPPy" /></a><br/>
      <a href="https://github.com/rsKliPPy">@rsKliPPy</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/samyycX"><img src="https://avatars.githubusercontent.com/u/60744529?v=4" width="64" height="64" alt="samyycX" /></a><br/>
      <a href="https://github.com/samyycX">@samyycX</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/sarim-hk"><img src="https://avatars.githubusercontent.com/u/58489447?v=4" width="64" height="64" alt="sarim-hk" /></a><br/>
      <a href="https://github.com/sarim-hk">@sarim-hk</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Satttoshi"><img src="https://avatars.githubusercontent.com/u/109807794?v=4" width="64" height="64" alt="Satttoshi" /></a><br/>
      <a href="https://github.com/Satttoshi">@Satttoshi</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/schwarper"><img src="https://avatars.githubusercontent.com/u/75811921?v=4" width="64" height="64" alt="schwarper" /></a><br/>
      <a href="https://github.com/schwarper">@schwarper</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/shobhit-pathak"><img src="https://avatars.githubusercontent.com/u/140690706?v=4" width="64" height="64" alt="shobhit-pathak" /></a><br/>
      <a href="https://github.com/shobhit-pathak">@shobhit-pathak</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/sirNugg3ts"><img src="https://avatars.githubusercontent.com/u/28486181?v=4" width="64" height="64" alt="sirNugg3ts" /></a><br/>
      <a href="https://github.com/sirNugg3ts">@sirNugg3ts</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/skuzzis"><img src="https://avatars.githubusercontent.com/u/61626661?v=4" width="64" height="64" alt="skuzzis" /></a><br/>
      <a href="https://github.com/skuzzis">@skuzzis</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/sniperpl"><img src="https://avatars.githubusercontent.com/u/87908771?v=4" width="64" height="64" alt="sniperpl" /></a><br/>
      <a href="https://github.com/sniperpl">@sniperpl</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/snorux"><img src="https://avatars.githubusercontent.com/u/34697265?v=4" width="64" height="64" alt="snorux" /></a><br/>
      <a href="https://github.com/snorux">@snorux</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/snowhp"><img src="https://avatars.githubusercontent.com/u/13867481?v=4" width="64" height="64" alt="snowhp" /></a><br/>
      <a href="https://github.com/snowhp">@snowhp</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Source2ZE"><img src="https://avatars.githubusercontent.com/u/129127192?v=4" width="64" height="64" alt="Source2ZE" /></a><br/>
      <a href="https://github.com/Source2ZE">@Source2ZE</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/sphaxa"><img src="https://avatars.githubusercontent.com/u/25424125?v=4" width="64" height="64" alt="sphaxa" /></a><br/>
      <a href="https://github.com/sphaxa">@sphaxa</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/st1ng2"><img src="https://avatars.githubusercontent.com/u/41505081?v=4" width="64" height="64" alt="st1ng2" /></a><br/>
      <a href="https://github.com/st1ng2">@st1ng2</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/stefanx111"><img src="https://avatars.githubusercontent.com/u/60297289?v=4" width="64" height="64" alt="stefanx111" /></a><br/>
      <a href="https://github.com/stefanx111">@stefanx111</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/STONE-GPY"><img src="https://avatars.githubusercontent.com/u/131870243?v=4" width="64" height="64" alt="STONE-GPY" /></a><br/>
      <a href="https://github.com/STONE-GPY">@STONE-GPY</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/swiftly-solution"><img src="https://avatars.githubusercontent.com/u/118755242?v=4" width="64" height="64" alt="swiftly-solution" /></a><br/>
      <a href="https://github.com/swiftly-solution">@swiftly-solution</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/szogun1910"><img src="https://avatars.githubusercontent.com/u/69729783?v=4" width="64" height="64" alt="szogun1910" /></a><br/>
      <a href="https://github.com/szogun1910">@szogun1910</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/T3Marius"><img src="https://avatars.githubusercontent.com/u/168598779?v=4" width="64" height="64" alt="T3Marius" /></a><br/>
      <a href="https://github.com/T3Marius">@T3Marius</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/T3Marius-hub"><img src="https://avatars.githubusercontent.com/u/173165797?v=4" width="64" height="64" alt="T3Marius-hub" /></a><br/>
      <a href="https://github.com/T3Marius-hub">@T3Marius-hub</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/The0mikkel"><img src="https://avatars.githubusercontent.com/u/28625667?v=4" width="64" height="64" alt="The0mikkel" /></a><br/>
      <a href="https://github.com/The0mikkel">@The0mikkel</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/thechrisnixon"><img src="https://avatars.githubusercontent.com/u/672057?v=4" width="64" height="64" alt="thechrisnixon" /></a><br/>
      <a href="https://github.com/thechrisnixon">@thechrisnixon</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/ThunderClapZ"><img src="https://avatars.githubusercontent.com/u/25366481?v=4" width="64" height="64" alt="ThunderClapZ" /></a><br/>
      <a href="https://github.com/ThunderClapZ">@ThunderClapZ</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/TICHOJEBEC-SK"><img src="https://avatars.githubusercontent.com/u/150498032?v=4" width="64" height="64" alt="TICHOJEBEC-SK" /></a><br/>
      <a href="https://github.com/TICHOJEBEC-SK">@TICHOJEBEC-SK</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/tilgep"><img src="https://avatars.githubusercontent.com/u/66904238?v=4" width="64" height="64" alt="tilgep" /></a><br/>
      <a href="https://github.com/tilgep">@tilgep</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/tiltysola"><img src="https://avatars.githubusercontent.com/u/19757919?v=4" width="64" height="64" alt="tiltysola" /></a><br/>
      <a href="https://github.com/tiltysola">@tiltysola</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/umbr1X"><img src="https://avatars.githubusercontent.com/u/123817480?v=4" width="64" height="64" alt="umbr1X" /></a><br/>
      <a href="https://github.com/umbr1X">@umbr1X</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/UpkkXnet"><img src="https://avatars.githubusercontent.com/u/96552017?v=4" width="64" height="64" alt="UpkkXnet" /></a><br/>
      <a href="https://github.com/UpkkXnet">@UpkkXnet</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Vauff"><img src="https://avatars.githubusercontent.com/u/6075172?v=4" width="64" height="64" alt="Vauff" /></a><br/>
      <a href="https://github.com/Vauff">@Vauff</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Wend4r"><img src="https://avatars.githubusercontent.com/u/47463683?v=4" width="64" height="64" alt="Wend4r" /></a><br/>
      <a href="https://github.com/Wend4r">@Wend4r</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/wiruwiru"><img src="https://avatars.githubusercontent.com/u/61034981?v=4" width="64" height="64" alt="wiruwiru" /></a><br/>
      <a href="https://github.com/wiruwiru">@wiruwiru</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/xen-000"><img src="https://avatars.githubusercontent.com/u/24222257?v=4" width="64" height="64" alt="xen-000" /></a><br/>
      <a href="https://github.com/xen-000">@xen-000</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Yarukon"><img src="https://avatars.githubusercontent.com/u/61296195?v=4" width="64" height="64" alt="Yarukon" /></a><br/>
      <a href="https://github.com/Yarukon">@Yarukon</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/yonilerner"><img src="https://avatars.githubusercontent.com/u/278810?v=4" width="64" height="64" alt="yonilerner" /></a><br/>
      <a href="https://github.com/yonilerner">@yonilerner</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/zakriamansoor47"><img src="https://avatars.githubusercontent.com/u/56433510?v=4" width="64" height="64" alt="zakriamansoor47" /></a><br/>
      <a href="https://github.com/zakriamansoor47">@zakriamansoor47</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Zeisenx"><img src="https://avatars.githubusercontent.com/u/19303143?v=4" width="64" height="64" alt="Zeisenx" /></a><br/>
      <a href="https://github.com/Zeisenx">@Zeisenx</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/zer0k-z"><img src="https://avatars.githubusercontent.com/u/61156310?v=4" width="64" height="64" alt="zer0k-z" /></a><br/>
      <a href="https://github.com/zer0k-z">@zer0k-z</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/zhw1nq"><img src="https://avatars.githubusercontent.com/u/132770113?v=4" width="64" height="64" alt="zhw1nq" /></a><br/>
      <a href="https://github.com/zhw1nq">@zhw1nq</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/ZMatu"><img src="https://avatars.githubusercontent.com/u/78674116?v=4" width="64" height="64" alt="ZMatu" /></a><br/>
      <a href="https://github.com/ZMatu">@ZMatu</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/zwolof"><img src="https://avatars.githubusercontent.com/u/21288834?v=4" width="64" height="64" alt="zwolof" /></a><br/>
      <a href="https://github.com/zwolof">@zwolof</a>
    </td>
  </tr>
</table>


# Contributing

## How to add plugins
Add an entry in `manifests/xxx.json` and follow the same format as the other entries, the github workflow will auto update the `README.md`.

## Rules
- Plugin must be open source
- Plugin must be functioning

This project is a free and open-source project. We welcome any community resource websites/repositories/plugins as long as they follow the rules above, regardless of their popularity.\
Please feel free to submit pull requests or issues, we need your contributions!
