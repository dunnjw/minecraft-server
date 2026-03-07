# Project Mini-Hive — Wyatt's Minecraft Server

A crossplay Minecraft server running on a Mac mini that lets both **Java Edition** (Mac/PC) and **Bedrock Edition** (iPad/Xbox/Switch) players connect — both locally and over the internet.

## Server Info

- **Server Software:** PaperMC 1.21.11 (build 69)
- **Host Machine:** Mac mini (M4 Pro, 24GB RAM)
- **Server Location:** `/Users/family/dev/minecraft/MinecraftServer`

## Architecture Overview

```
Internet Players
    |
    |-- Java Edition ----> Playit.gg Plugin (TCP tunnel) --+
    |                                                       |
    +-- Bedrock Edition --> Playit-cli (UDP tunnel) --------+
                                                            |
                                                            v
                                                     Mac mini (M4 Pro)
                                                            |
                                             +--------------+--------------+
                                             |              |              |
                                         PaperMC        GeyserMC      Floodgate
                                       (Java server)  (translates    (Xbox auth
                                                       Bedrock->Java) for Bedrock)
```

**LAN players** connect directly — Java on port `25565`, Bedrock on port `19132`.

## Components

| Component | What It Does | How It Runs |
|---|---|---|
| **PaperMC 1.21.11** | The Minecraft server | `java -jar server.jar` in Terminal tab 1 |
| **Geyser-Spigot** (plugin) | Translates Bedrock protocol to Java so iPad/console players can join | Runs inside the server automatically |
| **Floodgate** (plugin) | Lets Bedrock players authenticate with their Xbox account | Runs inside the server automatically |
| **Playit.gg plugin** (plugin) | Creates a TCP tunnel for Java Edition remote access | Runs inside the server automatically |
| **playit-cli** (standalone) | Creates a UDP tunnel for Bedrock Edition remote access | `~/.cargo/bin/playit-cli` in Terminal tab 2 |

## Connection Addresses

| Edition | Address | Port |
|---|---|---|
| Java (remote) | `xbox-bean.gl.joinmc.link` | default (25565) |
| Bedrock (remote) | `deals-everything.gl.at.ply.gg` | `24822` |
| Java (LAN) | `localhost` | `25565` |
| Bedrock (LAN) | `192.168.1.249` | `19132` |

## Starting the Server

You need **two Terminal tabs** running:

### Tab 1: Minecraft Server
```bash
cd /Users/family/dev/minecraft/MinecraftServer
java -jar server.jar
```

### Tab 2: Bedrock Tunnel (Playit.gg standalone agent)
```bash
~/.cargo/bin/playit-cli
```

The Java tunnel runs automatically via the Playit.gg plugin inside the server.
The Bedrock tunnel requires the standalone agent because the plugin only supports TCP (Java) tunnels.

## Stopping the Server

Type `stop` in the server Terminal tab. This saves the world and shuts down gracefully.
**Never close the Terminal window to stop the server** — always use the `stop` command.

## Admin Commands

Type these in the **server Terminal** (not in-game chat):

### Whitelist (controlling who can join)
```
whitelist on              # Turn on the whitelist
whitelist off             # Turn off the whitelist
whitelist add PlayerName  # Allow a player to join
whitelist remove PlayerName  # Remove a player
whitelist list            # See who's on the whitelist
```
**Note:** Whitelist is OFF by default. Anyone with the address can join until you turn it on.
Don't forget to add yourself (`whitelist add Kifoles`) before turning it on!

Bedrock players added via Floodgate have a `.` prefix (e.g., `.twinklemittens`).
To whitelist a Bedrock player: `whitelist add .TheirXboxName`

### Operator (admin powers)
```
op PlayerName             # Give a player admin/operator powers
deop PlayerName           # Remove admin powers
```
Operators can use commands like `/gamemode creative`, `/tp`, `/give`, etc.

### Other Useful Commands
```
ban PlayerName            # Ban a player
pardon PlayerName         # Unban a player
kick PlayerName           # Kick a player (they can rejoin)
say Message               # Broadcast a message to all players
list                      # Show who's currently online
```

### In-Game Commands (type in chat with T key, requires op)
```
/gamemode creative        # Switch to creative mode
/gamemode survival        # Switch to survival mode
/tp PlayerName            # Teleport to a player
/time set day             # Set time to daytime
/weather clear            # Clear the weather
/difficulty easy          # Set difficulty (peaceful/easy/normal/hard)
```

## Key Config Files

| File | What It Controls |
|---|---|
| `MinecraftServer/server.properties` | Server settings (difficulty, max players, view distance, MOTD) |
| `MinecraftServer/plugins/Geyser-Spigot/config.yml` | Bedrock bridge settings (`auth-type: floodgate`) |
| `MinecraftServer/plugins/floodgate/config.yml` | Floodgate settings |
| `MinecraftServer/plugins/playit-gg/config.yml` | Playit tunnel config (sensitive — not in git) |

