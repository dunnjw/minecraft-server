# Project Mini-Hive — Summary & Maintenance Guide

## What We Built

A crossplay Minecraft server running on your Mac mini that lets both **Java Edition** (Mac/PC) and **Bedrock Edition** (iPad/Xbox/Switch) players connect — both locally and over the internet.

---

## Architecture Overview

```
Internet Players
    │
    ├── Java Edition ──→ Playit.gg Plugin (TCP tunnel) ──┐
    │                                                      │
    └── Bedrock Edition ──→ Playit-cli (UDP tunnel) ──────┤
                                                           │
                                                           ▼
                                                    Mac mini (M4 Pro)
                                                           │
                                            ┌──────────────┼──────────────┐
                                            │              │              │
                                        PaperMC        GeyserMC      Floodgate
                                      (Java server)  (translates    (Xbox auth
                                                      Bedrock→Java)  for Bedrock)
```

**LAN players** connect directly — Java on port `25565`, Bedrock on port `19132`.

---

## Components & What They Do

| Component | What It Does | How It Runs |
|---|---|---|
| **PaperMC 1.21.11** | The actual Minecraft server | `java -jar server.jar` in Terminal tab 1 |
| **Geyser-Spigot** (plugin) | Translates Bedrock protocol → Java so iPad/console players can join | Runs inside the server automatically |
| **Floodgate** (plugin) | Lets Bedrock players authenticate with their Xbox account | Runs inside the server automatically |
| **Playit.gg plugin** (plugin) | Creates a TCP tunnel for Java Edition remote access | Runs inside the server automatically |
| **playit-cli** (standalone) | Creates a UDP tunnel for Bedrock Edition remote access | `~/.cargo/bin/playit-cli` in Terminal tab 2 |

---

## Starting the Server

You need **two Terminal tabs**:

**Tab 1 — Minecraft Server:**
```bash
cd /Users/family/dev/minecraft/MinecraftServer
java -jar server.jar
```

**Tab 2 — Bedrock Tunnel:**
```bash
~/.cargo/bin/playit-cli
```

Stop the server by typing `stop` in Tab 1. **Never** close the Terminal window directly.

---

## Connection Addresses

| Who | Address | Port |
|---|---|---|
| Java (remote) | `xbox-bean.gl.joinmc.link` | default (25565) |
| Bedrock (remote) | `deals-everything.gl.at.ply.gg` | `24822` |
| Java (LAN) | `localhost` | `25565` |
| Bedrock (LAN) | `192.168.1.249` | `19132` |

---

## Things to Keep an Eye On

### 1. Playit-cli Sessions Expire

The standalone Bedrock tunnel agent (`playit-cli`) sessions can expire after running for a long time (~36+ hours). **Symptom:** Bedrock friends can't connect remotely. **Fix:** Quit playit-cli (`q`) and restart it.

### 2. Playit Plugin Connection Hiccups

The Java tunnel plugin logs periodic "failed when communicating with tunnel server" errors (roughly every 15 minutes) to an IPv6 address. It reconnects automatically each time. This hasn't caused noticeable player issues but is worth watching. If Java remote connections become unreliable, this could be the cause.

### 3. World Backups

Backups are **manual**. Run before making any major changes:
```bash
cd /Users/family/dev/minecraft
./backup.sh
```
This backs up all three dimensions (overworld, nether, end) and player data to the `backups/` folder with a timestamp.

### 4. Server Updates

When Minecraft releases a new version, your players' clients will update and may get "Outdated server" errors. You'll need to download the matching PaperMC version from [papermc.io](https://papermc.io) and replace `server.jar`. Stop the server first, back up, then swap the jar.

### 5. Plugin Updates

Geyser, Floodgate, and the Playit plugin may need updates when you update the server. Download new versions from their respective sites and replace the JARs in `MinecraftServer/plugins/`.

### 6. Git for Config Tracking

Config changes are tracked in git. Before making plugin or config changes:
```bash
cd /Users/family/dev/minecraft
./backup.sh          # back up worlds
git add -A && git commit -m "description of change"
```

---

## Software Installed on the Mac mini

| Software | Purpose | Installed Via |
|---|---|---|
| Java 21 (Temurin) | Runs the Minecraft server | `brew install temurin@21` |
| Rust toolchain | Was needed to build playit-cli | `rustup` |
| playit-cli | Bedrock tunnel agent | `cargo install` (built from source) |

---

## Key Config Files

| File | What It Controls |
|---|---|
| `MinecraftServer/server.properties` | Server settings (difficulty, max players, view distance, MOTD) |
| `MinecraftServer/plugins/Geyser-Spigot/config.yml` | Bedrock bridge settings (`auth-type: floodgate`) |
| `MinecraftServer/plugins/floodgate/config.yml` | Floodgate settings |
| `MinecraftServer/plugins/playit-gg/config.yml` | Playit tunnel config (sensitive — not in git) |

---

## Lessons Learned Along the Way

- **Controller support on Java Edition Mac is a dead end** — macOS GLFW/LWJGL doesn't properly detect game controllers. Wyatt uses keyboard/mouse on Mac and controller on iPad via Bedrock.
- **iPad "can't connect" on LAN** — Check iPad Settings → Minecraft → Local Network is toggled ON.
- **"Invalid session" errors** — Quit and relaunch the Minecraft client to refresh the session.
- **Bedrock players have a `.` prefix** — When whitelisting, use `.TheirXboxName` (e.g., `whitelist add .twinklemittens`).

---

## Future Ideas (Not Yet Done)

- **Auto-restart script** for playit-cli so it recovers from session expiration automatically
- **Custom MOTD and server.properties tuning**
- **Mods/plugins** — datapacks or server-side plugins for gameplay enhancements
- **Scheduled backups** via cron
