# Project Mini-Hive - Wyatt's Minecraft Server

## Server Info

- **Server Software:** PaperMC 1.21.11
- **Host Machine:** Mac mini (M4 Pro, 24GB RAM)
- **Server Location:** `/Users/family/dev/minecraft/MinecraftServer`

## Connection Addresses

| Edition | Address | Port |
|---|---|---|
| Java (remote) | `xbox-bean.gl.joinmc.link` | default (25565) |
| Bedrock (remote) | `deals-everything.gl.at.ply.gg` | `24822` |
| Java (local/LAN) | `localhost` | `25565` |
| Bedrock (local/LAN) | `192.168.1.249` | `19132` |

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
The Bedrock tunnel requires the standalone agent because the plugin only supports Java tunnels.

## Stopping the Server

Type `stop` in the server Terminal tab. This saves the world and shuts down gracefully.
**Never close the Terminal window to stop the server** - always use the `stop` command.

## Plugins

Located in `MinecraftServer/plugins/`:

| Plugin | Purpose |
|---|---|
| **Geyser-Spigot** | Translates Bedrock protocol to Java - lets iPad/console players join |
| **floodgate-spigot** | Lets Bedrock players join with their Xbox account (no Java account needed) |
| **playit-minecraft-plugin** | Creates the Java tunnel to Playit.gg for remote access |

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

Bedrock players added via Floodgate will have a `.` prefix (e.g., `.twinklemittens`).
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

## Server Configuration

### server.properties
Located at `MinecraftServer/server.properties`. Key settings:
- `view-distance=10` - How many chunks the server sends to players (can increase for better visibility)
- `max-players=20` - Maximum number of players
- `difficulty=easy` - World difficulty
- `motd=A Minecraft Server` - Message shown in server list
- `gamemode=survival` - Default game mode for new players

Edit this file while the server is stopped, then restart.

### Geyser Config
Located at `MinecraftServer/plugins/Geyser-Spigot/config.yml`
- `auth-type: floodgate` - Lets Bedrock players use Xbox accounts
- `port: 19132` - Bedrock listening port

## Backups

Regularly copy the `world`, `world_nether`, and `world_the_end` folders somewhere safe.

Quick backup command:
```bash
cp -r /Users/family/dev/minecraft/MinecraftServer/world /Users/family/dev/minecraft/backups/world-$(date +%Y%m%d-%H%M%S)
cp -r /Users/family/dev/minecraft/MinecraftServer/world_nether /Users/family/dev/minecraft/backups/world_nether-$(date +%Y%m%d-%H%M%S)
cp -r /Users/family/dev/minecraft/MinecraftServer/world_the_end /Users/family/dev/minecraft/backups/world_the_end-$(date +%Y%m%d-%H%M%S)
```
Create the backups folder first: `mkdir -p /Users/family/dev/minecraft/backups`

## Playit.gg Account

- **Website:** https://playit.gg
- **Tunnels page:** https://playit.gg/account/tunnels
- Two agents are registered:
  - `from-key-0fb1` - The Minecraft plugin agent (Java tunnel only)
  - `from-key-d79e` - The standalone CLI agent (Bedrock tunnel)
- Verify your email if you haven't already

## Software Installed

| Software | Purpose | Install Method |
|---|---|---|
| Java 21 (Temurin) | Runs the Minecraft server | `brew install temurin@21` |
| Rust | Used to build the Playit agent | `rustup` |
| playit-cli | Standalone Playit.gg agent for Bedrock tunnel | Built from source via `cargo` |

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

## Troubleshooting

- **Server won't start:** Make sure you're in the `MinecraftServer` directory and Java 21 is installed (`java -version`)
- **Bedrock friends can't connect remotely:** Make sure `~/.cargo/bin/playit-cli` is running in a Terminal tab
- **iPad can't connect on LAN:** Check iPad Settings > Minecraft > Local Network is toggled ON
- **"Outdated server" error:** Your Minecraft client version doesn't match the server. Update PaperMC or change your client version
- **Skin warnings in logs:** Geyser couldn't reach its skin API. Not critical - skins may look wrong temporarily
