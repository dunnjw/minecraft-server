#!/bin/bash
# =============================================
# Minecraft Server Backup Script
# Run this before making changes or regularly
# =============================================

SERVER_DIR="/Users/family/dev/minecraft/MinecraftServer"
BACKUP_DIR="/Users/family/dev/minecraft/backups"
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
BACKUP_NAME="backup-$TIMESTAMP"
BACKUP_PATH="$BACKUP_DIR/$BACKUP_NAME"

echo "=== Minecraft World Backup ==="
echo "Timestamp: $TIMESTAMP"
echo ""

# Create backup directory if it doesn't exist
mkdir -p "$BACKUP_PATH"

# Back up world data
echo "Backing up Overworld..."
cp -r "$SERVER_DIR/world" "$BACKUP_PATH/world"

echo "Backing up Nether..."
cp -r "$SERVER_DIR/world_nether" "$BACKUP_PATH/world_nether"

echo "Backing up The End..."
cp -r "$SERVER_DIR/world_the_end" "$BACKUP_PATH/world_the_end"

# Back up player-related data
echo "Backing up player data..."
cp "$SERVER_DIR/banned-ips.json" "$BACKUP_PATH/"
cp "$SERVER_DIR/banned-players.json" "$BACKUP_PATH/"
cp "$SERVER_DIR/ops.json" "$BACKUP_PATH/"
cp "$SERVER_DIR/whitelist.json" "$BACKUP_PATH/"

# Calculate size
BACKUP_SIZE=$(du -sh "$BACKUP_PATH" | cut -f1)

echo ""
echo "Backup complete!"
echo "Location: $BACKUP_PATH"
echo "Size: $BACKUP_SIZE"
echo ""

# Show existing backups
echo "=== All Backups ==="
ls -1 "$BACKUP_DIR" | while read dir; do
    SIZE=$(du -sh "$BACKUP_DIR/$dir" 2>/dev/null | cut -f1)
    echo "  $dir  ($SIZE)"
done
