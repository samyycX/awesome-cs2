<div align="center" style="text-align: center">
<h3>Awesome CS2</h3>
<p>
  An awesome list for all available cs2 development information, including modding frameworks, development resources, plugins and etc.
</p>
<p>
  Last Sync: <strong>17 minutes ago</strong>
</p>
<p>
  Project Uptime: <strong>12 hours</strong>
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
- [Contributions](#contributions)

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
  ⏱️ updated 3 hours ago<br>
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

- **[Source2ZE/CS2ServerGUI](https://github.com/Source2ZE/CS2ServerGUI)**<br>
  ⭐ 48<br>
  ⏱️ updated 1 week ago<br>
  *A plugin that shows entities, net messages, events and etc with a GUI.*

- **[Source2ZE/CS2ServerGUI](https://github.com/Source2ZE/CS2ServerGUI)**<br>
  ⭐ 48<br>
  ⏱️ updated 1 week ago<br>
  *A plugin that shows entities, net messages, events and etc with a GUI.*

- **[Source2ZE/StripperCS2](https://github.com/Source2ZE/StripperCS2)**<br>
  ⭐ 45<br>
  ⏱️ updated 1 week ago<br>
  *A plugin that allows server operators to manage map lump data similarly to how Stripper:Source worked.*

- **[Source2ZE/AcceleratorCS2](https://github.com/Source2ZE/AcceleratorCS2)**<br>
  ⭐ 28<br>
  ⏱️ updated 2 weeks ago<br>
  *A plugin that generate a crash dump when there's a crash.*

- **[samyycX/Audio](https://github.com/samyycX/Audio)**<br>
  ⭐ 13<br>
  ⏱️ updated 4 days ago<br>
  *A demo and a metamod lib to provide similar functions to the previous SM-Ext-Audio extension in csgo, that is, sending custom audio streams such as a song through a bot's voice chat.*

- **[GAMMACASE/Source2SchemaDumper](https://github.com/GAMMACASE/Source2SchemaDumper)**<br>
  ⭐ 11<br>
  ⏱️ updated 5 days ago<br>
  *A plugin that can dump the schemas and generate a header file.*


## CounterStrikeSharp Plugins

- **[Nereziel/cs2-WeaponPaints](https://github.com/Nereziel/cs2-WeaponPaints)**<br>
  ⭐ 312<br>
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

- **[daffyyyy/CS2-Tags](https://github.com/daffyyyy/CS2-Tags)**<br>
  ⭐ 52<br>
  ⏱️ updated 1 year ago<br>
  *Adds tags to the server that can be easily edited, tags can be assigned via permission or steamid64.*

- **[schwarper/cs2-tags](https://github.com/schwarper/cs2-tags)**<br>
  ⭐ 41<br>
  ⏱️ updated 2 weeks ago<br>
  *A tag plugin designed to enhance your CS2 experience with a dynamic tagging system. Customise and manage player tags effortlessly for a more interactive and engaging game environment.*

- **[schwarper/CS2MenuManager](https://github.com/schwarper/CS2MenuManager)**<br>
  ⭐ 35<br>
  ⏱️ updated 3 weeks ago<br>
  *CS2MenuManager is a modern, extensible and easy to use menu system for Counter-Strike 2 based on the CounterStrikeSharp library.*

- **[schwarper/CS2TraceRay](https://github.com/schwarper/CS2TraceRay)**<br>
  ⭐ 20<br>
  ⏱️ updated 1 day ago<br>
  *A trace ray library developed for use in Counter Strike 2, in conjunction with the CounterStrikeSharp API. This enables the use of trace ray with TraceMask, Contents and skip enums.*

- **[samyycX/CS2-SkyboxChanger](https://github.com/samyycX/CS2-SkyboxChanger)**<br>
  ⭐ 17<br>
  ⏱️ updated 2 weeks ago<br>
  *A plugin allow player to change their own skybox material, color and brightness on every map dynamically and seamlessly.*

- **[schwarper/cs2-anticheat](https://github.com/schwarper/cs2-anticheat)**<br>
  ⭐ 14<br>
  ⏱️ updated 12 hours ago<br>
  *cs2-anticheat is an anti-cheat system in development for CounterStrike 2.*

- **[T3Marius/T3Menu-API](https://github.com/T3Marius/T3Menu-API)**<br>
  ⭐ 11<br>
  ⏱️ updated 17 hours ago<br>
  *T3Menu-API is a plugin created on counterstrikesharp with purpose of creating a better, refined menu controlled with player buttons.*

- **[samyycX/CSSharpPatcher](https://github.com/samyycX/CSSharpPatcher)**<br>
  ⭐ 8<br>
  ⏱️ updated 1 week ago<br>
  *A plugin with various patches for cs2.*

- **[TICHOJEBEC-SK/cs2-WarnSystem](https://github.com/TICHOJEBEC-SK/cs2-WarnSystem)**<br>
  ⭐ 1<br>
  ⏱️ updated 11 hours ago<br>
  *A plugin that allows admins to warn players.*


## Swiftly Plugins

- **[swiftly-solution/admins](https://github.com/swiftly-solution/admins)**<br>
  ⭐ 4<br>
  ⏱️ updated 5 months ago<br>
  *A simple plugin for swiftly that implements an admin system.*


# Contributions

## Rules
- Plugin must be open source
- Plugin must be functioning

This project is a free and open-source project. We welcome any community resource websites/repositories/plugins as long as they follow the rules above, regardless of their popularity.\
Please feel free to submit pull requests or issues, we need your contributions!