### server.properties highlights
- `view-distance=10` — How many chunks the server sends to players
- `max-players=20` — Maximum number of players
- `difficulty=easy` — World difficulty
- `motd=A Minecraft Server` — Message shown in server list
- `gamemode=survival` — Default game mode for new players

Edit this file while the server is stopped, then restart.

## Backups

### Backup Script
```bash
cd /Users/family/dev/minecraft
./backup.sh
```
This backs up all three dimensions (overworld, nether, end) and player data (bans, ops, whitelist) to the `backups/` folder with a timestamp.

### Git for Config Tracking
Config and plugin changes are tracked in git. Before making changes:
```bash
cd /Users/family/dev/minecraft
./backup.sh
git add -A && git commit -m "description of change"
```

## Playit.gg Account

- **Website:** https://playit.gg
- **Tunnels page:** https://playit.gg/account/tunnels
- Two agents are registered:
  - `from-key-0fb1` — The Minecraft plugin agent (Java tunnel)
  - `from-key-d79e` — The standalone CLI agent (Bedrock tunnel)

## Software Installed on the Mac mini

| Software | Purpose | Installed Via |
|---|---|---|
| Java 21 (Temurin) | Runs the Minecraft server | `brew install temurin@21` |
| Rust toolchain | Was needed to build playit-cli | `rustup` |
| playit-cli | Bedrock tunnel agent | `cargo install` (built from source) |
| pandoc | Markdown to PDF conversion | `brew install pandoc` |

## Keyboard Controls (for Wyatt)

| Key | Action |
|---|---|
| W A S D | Move |
| Space | Jump (double-tap to fly in Creative) |
| Left Shift | Sneak / fly down |
| Control | Sprint |
| E | Inventory |
| T | Chat |
| Left click (1 finger) | Break / attack |
| Right click (2 fingers) | Place / use |
| Q | Drop item |
| 1-9 | Select hotbar slot |
| Escape | Pause menu |

## Maintenance

### Playit-cli Sessions Expire
The standalone Bedrock tunnel agent sessions can expire after ~36+ hours. **Symptom:** Bedrock friends can't connect remotely. **Fix:** Quit playit-cli (`q`) and restart it.

### Playit Plugin Connection Hiccups
The Java tunnel plugin logs periodic "failed when communicating with tunnel server" errors (roughly every 15 minutes) to an IPv6 address. It reconnects automatically each time. This hasn't caused noticeable player issues but is worth watching.

### Server Updates
When Minecraft releases a new version, players' clients will update and may get "Outdated server" errors. Download the matching PaperMC version from [papermc.io](https://papermc.io) and replace `server.jar`. Stop the server first, back up, then swap the jar.

### Plugin Updates
Geyser, Floodgate, and the Playit plugin may need updates when you update the server. Download new versions from their respective sites and replace the JARs in `MinecraftServer/plugins/`.

## Troubleshooting

- **Server won't start:** Make sure you're in the `MinecraftServer` directory and Java 21 is installed (`java -version`)
- **Bedrock friends can't connect remotely:** Make sure `~/.cargo/bin/playit-cli` is running in a Terminal tab. Session may have expired — restart it.
- **iPad can't connect on LAN:** Check iPad Settings > Minecraft > Local Network is toggled ON
- **"Outdated server" error:** Your Minecraft client version doesn't match the server. Update PaperMC or change your client version.
- **"Invalid session" error:** Quit and relaunch the Minecraft client to refresh the session.
- **Skin warnings in logs:** Geyser couldn't reach its skin API. Not critical — skins may look wrong temporarily.
- **Controller on Java Edition Mac:** Doesn't work due to macOS GLFW/LWJGL limitations. Use keyboard/mouse on Mac, controller on iPad via Bedrock.

## Lessons Learned

- **Controller support on Java Edition Mac is a dead end** — macOS GLFW/LWJGL doesn't properly detect game controllers. Wyatt uses keyboard/mouse on Mac and controller on iPad via Bedrock.
- **iPad Local Network permission** — iOS requires Minecraft to have Local Network access enabled in iPad Settings.
- **Bedrock players have a `.` prefix** — Floodgate prepends `.` to Xbox gamertags for whitelisting and commands.
- **Playit plugin only handles TCP** — That's why we need the standalone `playit-cli` for Bedrock (UDP).
- **playit-cli was built from source** — No macOS binary was available, so we installed Rust and compiled it with `cargo install`.

## Future Ideas

- **Auto-restart script** for playit-cli so it recovers from session expiration automatically
- **Custom MOTD and server.properties tuning**
- **Mods/plugins** — datapacks or server-side plugins for gameplay enhancements
- **Scheduled backups** via cron
