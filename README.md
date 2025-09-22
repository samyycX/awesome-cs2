<div align="center" style="text-align: center">
<h3>Awesome CS2</h3>
<p>
  An awesome list for all available cs2 development information, including modding frameworks, development resources, plugins and etc.
</p>
<p>
  Last Sync: <strong>2025/09/21 02:02:29</strong>
</p>
<p>
  Project Uptime: <strong>3 weeks</strong>
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

- **[S2TS](https://s2ts.net/)**\
  *A project that compiles typescript codes into .vts_c files that can run in cs2 scripting engine.*\
  *Also provide documentation for current SourceTS API.*

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
  ⭐ 320<br>
  ⏱️ updated 3 days ago<br>
  *A plugin with tons of fixes and features aimed but not limited to zombie escape.*

- **[KZGlobalTeam/cs2kz-metamod](https://github.com/KZGlobalTeam/cs2kz-metamod)**<br>
  ⭐ 162<br>
  ⏱️ updated 20 hours ago<br>
  *KZ plugin for cs2. WIP, not ready for release.*

- **[Source2ZE/MultiAddonManager](https://github.com/Source2ZE/MultiAddonManager)**<br>
  ⭐ 107<br>
  ⏱️ updated 5 days ago<br>
  *A plugin that allows you to use multiple workshop addons at once and have clients download them.*

- **[Salvatore-Als/cs2-fake-rcon](https://github.com/Salvatore-Als/cs2-fake-rcon)**<br>
  ⭐ 56<br>
  ⏱️ updated 3 days ago<br>
  *Fakercon adds the fake_rcon_password and fake_rcon commands because Valve has not integrated the original command into the game (or it is broken).*

- **[Source2ZE/CleanerCS2](https://github.com/Source2ZE/CleanerCS2)**<br>
  ⭐ 55<br>
  ⏱️ updated 4 days ago<br>
  *A simple plugin that allows you to filter out console prints with regular expressions.*

- **[Source2ZE/ServerListPlayersFix](https://github.com/Source2ZE/ServerListPlayersFix)**<br>
  ⭐ 53<br>
  ⏱️ updated 4 days ago<br>
  *Populates the user information inside the steam api, as a result this fixes the players not showing up in the server browser.*

- **[Source2ZE/MovementUnlocker](https://github.com/Source2ZE/MovementUnlocker)**<br>
  ⭐ 52<br>
  ⏱️ updated 2 days ago<br>
  *A plugin that removes the max speed limitation from players on the ground, feels like CS:S. Useful for zombie knockback, several movement gamemodes, or just easier bhop.*

- **[Source2ZE/CS2ServerGUI](https://github.com/Source2ZE/CS2ServerGUI)**<br>
  ⭐ 49<br>
  ⏱️ updated 2 days ago<br>
  *A plugin that shows entities, net messages, events and etc with a GUI.*

- **[Source2ZE/StripperCS2](https://github.com/Source2ZE/StripperCS2)**<br>
  ⭐ 45<br>
  ⏱️ updated 1 month ago<br>
  *A plugin that allows server operators to manage map lump data similarly to how Stripper:Source worked.*

- **[Cruze03/FakeRanks-RevealAll](https://github.com/Cruze03/FakeRanks-RevealAll)**<br>
  ⭐ 42<br>
  ⏱️ updated 4 days ago<br>
  *A metamod plugin that reveals ranks of all players in server for player who presses tab.*

- **[Interesting-exe/CS2Fixes-RampbugFix](https://github.com/Interesting-exe/CS2Fixes-RampbugFix)**<br>
  ⭐ 30<br>
  ⏱️ updated 3 days ago<br>
  *Minimizes rampbugs. This plugin isn't perfect and rampbugs will continue to occur until Valve decides to finally fix them.*

- **[Source2ZE/AcceleratorCS2](https://github.com/Source2ZE/AcceleratorCS2)**<br>
  ⭐ 27<br>
  ⏱️ updated 1 month ago<br>
  *A plugin that generate a crash dump when there's a crash.*

- **[samyycX/Audio](https://github.com/samyycX/Audio)**<br>
  ⭐ 14<br>
  ⏱️ updated 1 month ago<br>
  *A demo and a metamod lib to provide similar functions to the previous SM-Ext-Audio extension in csgo, that is, sending custom audio streams such as a song through a bot's voice chat.*

- **[GAMMACASE/Source2SchemaDumper](https://github.com/GAMMACASE/Source2SchemaDumper)**<br>
  ⭐ 12<br>
  ⏱️ updated 1 month ago<br>
  *A plugin that can dump the schemas and generate a header file.*

- **[Cruze03/GameBanFix](https://github.com/Cruze03/GameBanFix)**<br>
  ⭐ 10<br>
  ⏱️ updated 4 days ago<br>
  *Fixes issue where if a player with game ban joins, other players even without a ban are then unable to join.*


## CounterStrikeSharp Plugins

- **[shobhit-pathak/MatchZy](https://github.com/shobhit-pathak/MatchZy)**<br>
  ⭐ 374<br>
  ⏱️ updated 2 weeks ago<br>
  *MatchZy is a plugin for CS2 (Counter Strike 2) for running and managing practice/pugs/scrims/matches with easy configuration!*

- **[Nereziel/cs2-WeaponPaints](https://github.com/Nereziel/cs2-WeaponPaints)**<br>
  ⭐ 315<br>
  ⏱️ updated 3 days ago<br>
  *A plugin to change weapon paints, gloves, agents and etc.*

- **[B3none/cs2-retakes](https://github.com/B3none/cs2-retakes)**<br>
  ⭐ 284<br>
  ⏱️ updated 2 days ago<br>
  *CS2 implementation of retakes written in C# for CounterStrikeSharp. Based on the version for CS:GO by Splewis.*

- **[daffyyyy/CS2-SimpleAdmin](https://github.com/daffyyyy/CS2-SimpleAdmin)**<br>
  ⭐ 149<br>
  ⏱️ updated 2 weeks ago<br>
  *Manage your Counter-Strike 2 server with simple commands!*

- **[counterstrikesharp-panel/css-bans](https://github.com/counterstrikesharp-panel/css-bans)**<br>
  ⭐ 129<br>
  ⏱️ updated 2 months ago<br>
  *CSS-BANS is an admin web panel for Counter-Strike 2, powered by CounterStrikeSharp.*

- **[samyycX/CS2-PlayerModelChanger](https://github.com/samyycX/CS2-PlayerModelChanger)**<br>
  ⭐ 110<br>
  ⏱️ updated 3 weeks ago<br>
  *A cssharp plugin to change player models.*

- **[NockyCZ/CS2-Deathmatch](https://github.com/NockyCZ/CS2-Deathmatch)**<br>
  ⭐ 106<br>
  ⏱️ updated 1 month ago<br>
  *A plugin to implement deathmatch gamemode.*

- **[NiGHT757/AFKManager](https://github.com/NiGHT757/AFKManager)**<br>
  ⭐ 71<br>
  ⏱️ updated 1 day ago<br>
  *AFK Manager plugin for CS2 based on player-checker by sazonische from CS:GO.*

- **[partiusfabaa/cs2-VIPCore](https://github.com/partiusfabaa/cs2-VIPCore)**<br>
  ⭐ 69<br>
  ⏱️ updated 3 weeks ago<br>
  *A vip plugin for cs2.*

- **[partiusfabaa/cs2-ranks](https://github.com/partiusfabaa/cs2-ranks)**<br>
  ⭐ 59<br>
  ⏱️ updated 1 month ago<br>
  *Each player is assigned a rank based on their accumulated experience points. Ranks range from "None" to the prestigious "The Global Elite."*

- **[oqyh/cs2-Game-Manager-GoldKingZ](https://github.com/oqyh/cs2-Game-Manager-GoldKingZ)**<br>
  ⭐ 59<br>
  ⏱️ updated 4 months ago<br>
  *Block/Hide unnecessaries in game.*

- **[B3none/cs2-instadefuse](https://github.com/B3none/cs2-instadefuse)**<br>
  ⭐ 55<br>
  ⏱️ updated 1 year ago<br>
  *A plugin that allows players to instantly defuse the bomb.*

- **[Lan2Play/PugSharp](https://github.com/Lan2Play/PugSharp)**<br>
  ⭐ 54<br>
  ⏱️ updated 2 weeks ago<br>
  *Pugsharp is a PUG System Plugin for CS2 based on the awesome CounterStrikeSharp by roflmuffin.*

- **[daffyyyy/CS2-Tags](https://github.com/daffyyyy/CS2-Tags)**<br>
  ⭐ 53<br>
  ⏱️ updated 1 year ago<br>
  *Adds tags to the server that can be easily edited, tags can be assigned via permission or steamid64.*

- **[Cruze03/FortniteEmotesNDances](https://github.com/Cruze03/FortniteEmotesNDances)**<br>
  ⭐ 52<br>
  ⏱️ updated 1 month ago<br>
  *This plugin allows players to use Emotes & Dances just like Fortnite.*

- **[KillStr3aK/ResourcePrecacher](https://github.com/KillStr3aK/ResourcePrecacher)**<br>
  ⭐ 46<br>
  ⏱️ updated 3 months ago<br>
  *This plugin can precache custom resources.*

- **[Oz-Lin/cs2-rockthevote](https://github.com/Oz-Lin/cs2-rockthevote)**<br>
  ⭐ 44<br>
  ⏱️ updated 1 month ago<br>
  *General purpose map voting plugin, started as a simple RTV and now has more features.*

- **[schwarper/cs2-tags](https://github.com/schwarper/cs2-tags)**<br>
  ⭐ 42<br>
  ⏱️ updated 1 month ago<br>
  *A tag plugin designed to enhance your CS2 experience with a dynamic tagging system. Customise and manage player tags effortlessly for a more interactive and engaging game environment.*

- **[schwarper/CS2MenuManager](https://github.com/schwarper/CS2MenuManager)**<br>
  ⭐ 36<br>
  ⏱️ updated 1 month ago<br>
  *CS2MenuManager is a modern, extensible and easy to use menu system for Counter-Strike 2 based on the CounterStrikeSharp library.*

- **[zwolof/cs2-executes](https://github.com/zwolof/cs2-executes)**<br>
  ⭐ 32<br>
  ⏱️ updated 5 hours ago<br>
  *CS2 implementation of executes written in C# for CounterStrikeSharp. Based on the version for CS:GO by Splewis.*

- **[HvH-gg/CS2-Essentials](https://github.com/HvH-gg/CS2-Essentials)**<br>
  ⭐ 30<br>
  ⏱️ updated 1 month ago<br>
  *It includes basic features like reset score and rage quit as well as optional restrictions for weapons, friendly fire, rapid fire and other exploit/crash fixes.*

- **[ssypchenko/cs2-gungame](https://github.com/ssypchenko/cs2-gungame)**<br>
  ⭐ 27<br>
  ⏱️ updated 4 weeks ago<br>
  *GunGame is a gameplay plugin inspired by the SourceMode GunGame plugin.*

- **[oqyh/cs2-Connect-Disconnect-Sound-GoldKingZ](https://github.com/oqyh/cs2-Connect-Disconnect-Sound-GoldKingZ)**<br>
  ⭐ 27<br>
  ⏱️ updated 4 months ago<br>
  *Emit a sound when a player connects or disconnects.*

- **[R0mz1k/css-C4-Timer](https://github.com/R0mz1k/css-C4-Timer)**<br>
  ⭐ 27<br>
  ⏱️ updated 9 months ago<br>
  *This plugin adds countdown to c4 bomb explosion to your server.*

- **[darkerz7/EntWatchSharp](https://github.com/darkerz7/EntWatchSharp)**<br>
  ⭐ 26<br>
  ⏱️ updated 3 days ago<br>
  *Notify players about entity interactions.*

- **[oqyh/cs2-Chat-Logger-GoldKingZ](https://github.com/oqyh/cs2-Chat-Logger-GoldKingZ)**<br>
  ⭐ 26<br>
  ⏱️ updated 3 months ago<br>
  *Log chat to local/discord webhook/mysql/web server.*

- **[schwarper/CS2TraceRay](https://github.com/schwarper/CS2TraceRay)**<br>
  ⭐ 23<br>
  ⏱️ updated 3 days ago<br>
  *A trace ray library developed for use in Counter Strike 2, in conjunction with the CounterStrikeSharp API. This enables the use of trace ray with TraceMask, Contents and skip enums.*

- **[grrhn/ThirdPerson-WIP](https://github.com/grrhn/ThirdPerson-WIP)**<br>
  ⭐ 22<br>
  ⏱️ updated 8 months ago<br>
  *WIP ThirdPerson plugin for CS2 expect bugs.*

- **[Cruze03/Clientprefs](https://github.com/Cruze03/Clientprefs)**<br>
  ⭐ 20<br>
  ⏱️ updated 1 month ago<br>
  *This plugin exposes some natives for developers to save player data to SQLite / MySQL without actually adding sql code to your plugin giving developers easy access to save player cookie to database.*

- **[qstage/CS2-HidePlayers](https://github.com/qstage/CS2-HidePlayers)**<br>
  ⭐ 19<br>
  ⏱️ updated 2 weeks ago<br>
  *Allows you to hide player models.*

- **[KillStr3aK/CS2-AntiDLL](https://github.com/KillStr3aK/CS2-AntiDLL)**<br>
  ⭐ 18<br>
  ⏱️ updated 5 months ago<br>
  *This plugin is similar to the CS:GO version.*

- **[samyycX/CS2-SkyboxChanger](https://github.com/samyycX/CS2-SkyboxChanger)**<br>
  ⭐ 17<br>
  ⏱️ updated 1 month ago<br>
  *A plugin allow player to change their own skybox material, color and brightness on every map dynamically and seamlessly.*

- **[wiruwiru/AutomaticAds-CS2](https://github.com/wiruwiru/AutomaticAds-CS2)**<br>
  ⭐ 17<br>
  ⏱️ updated 1 month ago<br>
  *This plugin allows you to schedule and display announcements in the chat at customizable intervals. Each announcement is accompanied by a brief sound effect to capture players' attention seamlessly.*

- **[zakriamansoor47/SLAYER_Duel](https://github.com/zakriamansoor47/SLAYER_Duel)**<br>
  ⭐ 16<br>
  ⏱️ updated 3 weeks ago<br>
  *This plugin allows players to do 1vs1 duel.*

- **[phara1/advanced-ff-cs2](https://github.com/phara1/advanced-ff-cs2)**<br>
  ⭐ 16<br>
  ⏱️ updated 5 days ago<br>
  *This plugin implements advanced control of friendly fire.*

- **[qstage/CS2-FixRandomSpawn](https://github.com/qstage/CS2-FixRandomSpawn)**<br>
  ⭐ 16<br>
  ⏱️ updated 4 weeks ago<br>
  *Fixes convar `mp_randomspawn` for any game mode.*

- **[PhantomYopta/CS2_Speedometer](https://github.com/PhantomYopta/CS2_Speedometer)**<br>
  ⭐ 16<br>
  ⏱️ updated 1 year ago<br>
  *Just a speedometer for CS2.*

- **[HvH-gg/TeleportFix](https://github.com/HvH-gg/TeleportFix)**<br>
  ⭐ 15<br>
  ⏱️ updated 1 month ago<br>
  *CounterStrikeSharp plugin to fix the teleport/airstuck/crash exploit.*

- **[Cruze03/cs2_blockradiocommands](https://github.com/Cruze03/cs2_blockradiocommands)**<br>
  ⭐ 15<br>
  ⏱️ updated 1 year ago<br>
  *A CSSharp plugin to block all radio commands.*

- **[schwarper/cs2-anticheat](https://github.com/schwarper/cs2-anticheat)**<br>
  ⭐ 14<br>
  ⏱️ updated 2 weeks ago<br>
  *cs2-anticheat is an anti-cheat system in development for CounterStrike 2.*

- **[Quantor97/CS2-Kill-Plugin](https://github.com/Quantor97/CS2-Kill-Plugin)**<br>
  ⭐ 14<br>
  ⏱️ updated 1 year ago<br>
  *A simple kill plugin that allows players to suicide via chat by entering '!suicide' or '/suicide'.*

- **[K4ryuu/K4-AlwaysWeaponSkins](https://github.com/K4ryuu/K4-AlwaysWeaponSkins)**<br>
  ⭐ 12<br>
  ⏱️ updated 1 month ago<br>
  *This plugin enhances weapon skin visibility by ensuring your equipped Steam inventory skins are displayed consistently across both teams.*

- **[Kandru/cs2-update-manager](https://github.com/Kandru/cs2-update-manager)**<br>
  ⭐ 12<br>
  ⏱️ updated 1 month ago<br>
  *The Plugin Update Manager is a plugin for Counter-Strike 2 designed to automatically update all your other plugins.*

- **[samyycX/CSSharpPatcher](https://github.com/samyycX/CSSharpPatcher)**<br>
  ⭐ 11<br>
  ⏱️ updated 1 month ago<br>
  *A plugin with various patches for cs2.*

- **[HvH-gg/RapidFireFix](https://github.com/HvH-gg/RapidFireFix)**<br>
  ⭐ 11<br>
  ⏱️ updated 11 months ago<br>
  *CounterStrikeSharp plugin to handle rapid fire in CS2.*

- **[asapverneri/CS2-Playervotes](https://github.com/asapverneri/CS2-Playervotes)**<br>
  ⭐ 11<br>
  ⏱️ updated 1 month ago<br>
  *Lightweight and efficient voting system for CS2 without anything pointless, allowing players to initiate votes for kicking, banning, and muting players.*

- **[B3none/cs2-instaplant](https://github.com/B3none/cs2-instaplant)**<br>
  ⭐ 11<br>
  ⏱️ updated 1 year ago<br>
  *Plant the bomb instantly as a terrorist.*

- **[KKNecmi/ThirdPerson-Revamped](https://github.com/KKNecmi/ThirdPerson-Revamped)**<br>
  ⭐ 11<br>
  ⏱️ updated 2 days ago<br>
  *A modern, improved third-person camera plugin for Counter-Strike 2.*

- **[zakriamansoor47/SLAYER_AntiCamp](https://github.com/zakriamansoor47/SLAYER_AntiCamp)**<br>
  ⭐ 9<br>
  ⏱️ updated 5 months ago<br>
  *This plugin detect player who is camping for a specific time.*

- **[T3Marius/T3Menu-API](https://github.com/T3Marius/T3Menu-API)**<br>
  ⭐ 9<br>
  ⏱️ updated 1 week ago<br>
  *T3Menu-API is a plugin created on counterstrikesharp with purpose of creating a better, refined menu controlled with player buttons.*

- **[T3Marius/MVP-Anthem](https://github.com/T3Marius/MVP-Anthem)**<br>
  ⭐ 9<br>
  ⏱️ updated 4 weeks ago<br>
  *A plugin that add custom mvp sound to the game.*

- **[Kandru/cs2-roll-the-dice](https://github.com/Kandru/cs2-roll-the-dice)**<br>
  ⭐ 9<br>
  ⏱️ updated 11 hours ago<br>
  *This plugin lets your players roll the dice each round (at any time during an round) to get either a positive or negative effect for the current round.*

- **[darkerz7/CS2-HideTeammates](https://github.com/darkerz7/CS2-HideTeammates)**<br>
  ⭐ 8<br>
  ⏱️ updated 1 month ago<br>
  *Hides Teammates on the entire map or distance.*

- **[Kandru/cs2-quake-sounds](https://github.com/Kandru/cs2-quake-sounds)**<br>
  ⭐ 8<br>
  ⏱️ updated 2 days ago<br>
  *This is a simple Quake Sound plugin for your server. It supports all types of sounds - only a workshop addon is necessesary.*

- **[Kandru/cs2-challenges](https://github.com/Kandru/cs2-challenges)**<br>
  ⭐ 8<br>
  ⏱️ updated 5 months ago<br>
  *This plugin allows you to create Challenges for players. Challenges are tasks that players need to complete within a certain time frame (e.g., daily, weekly, monthly).*

- **[Austinbots/CS2-BotAI](https://github.com/Austinbots/CS2-BotAI)**<br>
  ⭐ 8<br>
  ⏱️ updated 1 week ago<br>
  *Improves the built in bots AI.*

- **[zakriamansoor47/SLAYER_UnrestrictedFOV](https://github.com/zakriamansoor47/SLAYER_UnrestrictedFOV)**<br>
  ⭐ 7<br>
  ⏱️ updated 5 months ago<br>
  *This simple plugin allow players to change their FOV.*

- **[darkerz7/CS2-EntityFix](https://github.com/darkerz7/CS2-EntityFix)**<br>
  ⭐ 7<br>
  ⏱️ updated 1 month ago<br>
  *Fixes game_player_equip, game_ui, IgniteLifeTime, point_viewcontrol, trigger_gravity. Idea taken from cs2fixes.*

- **[Kandru/cs2-demo-recorder](https://github.com/Kandru/cs2-demo-recorder)**<br>
  ⭐ 6<br>
  ⏱️ updated 1 month ago<br>
  *This tool automatically start a recording whenever someone is on your server. It makes sure to stop the recording before the level is being changed.*

- **[Ferks-FK/CS2-TeamLimiter](https://github.com/Ferks-FK/CS2-TeamLimiter)**<br>
  ⭐ 6<br>
  ⏱️ updated 8 months ago<br>
  *This plugin allows you to set a maximum number of players in both teams. Useful for PUG/MIX or Retake mode servers.*

- **[zakriamansoor47/SLAYER_HeadshotOnly](https://github.com/zakriamansoor47/SLAYER_HeadshotOnly)**<br>
  ⭐ 5<br>
  ⏱️ updated 5 months ago<br>
  *This plugin enables headshot only to all players or enables headshot only on players themselves by using public command !hs.*

- **[zakriamansoor47/SLAYER_Noscope](https://github.com/zakriamansoor47/SLAYER_Noscope)**<br>
  ⭐ 5<br>
  ⏱️ updated 5 months ago<br>
  *This plugin disables scope of scope weapons like AWP, scout, etc.*

- **[asapverneri/CS2-Baninfo](https://github.com/asapverneri/CS2-Baninfo)**<br>
  ⭐ 5<br>
  ⏱️ updated 11 months ago<br>
  *Useful plugin that shows connected players ban & mute history in console.*

- **[asapverneri/CS2-ChatRelay](https://github.com/asapverneri/CS2-ChatRelay)**<br>
  ⭐ 5<br>
  ⏱️ updated 3 months ago<br>
  *Lightweight plugin to send your cs2 server chat messages to discord channel using webhook.*

- **[abnerfs/cs2-killfeed-filter](https://github.com/abnerfs/cs2-killfeed-filter)**<br>
  ⭐ 5<br>
  ⏱️ updated 1 year ago<br>
  *Show only your kills/assists/deaths in the killfeed, useful for DM servers where the killfeed has too much kills going on.*

- **[Letaryat/CS2-Poor-MapPropAds](https://github.com/Letaryat/CS2-Poor-MapPropAds)**<br>
  ⭐ 4<br>
  ⏱️ updated 3 weeks ago<br>
  *This plugin allows for server owners to create billboard type advertisements that are placed on wall.*

- **[Interesting-exe/QuickDefuse](https://github.com/Interesting-exe/QuickDefuse)**<br>
  ⭐ 4<br>
  ⏱️ updated 1 year ago<br>
  *Guess a wire for a chance to instantly defuse the bomb.*

- **[darkerz7/CSSharp-Fixes](https://github.com/darkerz7/CSSharp-Fixes)**<br>
  ⭐ 4<br>
  ⏱️ updated 3 days ago<br>
  *CS#Fixes is a CounterStrikeSharp plugin that fixes some bugs in Counter-Strike 2 and adds some commonly requested features.*

- **[asapverneri/CS2-BotQuotaManager](https://github.com/asapverneri/CS2-BotQuotaManager)**<br>
  ⭐ 4<br>
  ⏱️ updated 1 year ago<br>
  *This plugin handles bot_quota depending on playercount on the server.*

- **[R0mz1k/CSS-Knockback](https://github.com/R0mz1k/CSS-Knockback)**<br>
  ⭐ 4<br>
  ⏱️ updated 1 year ago<br>
  *This plugin, when hit, repels the recipient of the damage.*

- **[zakriamansoor47/SLAYER_Revive](https://github.com/zakriamansoor47/SLAYER_Revive)**<br>
  ⭐ 3<br>
  ⏱️ updated 6 days ago<br>
  *Revive teammates with 'E' (+use button).*

- **[TICHOJEBEC-SK/cs2-WeaponRestrict](https://github.com/TICHOJEBEC-SK/cs2-WeaponRestrict)**<br>
  ⭐ 3<br>
  ⏱️ updated 1 month ago<br>
  *A plugin that lets you restrict weapons by rules.*

- **[M-archand/CS2FlashingHtmlHudFix](https://github.com/M-archand/CS2FlashingHtmlHudFix)**<br>
  ⭐ 3<br>
  ⏱️ updated 10 months ago<br>
  *A CS2 CS# Plugin that uses a workaround found by Poggu to make .PrintToCenterHTML not flash every second by setting.*

- **[asapverneri/CS2-Gunsmenu](https://github.com/asapverneri/CS2-Gunsmenu)**<br>
  ⭐ 3<br>
  ⏱️ updated 1 month ago<br>
  *Up to date and lightweight gunmenu for CS2, allowing players to choose guns at any time of the round.*

- **[asapverneri/CS2-Legs](https://github.com/asapverneri/CS2-Legs)**<br>
  ⭐ 3<br>
  ⏱️ updated 1 year ago<br>
  *Simple plugin to disable lower body.*

- **[asapverneri/CS2-Clantags](https://github.com/asapverneri/CS2-Clantags)**<br>
  ⭐ 3<br>
  ⏱️ updated 2 months ago<br>
  *Extremely simple plugin to set admin/vip tag to scoreboard.*

- **[Austinbots/cs2-Change-Map-Rotation-Using-Text-File](https://github.com/Austinbots/cs2-Change-Map-Rotation-Using-Text-File)**<br>
  ⭐ 3<br>
  ⏱️ updated 3 weeks ago<br>
  *It allows you to change the map rotation using a text file.*

- **[asapverneri/CS2-ScoutzKnivez](https://github.com/asapverneri/CS2-ScoutzKnivez)**<br>
  ⭐ 2<br>
  ⏱️ updated 6 months ago<br>
  *This is a legendary gamemode made for CS2. It's in early state, but it should be pretty stable.*

- **[asapverneri/CS2-StaffList](https://github.com/asapverneri/CS2-StaffList)**<br>
  ⭐ 2<br>
  ⏱️ updated 1 year ago<br>
  *Simple plugin which show online admins in the server.*

- **[zakriamansoor47/SLAYER_1HitKill](https://github.com/zakriamansoor47/SLAYER_1HitKill)**<br>
  ⭐ 2<br>
  ⏱️ updated 5 months ago<br>
  *This simple plugin allows players to kill others in 1 Hit.*

- **[Dliix66/CS2-BotSlay](https://github.com/Dliix66/CS2-BotSlay)**<br>
  ⭐ 2<br>
  ⏱️ updated 1 year ago<br>
  *CSSharp plugin to slay all bots when the last player dies.*

- **[TICHOJEBEC-SK/cs2-WarnSystem](https://github.com/TICHOJEBEC-SK/cs2-WarnSystem)**<br>
  ⭐ 1<br>
  ⏱️ updated 2 weeks ago<br>
  *A plugin that allows admins to warn players.*

- **[schwarper/cs2-store](https://github.com/schwarper/cs2-store)**<br>
  ⭐ 1<br>
  ⏱️ updated 2 weeks ago<br>
  *A store plugin designed to enhance your gameplay by providing a dynamic credit system that allows players to purchase essential items directly from the store.*

- **[asapverneri/CS2-ChatLogs](https://github.com/asapverneri/CS2-ChatLogs)**<br>
  ⭐ 1<br>
  ⏱️ updated 3 months ago<br>
  *Plugin that store chat messages to MySQL database.*

- **[Austinbots/cs2-BotsNoKnife](https://github.com/Austinbots/cs2-BotsNoKnife)**<br>
  ⭐ 1<br>
  ⏱️ updated 3 weeks ago<br>
  *Strips knife from bots.*


## Swiftly Plugins

- **[swiftly-solution/admins](https://github.com/swiftly-solution/admins)**<br>
  ⭐ 4<br>
  ⏱️ updated 6 months ago<br>
  *A simple plugin for swiftly that implements an admin system (core).*

- **[swiftly-solution/vip_modules](https://github.com/swiftly-solution/vip_modules)**<br>
  ⭐ 4<br>
  ⏱️ updated 4 months ago<br>
  *A repository containing all the VIP Modules created by Swiftly Solution for VIP Core.*

- **[swiftly-solution/vip-core](https://github.com/swiftly-solution/vip-core)**<br>
  ⭐ 3<br>
  ⏱️ updated 4 months ago<br>
  *A simple plugin for swiftly that acts like a core for vip.*

- **[swiftly-solution/ranks](https://github.com/swiftly-solution/ranks)**<br>
  ⭐ 2<br>
  ⏱️ updated 7 months ago<br>
  *A simple plugin for Swiftly that implements an Rank System.*

- **[swiftly-solution/tags](https://github.com/swiftly-solution/tags)**<br>
  ⭐ 2<br>
  ⏱️ updated 6 months ago<br>
  *A simple plugin for Swiftly that implements tags on chat/scoreboard.*

- **[swiftly-solution/faceit-level](https://github.com/swiftly-solution/faceit-level)**<br>
  ⭐ 2<br>
  ⏱️ updated 9 months ago<br>
  *A simple plugin for Swiftly that queries the level faceit of a player and add the icon on the scoreboard.*

- **[swiftly-solution/admins_basebans](https://github.com/swiftly-solution/admins_basebans)**<br>
  ⭐ 1<br>
  ⏱️ updated 6 months ago<br>
  *A simple plugin for Swiftly that implements a ban system.*

- **[swiftly-solution/admins_commands](https://github.com/swiftly-solution/admins_commands)**<br>
  ⭐ 1<br>
  ⏱️ updated 8 months ago<br>
  *A simple plugin for Swiftly that implements some base commands.*

- **[swiftly-solution/connection-filters](https://github.com/swiftly-solution/connection-filters)**<br>
  ⭐ 1<br>
  ⏱️ updated 4 months ago<br>
  *A simple plugin for Swiftly that filters the connection based on some settings.*

- **[swiftly-solution/steam-requirements](https://github.com/swiftly-solution/steam-requirements)**<br>
  ⭐ 1<br>
  ⏱️ updated 8 months ago<br>
  *A simple plugin for Swiftly that decides if a player can connect based on some requirements.*

- **[swiftly-solution/advertisements](https://github.com/swiftly-solution/advertisements)**<br>
  ⭐ 1<br>
  ⏱️ updated 8 months ago<br>
  *A simple plugin for Swiftly that implements an chat advertising system.*

- **[swiftly-solution/multi1v1](https://github.com/swiftly-solution/multi1v1)**<br>
  ⭐ 1<br>
  ⏱️ updated 9 months ago<br>
  *A simple plugin for Swiftly that implements an Arena System.*

- **[swiftly-solution/countryflags](https://github.com/swiftly-solution/countryflags)**<br>
  ⭐ 1<br>
  ⏱️ updated 11 months ago<br>
  *A plugin for Swiftly which puts country flags on the scoreboard.*

- **[swiftly-solution/remove_default_messages](https://github.com/swiftly-solution/remove_default_messages)**<br>
  ⭐ 1<br>
  ⏱️ updated 1 year ago<br>
  *A plugin for Swiftly that removes the default game messages.*

- **[swiftly-solution/admins_basecomms](https://github.com/swiftly-solution/admins_basecomms)**<br>
  ⭐ 0<br>
  ⏱️ updated 4 months ago<br>
  *A simple plugin for Swiftly that implements a comms system.*

- **[swiftly-solution/map-chooser](https://github.com/swiftly-solution/map-chooser)**<br>
  ⭐ 0<br>
  ⏱️ updated 2 months ago<br>
  *A simple plugin for Swiftly that implements a basic map voting system.*

- **[swiftly-solution/mostactive](https://github.com/swiftly-solution/mostactive)**<br>
  ⭐ 0<br>
  ⏱️ updated 7 months ago<br>
  *A simple plugin for Swiftly that saves the connected time of a player on server in database.*

- **[swiftly-solution/random-team-logo](https://github.com/swiftly-solution/random-team-logo)**<br>
  ⭐ 0<br>
  ⏱️ updated 7 months ago<br>
  *A simple plugin for Swiftly which chooses a random team logo on each map start.*

- **[swiftly-solution/hud](https://github.com/swiftly-solution/hud)**<br>
  ⭐ 0<br>
  ⏱️ updated 3 months ago<br>
  *A simple plugin for Swiftly that implements a basic Hud System.*

- **[swiftly-solution/deathmatch](https://github.com/swiftly-solution/deathmatch)**<br>
  ⭐ 0<br>
  ⏱️ updated 7 months ago<br>
  *A simple plugin for swiftly that implements the basic functionality of a Deathmatch/FFA server.*

- **[swiftly-solution/player-model-changer](https://github.com/swiftly-solution/player-model-changer)**<br>
  ⭐ 0<br>
  ⏱️ updated 7 months ago<br>
  *A simple plugin for Swiftly that implements a basic player model changing system.*

- **[swiftly-solution/auto-team-balance](https://github.com/swiftly-solution/auto-team-balance)**<br>
  ⭐ 0<br>
  ⏱️ updated 7 months ago<br>
  *A simple plugin for Swiftly that balances the teams.*

- **[swiftly-solution/shop-core](https://github.com/swiftly-solution/shop-core)**<br>
  ⭐ 0<br>
  ⏱️ updated 7 months ago<br>
  *A simple plugin for Swiftly that implements the core of the shop.*

- **[swiftly-solution/shop-modules](https://github.com/swiftly-solution/shop-modules)**<br>
  ⭐ 0<br>
  ⏱️ updated 7 months ago<br>
  *A repository containing all the Shop Modules created by Swiftly Solution for Shop Core.*

- **[swiftly-solution/damage-management](https://github.com/swiftly-solution/damage-management)**<br>
  ⭐ 0<br>
  ⏱️ updated 7 months ago<br>
  *A simple plugin for swiftly that changes the damage management to faceit-style.*

- **[swiftly-solution/discord-logs](https://github.com/swiftly-solution/discord-logs)**<br>
  ⭐ 0<br>
  ⏱️ updated 8 months ago<br>
  *A simple plugin for Swiftly that integrates basic discord logs.*

- **[swiftly-solution/pm](https://github.com/swiftly-solution/pm)**<br>
  ⭐ 0<br>
  ⏱️ updated 1 year ago<br>
  *A Swiftly plugin that allows players to send private messages.*

- **[swiftly-solution/joinleave](https://github.com/swiftly-solution/joinleave)**<br>
  ⭐ 0<br>
  ⏱️ updated 1 year ago<br>
  *A plugin for Swiftly that prints a message when a player connects on/disconnects from the server.*

- **[swiftly-solution/antiteamflash](https://github.com/swiftly-solution/antiteamflash)**<br>
  ⭐ 0<br>
  ⏱️ updated 1 year ago<br>
  *A simple plugin for Swiftly that removes the possibility to get flashed from other teammates.*

- **[swiftly-solution/resetscore](https://github.com/swiftly-solution/resetscore)**<br>
  ⭐ 0<br>
  ⏱️ updated 1 year ago<br>
  *A plugin for Swiftly that sets the stats from the tab to 0 to the player that used the !rs/!resetscore command.*

- **[swiftly-solution/connect-sounds](https://github.com/swiftly-solution/connect-sounds)**<br>
  ⭐ 0<br>
  ⏱️ updated 8 months ago<br>
  *A simple plugin for Swiftly that plays a sound when a player connects.*

- **[swiftly-solution/goldmember](https://github.com/swiftly-solution/goldmember)**<br>
  ⭐ 0<br>
  ⏱️ updated 9 months ago<br>
  *A plugin for Swiftly that gives benefits to players who has your server DNS in their name.*

- **[swiftly-solution/advanced-weapons](https://github.com/swiftly-solution/advanced-weapons)**<br>
  ⭐ 0<br>
  ⏱️ updated 1 year ago<br>
  *A plugin for Swiftly that changes the properties of any weapon.*

- **[swiftly-solution/removebodies](https://github.com/swiftly-solution/removebodies)**<br>
  ⭐ 0<br>
  ⏱️ updated 1 year ago<br>
  *A plugin for Swiftly that removes the dead bodies from the ground.*

- **[swiftly-solution/welcomemessages](https://github.com/swiftly-solution/welcomemessages)**<br>
  ⭐ 0<br>
  ⏱️ updated 1 year ago<br>
  *A simple plugin for Swiftly that prints a message to a player when he has connected on the server.*


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
      <a href="https://github.com/8tnc"><img src="https://avatars.githubusercontent.com/u/78674116?v=4" width="64" height="64" alt="8tnc" /></a><br/>
      <a href="https://github.com/8tnc">@8tnc</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/abnerfs"><img src="https://avatars.githubusercontent.com/u/14078661?v=4" width="64" height="64" alt="abnerfs" /></a><br/>
      <a href="https://github.com/abnerfs">@abnerfs</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/actions-user"><img src="https://avatars.githubusercontent.com/u/65916846?v=4" width="64" height="64" alt="actions-user" /></a><br/>
      <a href="https://github.com/actions-user">@actions-user</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/akappakappa"><img src="https://avatars.githubusercontent.com/u/20224688?v=4" width="64" height="64" alt="akappakappa" /></a><br/>
      <a href="https://github.com/akappakappa">@akappakappa</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/akxcv"><img src="https://avatars.githubusercontent.com/u/17192674?v=4" width="64" height="64" alt="akxcv" /></a><br/>
      <a href="https://github.com/akxcv">@akxcv</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/algorithm-developer"><img src="https://avatars.githubusercontent.com/u/17625859?v=4" width="64" height="64" alt="algorithm-developer" /></a><br/>
      <a href="https://github.com/algorithm-developer">@algorithm-developer</a>
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
      <a href="https://github.com/amitelka"><img src="https://avatars.githubusercontent.com/u/12958411?v=4" width="64" height="64" alt="amitelka" /></a><br/>
      <a href="https://github.com/amitelka">@amitelka</a>
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
      <a href="https://github.com/AntPGN"><img src="https://avatars.githubusercontent.com/u/3760018?v=4" width="64" height="64" alt="AntPGN" /></a><br/>
      <a href="https://github.com/AntPGN">@AntPGN</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Apfelwurm"><img src="https://avatars.githubusercontent.com/u/23552885?v=4" width="64" height="64" alt="Apfelwurm" /></a><br/>
      <a href="https://github.com/Apfelwurm">@Apfelwurm</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/ar1a"><img src="https://avatars.githubusercontent.com/u/8436007?v=4" width="64" height="64" alt="ar1a" /></a><br/>
      <a href="https://github.com/ar1a">@ar1a</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/asapverneri"><img src="https://avatars.githubusercontent.com/u/142944488?v=4" width="64" height="64" alt="asapverneri" /></a><br/>
      <a href="https://github.com/asapverneri">@asapverneri</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/asensionacher"><img src="https://avatars.githubusercontent.com/u/7094577?v=4" width="64" height="64" alt="asensionacher" /></a><br/>
      <a href="https://github.com/asensionacher">@asensionacher</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/audiomaster99"><img src="https://avatars.githubusercontent.com/u/116572799?v=4" width="64" height="64" alt="audiomaster99" /></a><br/>
      <a href="https://github.com/audiomaster99">@audiomaster99</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Austinbots"><img src="https://avatars.githubusercontent.com/u/182579764?v=4" width="64" height="64" alt="Austinbots" /></a><br/>
      <a href="https://github.com/Austinbots">@Austinbots</a>
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
      <a href="https://github.com/BombFoolGranny"><img src="https://avatars.githubusercontent.com/u/32615723?v=4" width="64" height="64" alt="BombFoolGranny" /></a><br/>
      <a href="https://github.com/BombFoolGranny">@BombFoolGranny</a>
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
      <a href="https://github.com/busheezy"><img src="https://avatars.githubusercontent.com/u/6915170?v=4" width="64" height="64" alt="busheezy" /></a><br/>
      <a href="https://github.com/busheezy">@busheezy</a>
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
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/CharlesBarone"><img src="https://avatars.githubusercontent.com/u/16052438?v=4" width="64" height="64" alt="CharlesBarone" /></a><br/>
      <a href="https://github.com/CharlesBarone">@CharlesBarone</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Cherno-Beliy"><img src="https://avatars.githubusercontent.com/u/143458283?v=4" width="64" height="64" alt="Cherno-Beliy" /></a><br/>
      <a href="https://github.com/Cherno-Beliy">@Cherno-Beliy</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/counterstrikesharp-panel"><img src="https://avatars.githubusercontent.com/u/167018976?v=4" width="64" height="64" alt="counterstrikesharp-panel" /></a><br/>
      <a href="https://github.com/counterstrikesharp-panel">@counterstrikesharp-panel</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/crashzk"><img src="https://avatars.githubusercontent.com/u/32937653?v=4" width="64" height="64" alt="crashzk" /></a><br/>
      <a href="https://github.com/crashzk">@crashzk</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/criskkky"><img src="https://avatars.githubusercontent.com/u/36176343?v=4" width="64" height="64" alt="criskkky" /></a><br/>
      <a href="https://github.com/criskkky">@criskkky</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Cruze03"><img src="https://avatars.githubusercontent.com/u/31343375?v=4" width="64" height="64" alt="Cruze03" /></a><br/>
      <a href="https://github.com/Cruze03">@Cruze03</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/daffyyyy"><img src="https://avatars.githubusercontent.com/u/41084667?v=4" width="64" height="64" alt="daffyyyy" /></a><br/>
      <a href="https://github.com/daffyyyy">@daffyyyy</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/darichey"><img src="https://avatars.githubusercontent.com/u/3052455?v=4" width="64" height="64" alt="darichey" /></a><br/>
      <a href="https://github.com/darichey">@darichey</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/darkerz7"><img src="https://avatars.githubusercontent.com/u/25752428?v=4" width="64" height="64" alt="darkerz7" /></a><br/>
      <a href="https://github.com/darkerz7">@darkerz7</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/DeadSwimek"><img src="https://avatars.githubusercontent.com/u/66752697?v=4" width="64" height="64" alt="DeadSwimek" /></a><br/>
      <a href="https://github.com/DeadSwimek">@DeadSwimek</a>
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
      <a href="https://github.com/derkalle4"><img src="https://avatars.githubusercontent.com/u/15657782?v=4" width="64" height="64" alt="derkalle4" /></a><br/>
      <a href="https://github.com/derkalle4">@derkalle4</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/devayee"><img src="https://avatars.githubusercontent.com/u/93475779?v=4" width="64" height="64" alt="devayee" /></a><br/>
      <a href="https://github.com/devayee">@devayee</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/DizzyThermal"><img src="https://avatars.githubusercontent.com/u/730767?v=4" width="64" height="64" alt="DizzyThermal" /></a><br/>
      <a href="https://github.com/DizzyThermal">@DizzyThermal</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Dliix66"><img src="https://avatars.githubusercontent.com/u/2865871?v=4" width="64" height="64" alt="Dliix66" /></a><br/>
      <a href="https://github.com/Dliix66">@Dliix66</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/dollannn"><img src="https://avatars.githubusercontent.com/u/50216897?v=4" width="64" height="64" alt="dollannn" /></a><br/>
      <a href="https://github.com/dollannn">@dollannn</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/dom1torii"><img src="https://avatars.githubusercontent.com/u/84600518?v=4" width="64" height="64" alt="dom1torii" /></a><br/>
      <a href="https://github.com/dom1torii">@dom1torii</a>
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
      <a href="https://github.com/emilhaapalainen"><img src="https://avatars.githubusercontent.com/u/47125778?v=4" width="64" height="64" alt="emilhaapalainen" /></a><br/>
      <a href="https://github.com/emilhaapalainen">@emilhaapalainen</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/eSTuuu"><img src="https://avatars.githubusercontent.com/u/58341152?v=4" width="64" height="64" alt="eSTuuu" /></a><br/>
      <a href="https://github.com/eSTuuu">@eSTuuu</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/exababy"><img src="https://avatars.githubusercontent.com/u/44870116?v=4" width="64" height="64" alt="exababy" /></a><br/>
      <a href="https://github.com/exababy">@exababy</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/exd02"><img src="https://avatars.githubusercontent.com/u/62575526?v=4" width="64" height="64" alt="exd02" /></a><br/>
      <a href="https://github.com/exd02">@exd02</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/execut1ve"><img src="https://avatars.githubusercontent.com/u/37169808?v=4" width="64" height="64" alt="execut1ve" /></a><br/>
      <a href="https://github.com/execut1ve">@execut1ve</a>
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
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Faramour"><img src="https://avatars.githubusercontent.com/u/44729057?v=4" width="64" height="64" alt="Faramour" /></a><br/>
      <a href="https://github.com/Faramour">@Faramour</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Ferks-FK"><img src="https://avatars.githubusercontent.com/u/69549678?v=4" width="64" height="64" alt="Ferks-FK" /></a><br/>
      <a href="https://github.com/Ferks-FK">@Ferks-FK</a>
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
      <a href="https://github.com/GameChaos"><img src="https://avatars.githubusercontent.com/u/25118806?v=4" width="64" height="64" alt="GameChaos" /></a><br/>
      <a href="https://github.com/GameChaos">@GameChaos</a>
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
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/GekasD"><img src="https://avatars.githubusercontent.com/u/67982775?v=4" width="64" height="64" alt="GekasD" /></a><br/>
      <a href="https://github.com/GekasD">@GekasD</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/girlglock"><img src="https://avatars.githubusercontent.com/u/178796756?v=4" width="64" height="64" alt="girlglock" /></a><br/>
      <a href="https://github.com/girlglock">@girlglock</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/apps/github-actions"><img src="https://avatars.githubusercontent.com/in/15368?v=4" width="64" height="64" alt="github-actions[bot]" /></a><br/>
      <a href="https://github.com/apps/github-actions">@github-actions[bot]</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Gorakel"><img src="https://avatars.githubusercontent.com/u/29128011?v=4" width="64" height="64" alt="Gorakel" /></a><br/>
      <a href="https://github.com/Gorakel">@Gorakel</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/grrhn"><img src="https://avatars.githubusercontent.com/u/105857708?v=4" width="64" height="64" alt="grrhn" /></a><br/>
      <a href="https://github.com/grrhn">@grrhn</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/HerrMagiic"><img src="https://avatars.githubusercontent.com/u/70164539?v=4" width="64" height="64" alt="HerrMagiic" /></a><br/>
      <a href="https://github.com/HerrMagiic">@HerrMagiic</a>
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
      <a href="https://github.com/hlyl"><img src="https://avatars.githubusercontent.com/u/1834987?v=4" width="64" height="64" alt="hlyl" /></a><br/>
      <a href="https://github.com/hlyl">@hlyl</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/hobsRKM"><img src="https://avatars.githubusercontent.com/u/11420858?v=4" width="64" height="64" alt="hobsRKM" /></a><br/>
      <a href="https://github.com/hobsRKM">@hobsRKM</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/HvH-gg"><img src="https://avatars.githubusercontent.com/u/112752845?v=4" width="64" height="64" alt="HvH-gg" /></a><br/>
      <a href="https://github.com/HvH-gg">@HvH-gg</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/hzqst"><img src="https://avatars.githubusercontent.com/u/12287588?v=4" width="64" height="64" alt="hzqst" /></a><br/>
      <a href="https://github.com/hzqst">@hzqst</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/idk1703"><img src="https://avatars.githubusercontent.com/u/64554241?v=4" width="64" height="64" alt="idk1703" /></a><br/>
      <a href="https://github.com/idk1703">@idk1703</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Iksix"><img src="https://avatars.githubusercontent.com/u/109164274?v=4" width="64" height="64" alt="Iksix" /></a><br/>
      <a href="https://github.com/Iksix">@Iksix</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/ilyhalight"><img src="https://avatars.githubusercontent.com/u/62353659?v=4" width="64" height="64" alt="ilyhalight" /></a><br/>
      <a href="https://github.com/ilyhalight">@ilyhalight</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/im6705"><img src="https://avatars.githubusercontent.com/u/10539689?v=4" width="64" height="64" alt="im6705" /></a><br/>
      <a href="https://github.com/im6705">@im6705</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/imi-tat0r"><img src="https://avatars.githubusercontent.com/u/17706178?v=4" width="64" height="64" alt="imi-tat0r" /></a><br/>
      <a href="https://github.com/imi-tat0r">@imi-tat0r</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Interesting-exe"><img src="https://avatars.githubusercontent.com/u/52731127?v=4" width="64" height="64" alt="Interesting-exe" /></a><br/>
      <a href="https://github.com/Interesting-exe">@Interesting-exe</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/invoker420"><img src="https://avatars.githubusercontent.com/u/187507316?v=4" width="64" height="64" alt="invoker420" /></a><br/>
      <a href="https://github.com/invoker420">@invoker420</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/ipsvn"><img src="https://avatars.githubusercontent.com/u/80017804?v=4" width="64" height="64" alt="ipsvn" /></a><br/>
      <a href="https://github.com/ipsvn">@ipsvn</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Iwhite67"><img src="https://avatars.githubusercontent.com/u/9698964?v=4" width="64" height="64" alt="Iwhite67" /></a><br/>
      <a href="https://github.com/Iwhite67">@Iwhite67</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/iwyo"><img src="https://avatars.githubusercontent.com/u/48887967?v=4" width="64" height="64" alt="iwyo" /></a><br/>
      <a href="https://github.com/iwyo">@iwyo</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/JackJack3231"><img src="https://avatars.githubusercontent.com/u/26525530?v=4" width="64" height="64" alt="JackJack3231" /></a><br/>
      <a href="https://github.com/JackJack3231">@JackJack3231</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/jakkekz"><img src="https://avatars.githubusercontent.com/u/120755650?v=4" width="64" height="64" alt="jakkekz" /></a><br/>
      <a href="https://github.com/jakkekz">@jakkekz</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/JeBenzon"><img src="https://avatars.githubusercontent.com/u/15323233?v=4" width="64" height="64" alt="JeBenzon" /></a><br/>
      <a href="https://github.com/JeBenzon">@JeBenzon</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/jmgraeffe"><img src="https://avatars.githubusercontent.com/u/1965594?v=4" width="64" height="64" alt="jmgraeffe" /></a><br/>
      <a href="https://github.com/jmgraeffe">@jmgraeffe</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/jonassjoh"><img src="https://avatars.githubusercontent.com/u/17067347?v=4" width="64" height="64" alt="jonassjoh" /></a><br/>
      <a href="https://github.com/jonassjoh">@jonassjoh</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Julienhqr"><img src="https://avatars.githubusercontent.com/u/43007197?v=4" width="64" height="64" alt="Julienhqr" /></a><br/>
      <a href="https://github.com/Julienhqr">@Julienhqr</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/jvnipers"><img src="https://avatars.githubusercontent.com/u/96595352?v=4" width="64" height="64" alt="jvnipers" /></a><br/>
      <a href="https://github.com/jvnipers">@jvnipers</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/jwsharpe"><img src="https://avatars.githubusercontent.com/u/23224124?v=4" width="64" height="64" alt="jwsharpe" /></a><br/>
      <a href="https://github.com/jwsharpe">@jwsharpe</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/K4ryuu"><img src="https://avatars.githubusercontent.com/u/104531589?v=4" width="64" height="64" alt="K4ryuu" /></a><br/>
      <a href="https://github.com/K4ryuu">@K4ryuu</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Kandru"><img src="https://avatars.githubusercontent.com/u/1965552?v=4" width="64" height="64" alt="Kandru" /></a><br/>
      <a href="https://github.com/Kandru">@Kandru</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Katarina-E"><img src="https://avatars.githubusercontent.com/u/153746513?v=4" width="64" height="64" alt="Katarina-E" /></a><br/>
      <a href="https://github.com/Katarina-E">@Katarina-E</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/KillerRoi"><img src="https://avatars.githubusercontent.com/u/54289708?v=4" width="64" height="64" alt="KillerRoi" /></a><br/>
      <a href="https://github.com/KillerRoi">@KillerRoi</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/KillStr3aK"><img src="https://avatars.githubusercontent.com/u/19509520?v=4" width="64" height="64" alt="KillStr3aK" /></a><br/>
      <a href="https://github.com/KillStr3aK">@KillStr3aK</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/KKNecmi"><img src="https://avatars.githubusercontent.com/u/174268271?v=4" width="64" height="64" alt="KKNecmi" /></a><br/>
      <a href="https://github.com/KKNecmi">@KKNecmi</a>
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
      <a href="https://github.com/kralgorkem"><img src="https://avatars.githubusercontent.com/u/61798602?v=4" width="64" height="64" alt="kralgorkem" /></a><br/>
      <a href="https://github.com/kralgorkem">@kralgorkem</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Kroytz"><img src="https://avatars.githubusercontent.com/u/33564475?v=4" width="64" height="64" alt="Kroytz" /></a><br/>
      <a href="https://github.com/Kroytz">@Kroytz</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/kus"><img src="https://avatars.githubusercontent.com/u/571523?v=4" width="64" height="64" alt="kus" /></a><br/>
      <a href="https://github.com/kus">@kus</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Kxnrl"><img src="https://avatars.githubusercontent.com/u/3905845?v=4" width="64" height="64" alt="Kxnrl" /></a><br/>
      <a href="https://github.com/Kxnrl">@Kxnrl</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/KZGlobalTeam"><img src="https://avatars.githubusercontent.com/u/71567872?v=4" width="64" height="64" alt="KZGlobalTeam" /></a><br/>
      <a href="https://github.com/KZGlobalTeam">@KZGlobalTeam</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/laazzee"><img src="https://avatars.githubusercontent.com/u/19431478?v=4" width="64" height="64" alt="laazzee" /></a><br/>
      <a href="https://github.com/laazzee">@laazzee</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Lan2Play"><img src="https://avatars.githubusercontent.com/u/73311398?v=4" width="64" height="64" alt="Lan2Play" /></a><br/>
      <a href="https://github.com/Lan2Play">@Lan2Play</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/lanslide-team"><img src="https://avatars.githubusercontent.com/u/122711296?v=4" width="64" height="64" alt="lanslide-team" /></a><br/>
      <a href="https://github.com/lanslide-team">@lanslide-team</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/LaplaceTor"><img src="https://avatars.githubusercontent.com/u/28674126?v=4" width="64" height="64" alt="LaplaceTor" /></a><br/>
      <a href="https://github.com/LaplaceTor">@LaplaceTor</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Letaryat"><img src="https://avatars.githubusercontent.com/u/69041891?v=4" width="64" height="64" alt="Letaryat" /></a><br/>
      <a href="https://github.com/Letaryat">@Letaryat</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/M-archand"><img src="https://avatars.githubusercontent.com/u/13469995?v=4" width="64" height="64" alt="M-archand" /></a><br/>
      <a href="https://github.com/M-archand">@M-archand</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/m-arcuri"><img src="https://avatars.githubusercontent.com/u/124469923?v=4" width="64" height="64" alt="m-arcuri" /></a><br/>
      <a href="https://github.com/m-arcuri">@m-arcuri</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/m3ntorsky"><img src="https://avatars.githubusercontent.com/u/98771679?v=4" width="64" height="64" alt="m3ntorsky" /></a><br/>
      <a href="https://github.com/m3ntorsky">@m3ntorsky</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/mAa4a97"><img src="https://avatars.githubusercontent.com/u/34139457?v=4" width="64" height="64" alt="mAa4a97" /></a><br/>
      <a href="https://github.com/mAa4a97">@mAa4a97</a>
    </td>
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
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/MD-V"><img src="https://avatars.githubusercontent.com/u/436613?v=4" width="64" height="64" alt="MD-V" /></a><br/>
      <a href="https://github.com/MD-V">@MD-V</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/MerakW"><img src="https://avatars.githubusercontent.com/u/34398344?v=4" width="64" height="64" alt="MerakW" /></a><br/>
      <a href="https://github.com/MerakW">@MerakW</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Mesharsky"><img src="https://avatars.githubusercontent.com/u/30102036?v=4" width="64" height="64" alt="Mesharsky" /></a><br/>
      <a href="https://github.com/Mesharsky">@Mesharsky</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/michihupf"><img src="https://avatars.githubusercontent.com/u/26794144?v=4" width="64" height="64" alt="michihupf" /></a><br/>
      <a href="https://github.com/michihupf">@michihupf</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/mihaigsm2003"><img src="https://avatars.githubusercontent.com/u/51678688?v=4" width="64" height="64" alt="mihaigsm2003" /></a><br/>
      <a href="https://github.com/mihaigsm2003">@mihaigsm2003</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/milkywayfarer"><img src="https://avatars.githubusercontent.com/u/17110335?v=4" width="64" height="64" alt="milkywayfarer" /></a><br/>
      <a href="https://github.com/milkywayfarer">@milkywayfarer</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/moongetsu"><img src="https://avatars.githubusercontent.com/u/111883135?v=4" width="64" height="64" alt="moongetsu" /></a><br/>
      <a href="https://github.com/moongetsu">@moongetsu</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/moyogii"><img src="https://avatars.githubusercontent.com/u/22126651?v=4" width="64" height="64" alt="moyogii" /></a><br/>
      <a href="https://github.com/moyogii">@moyogii</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/mrc4tt"><img src="https://avatars.githubusercontent.com/u/5301047?v=4" width="64" height="64" alt="mrc4tt" /></a><br/>
      <a href="https://github.com/mrc4tt">@mrc4tt</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/MSWS"><img src="https://avatars.githubusercontent.com/u/14448584?v=4" width="64" height="64" alt="MSWS" /></a><br/>
      <a href="https://github.com/MSWS">@MSWS</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/NaathySz"><img src="https://avatars.githubusercontent.com/u/97997774?v=4" width="64" height="64" alt="NaathySz" /></a><br/>
      <a href="https://github.com/NaathySz">@NaathySz</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Nereziel"><img src="https://avatars.githubusercontent.com/u/8618825?v=4" width="64" height="64" alt="Nereziel" /></a><br/>
      <a href="https://github.com/Nereziel">@Nereziel</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/nicedayzhu"><img src="https://avatars.githubusercontent.com/u/5286862?v=4" width="64" height="64" alt="nicedayzhu" /></a><br/>
      <a href="https://github.com/nicedayzhu">@nicedayzhu</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/NiGHT757"><img src="https://avatars.githubusercontent.com/u/86895149?v=4" width="64" height="64" alt="NiGHT757" /></a><br/>
      <a href="https://github.com/NiGHT757">@NiGHT757</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/NikolaJyun"><img src="https://avatars.githubusercontent.com/u/22559124?v=4" width="64" height="64" alt="NikolaJyun" /></a><br/>
      <a href="https://github.com/NikolaJyun">@NikolaJyun</a>
    </td>
  </tr>
  <tr>
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
    <td align="center" valign="top" width="80">
      <a href="https://github.com/nry1337"><img src="https://avatars.githubusercontent.com/u/40671068?v=4" width="64" height="64" alt="nry1337" /></a><br/>
      <a href="https://github.com/nry1337">@nry1337</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Nubston"><img src="https://avatars.githubusercontent.com/u/15358552?v=4" width="64" height="64" alt="Nubston" /></a><br/>
      <a href="https://github.com/Nubston">@Nubston</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/nuclearsilo583"><img src="https://avatars.githubusercontent.com/u/58926275?v=4" width="64" height="64" alt="nuclearsilo583" /></a><br/>
      <a href="https://github.com/nuclearsilo583">@nuclearsilo583</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/NullVerdict"><img src="https://avatars.githubusercontent.com/u/24498484?v=4" width="64" height="64" alt="NullVerdict" /></a><br/>
      <a href="https://github.com/NullVerdict">@NullVerdict</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/NYSHUN"><img src="https://avatars.githubusercontent.com/u/175985294?v=4" width="64" height="64" alt="NYSHUN" /></a><br/>
      <a href="https://github.com/NYSHUN">@NYSHUN</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/o3LL"><img src="https://avatars.githubusercontent.com/u/16344976?v=4" width="64" height="64" alt="o3LL" /></a><br/>
      <a href="https://github.com/o3LL">@o3LL</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/OniquirAK"><img src="https://avatars.githubusercontent.com/u/84151839?v=4" width="64" height="64" alt="OniquirAK" /></a><br/>
      <a href="https://github.com/OniquirAK">@OniquirAK</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/oqyh"><img src="https://avatars.githubusercontent.com/u/48490385?v=4" width="64" height="64" alt="oqyh" /></a><br/>
      <a href="https://github.com/oqyh">@oqyh</a>
    </td>
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
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/pandathebeasty"><img src="https://avatars.githubusercontent.com/u/64710238?v=4" width="64" height="64" alt="pandathebeasty" /></a><br/>
      <a href="https://github.com/pandathebeasty">@pandathebeasty</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/panikajo"><img src="https://avatars.githubusercontent.com/u/4964185?v=4" width="64" height="64" alt="panikajo" /></a><br/>
      <a href="https://github.com/panikajo">@panikajo</a>
    </td>
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
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/phara1"><img src="https://avatars.githubusercontent.com/u/129111509?v=4" width="64" height="64" alt="phara1" /></a><br/>
      <a href="https://github.com/phara1">@phara1</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Poggicek"><img src="https://avatars.githubusercontent.com/u/45881722?v=4" width="64" height="64" alt="Poggicek" /></a><br/>
      <a href="https://github.com/Poggicek">@Poggicek</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/poggicek"><img src="https://github.com/poggicek.png" width="64" height="64" alt="poggicek" /></a><br/>
      <a href="https://github.com/poggicek">@poggicek</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Prefix"><img src="https://avatars.githubusercontent.com/u/1775218?v=4" width="64" height="64" alt="Prefix" /></a><br/>
      <a href="https://github.com/Prefix">@Prefix</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/qq410525209"><img src="https://avatars.githubusercontent.com/u/47157419?v=4" width="64" height="64" alt="qq410525209" /></a><br/>
      <a href="https://github.com/qq410525209">@qq410525209</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/qstage"><img src="https://avatars.githubusercontent.com/u/166386817?v=4" width="64" height="64" alt="qstage" /></a><br/>
      <a href="https://github.com/qstage">@qstage</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Quantor97"><img src="https://avatars.githubusercontent.com/u/45876155?v=4" width="64" height="64" alt="Quantor97" /></a><br/>
      <a href="https://github.com/Quantor97">@Quantor97</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/R0mz1k"><img src="https://avatars.githubusercontent.com/u/81678188?v=4" width="64" height="64" alt="R0mz1k" /></a><br/>
      <a href="https://github.com/R0mz1k">@R0mz1k</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/rainstorm-9"><img src="https://avatars.githubusercontent.com/u/181768486?v=4" width="64" height="64" alt="rainstorm-9" /></a><br/>
      <a href="https://github.com/rainstorm-9">@rainstorm-9</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Ravid-A"><img src="https://avatars.githubusercontent.com/u/72127473?v=4" width="64" height="64" alt="Ravid-A" /></a><br/>
      <a href="https://github.com/Ravid-A">@Ravid-A</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/razpbrry"><img src="https://avatars.githubusercontent.com/u/9876747?v=4" width="64" height="64" alt="razpbrry" /></a><br/>
      <a href="https://github.com/razpbrry">@razpbrry</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/rcnoob"><img src="https://avatars.githubusercontent.com/u/139053812?v=4" width="64" height="64" alt="rcnoob" /></a><br/>
      <a href="https://github.com/rcnoob">@rcnoob</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/rcon420"><img src="https://avatars.githubusercontent.com/u/47292145?v=4" width="64" height="64" alt="rcon420" /></a><br/>
      <a href="https://github.com/rcon420">@rcon420</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/rdfortega"><img src="https://avatars.githubusercontent.com/u/19917918?v=4" width="64" height="64" alt="rdfortega" /></a><br/>
      <a href="https://github.com/rdfortega">@rdfortega</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/ReneRebsdorf"><img src="https://avatars.githubusercontent.com/u/44376705?v=4" width="64" height="64" alt="ReneRebsdorf" /></a><br/>
      <a href="https://github.com/ReneRebsdorf">@ReneRebsdorf</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Riicesp"><img src="https://avatars.githubusercontent.com/u/171302297?v=4" width="64" height="64" alt="Riicesp" /></a><br/>
      <a href="https://github.com/Riicesp">@Riicesp</a>
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
      <a href="https://github.com/Salvatore-Als"><img src="https://avatars.githubusercontent.com/u/58212852?v=4" width="64" height="64" alt="Salvatore-Als" /></a><br/>
      <a href="https://github.com/Salvatore-Als">@Salvatore-Als</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/samyycX"><img src="https://avatars.githubusercontent.com/u/60744529?v=4" width="64" height="64" alt="samyycX" /></a><br/>
      <a href="https://github.com/samyycX">@samyycX</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/sapsanDev"><img src="https://avatars.githubusercontent.com/u/42625140?v=4" width="64" height="64" alt="sapsanDev" /></a><br/>
      <a href="https://github.com/sapsanDev">@sapsanDev</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/sarim-hk"><img src="https://avatars.githubusercontent.com/u/58489447?v=4" width="64" height="64" alt="sarim-hk" /></a><br/>
      <a href="https://github.com/sarim-hk">@sarim-hk</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Satttoshi"><img src="https://avatars.githubusercontent.com/u/109807794?v=4" width="64" height="64" alt="Satttoshi" /></a><br/>
      <a href="https://github.com/Satttoshi">@Satttoshi</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/ScchutzZ"><img src="https://avatars.githubusercontent.com/u/10107035?v=4" width="64" height="64" alt="ScchutzZ" /></a><br/>
      <a href="https://github.com/ScchutzZ">@ScchutzZ</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/schwarper"><img src="https://avatars.githubusercontent.com/u/75811921?v=4" width="64" height="64" alt="schwarper" /></a><br/>
      <a href="https://github.com/schwarper">@schwarper</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/shobhit-pathak"><img src="https://avatars.githubusercontent.com/u/140690706?v=4" width="64" height="64" alt="shobhit-pathak" /></a><br/>
      <a href="https://github.com/shobhit-pathak">@shobhit-pathak</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/sirNugg3ts"><img src="https://avatars.githubusercontent.com/u/28486181?v=4" width="64" height="64" alt="sirNugg3ts" /></a><br/>
      <a href="https://github.com/sirNugg3ts">@sirNugg3ts</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/skayee"><img src="https://avatars.githubusercontent.com/u/75901057?v=4" width="64" height="64" alt="skayee" /></a><br/>
      <a href="https://github.com/skayee">@skayee</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/skuzzis"><img src="https://avatars.githubusercontent.com/u/61626661?v=4" width="64" height="64" alt="skuzzis" /></a><br/>
      <a href="https://github.com/skuzzis">@skuzzis</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/sn0wmankr"><img src="https://avatars.githubusercontent.com/u/24391844?v=4" width="64" height="64" alt="sn0wmankr" /></a><br/>
      <a href="https://github.com/sn0wmankr">@sn0wmankr</a>
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
      <a href="https://github.com/ssypchenko"><img src="https://avatars.githubusercontent.com/u/30598453?v=4" width="64" height="64" alt="ssypchenko" /></a><br/>
      <a href="https://github.com/ssypchenko">@ssypchenko</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/st1ng2"><img src="https://avatars.githubusercontent.com/u/41505081?v=4" width="64" height="64" alt="st1ng2" /></a><br/>
      <a href="https://github.com/st1ng2">@st1ng2</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/stefanx111"><img src="https://avatars.githubusercontent.com/u/60297289?v=4" width="64" height="64" alt="stefanx111" /></a><br/>
      <a href="https://github.com/stefanx111">@stefanx111</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Stimayk"><img src="https://avatars.githubusercontent.com/u/51941742?v=4" width="64" height="64" alt="Stimayk" /></a><br/>
      <a href="https://github.com/Stimayk">@Stimayk</a>
    </td>
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
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/T3Marius"><img src="https://avatars.githubusercontent.com/u/168598779?v=4" width="64" height="64" alt="T3Marius" /></a><br/>
      <a href="https://github.com/T3Marius">@T3Marius</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/T3Marius-hub"><img src="https://avatars.githubusercontent.com/u/173165797?v=4" width="64" height="64" alt="T3Marius-hub" /></a><br/>
      <a href="https://github.com/T3Marius-hub">@T3Marius-hub</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/tatuaua"><img src="https://avatars.githubusercontent.com/u/116430797?v=4" width="64" height="64" alt="tatuaua" /></a><br/>
      <a href="https://github.com/tatuaua">@tatuaua</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/The0mikkel"><img src="https://avatars.githubusercontent.com/u/28625667?v=4" width="64" height="64" alt="The0mikkel" /></a><br/>
      <a href="https://github.com/The0mikkel">@The0mikkel</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/thechrisnixon"><img src="https://avatars.githubusercontent.com/u/672057?v=4" width="64" height="64" alt="thechrisnixon" /></a><br/>
      <a href="https://github.com/thechrisnixon">@thechrisnixon</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/TheR00st3r"><img src="https://avatars.githubusercontent.com/u/1764864?v=4" width="64" height="64" alt="TheR00st3r" /></a><br/>
      <a href="https://github.com/TheR00st3r">@TheR00st3r</a>
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
    <td align="center" valign="top" width="80">
      <a href="https://github.com/tiltysola"><img src="https://avatars.githubusercontent.com/u/19757919?v=4" width="64" height="64" alt="tiltysola" /></a><br/>
      <a href="https://github.com/tiltysola">@tiltysola</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Tsukasa-Nefren"><img src="https://avatars.githubusercontent.com/u/89155368?v=4" width="64" height="64" alt="Tsukasa-Nefren" /></a><br/>
      <a href="https://github.com/Tsukasa-Nefren">@Tsukasa-Nefren</a>
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
      <a href="https://github.com/ValMadBox"><img src="https://avatars.githubusercontent.com/u/195292199?v=4" width="64" height="64" alt="ValMadBox" /></a><br/>
      <a href="https://github.com/ValMadBox">@ValMadBox</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Vauff"><img src="https://avatars.githubusercontent.com/u/6075172?v=4" width="64" height="64" alt="Vauff" /></a><br/>
      <a href="https://github.com/Vauff">@Vauff</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/vulikit"><img src="https://avatars.githubusercontent.com/u/155004361?v=4" width="64" height="64" alt="vulikit" /></a><br/>
      <a href="https://github.com/vulikit">@vulikit</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/weblate"><img src="https://avatars.githubusercontent.com/u/1607653?v=4" width="64" height="64" alt="weblate" /></a><br/>
      <a href="https://github.com/weblate">@weblate</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/webpashtet"><img src="https://avatars.githubusercontent.com/u/44953225?v=4" width="64" height="64" alt="webpashtet" /></a><br/>
      <a href="https://github.com/webpashtet">@webpashtet</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Wend4r"><img src="https://avatars.githubusercontent.com/u/47463683?v=4" width="64" height="64" alt="Wend4r" /></a><br/>
      <a href="https://github.com/Wend4r">@Wend4r</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/wiruwiru"><img src="https://avatars.githubusercontent.com/u/61034981?v=4" width="64" height="64" alt="wiruwiru" /></a><br/>
      <a href="https://github.com/wiruwiru">@wiruwiru</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/wjsrnrgus33"><img src="https://avatars.githubusercontent.com/u/112553297?v=4" width="64" height="64" alt="wjsrnrgus33" /></a><br/>
      <a href="https://github.com/wjsrnrgus33">@wjsrnrgus33</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Wngui"><img src="https://avatars.githubusercontent.com/u/12588316?v=4" width="64" height="64" alt="Wngui" /></a><br/>
      <a href="https://github.com/Wngui">@Wngui</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/xen-000"><img src="https://avatars.githubusercontent.com/u/24222257?v=4" width="64" height="64" alt="xen-000" /></a><br/>
      <a href="https://github.com/xen-000">@xen-000</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/xLeviNx"><img src="https://avatars.githubusercontent.com/u/48465241?v=4" width="64" height="64" alt="xLeviNx" /></a><br/>
      <a href="https://github.com/xLeviNx">@xLeviNx</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/y0ungsm"><img src="https://avatars.githubusercontent.com/u/84058740?v=4" width="64" height="64" alt="y0ungsm" /></a><br/>
      <a href="https://github.com/y0ungsm">@y0ungsm</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Yarukon"><img src="https://avatars.githubusercontent.com/u/61296195?v=4" width="64" height="64" alt="Yarukon" /></a><br/>
      <a href="https://github.com/Yarukon">@Yarukon</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Yeagorn"><img src="https://avatars.githubusercontent.com/u/37038659?v=4" width="64" height="64" alt="Yeagorn" /></a><br/>
      <a href="https://github.com/Yeagorn">@Yeagorn</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/yonilerner"><img src="https://avatars.githubusercontent.com/u/278810?v=4" width="64" height="64" alt="yonilerner" /></a><br/>
      <a href="https://github.com/yonilerner">@yonilerner</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/zakriamansoor47"><img src="https://avatars.githubusercontent.com/u/56433510?v=4" width="64" height="64" alt="zakriamansoor47" /></a><br/>
      <a href="https://github.com/zakriamansoor47">@zakriamansoor47</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/Zeisenx"><img src="https://avatars.githubusercontent.com/u/19303143?v=4" width="64" height="64" alt="Zeisenx" /></a><br/>
      <a href="https://github.com/Zeisenx">@Zeisenx</a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/zer0k-z"><img src="https://avatars.githubusercontent.com/u/61156310?v=4" width="64" height="64" alt="zer0k-z" /></a><br/>
      <a href="https://github.com/zer0k-z">@zer0k-z</a>
    </td>
    <td align="center" valign="top" width="80">
      <a href="https://github.com/zwolof"><img src="https://avatars.githubusercontent.com/u/21288834?v=4" width="64" height="64" alt="zwolof" /></a><br/>
      <a href="https://github.com/zwolof">@zwolof</a>
    </td>
  </tr>
</table>


# Contributing

## How to add plugins
You only need to add an entry in `manifests/xxx.json` and follow the same format as the other entries.

## Rules
- Plugin must be open source
- Plugin must be functioning
- Website must be non-profit

This project is a free and open-source project. We welcome any community resource websites/repositories/plugins as long as they follow the rules above, regardless of their popularity.\
Please feel free to submit pull requests or issues, we need your contributions!
