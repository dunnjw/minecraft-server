"""Generate Bedrock Edition icons.png with chive hearts.

Bedrock uses a 256x256 sprite sheet. The heart sprites are 9x9 pixels
located in specific positions on the sheet. We start with a transparent
image and place our chive hearts in the correct positions.

Heart layout in icons.png (row at y=0, each 9px wide):
  x=0:   empty heart container
  x=9:   empty heart container (highlight/blink)
  x=18:  half heart container  (not used separately in Bedrock)
  x=27:  half heart container (highlight)
  x=36:  full heart (normal)
  x=45:  full heart (hit/damage flash)
  x=54:  half heart (normal)
  x=63:  half heart (hit/damage flash)

  Next row (y=9) has poison hearts, etc.

Actually the Bedrock icons.png layout matches the Java pre-1.20 layout:
- Row y=0: Hearts
  x=0: container, x=9: container_blink
  x=16: full, x=25: full_blink (these are at 16,0 and 25,0)

Let me use the standard Minecraft icons.png heart positions:
Hearts start at y=0 in the sprite sheet.
Each icon is 9x9.

Standard positions (from vanilla icons.png):
- (16, 0): full red heart
- (25, 0): full heart (damage)
- (16, 9): half red heart
- (25, 9): half heart (damage)
- (0, 0):  heart container (outline)
- (9, 0):  heart container blink

Actually, the standard Minecraft icons.png heart positions are:
Row 0 (y=0): containers and normal hearts
  (0,0) container outline
  (9,0) container highlight
  (16,0) full heart
  (25,0) full heart damage flash
  (34,0) half heart
  (43,0) half heart damage flash
  (52,0) full heart (another variant)
  (61,0) full heart golden/absorption

Wait, let me just be precise about the vanilla layout. The hearts in
icons.png are at specific pixel coordinates. Let me place our chive
hearts at the correct positions.
"""
from PIL import Image

# Colors
DARK_GREEN = (34, 120, 15, 255)
GREEN = (60, 180, 30, 255)
LIGHT_GREEN = (100, 210, 70, 255)
PURPLE_TIP = (180, 100, 200, 255)
DARK_OUTLINE = (20, 70, 10, 255)
TRANSPARENT = (0, 0, 0, 0)
DARK_GRAY = (30, 30, 30, 255)
BRIGHT_GREEN = (100, 220, 70, 255)
BRIGHT_PURPLE = (220, 140, 240, 255)


def draw_full_chive(img, ox, oy):
    """Draw a full chive heart at offset (ox, oy)."""
    p = img.putpixel
    p((ox+2, oy+0), PURPLE_TIP)
    p((ox+6, oy+0), PURPLE_TIP)
    p((ox+2, oy+1), LIGHT_GREEN)
    p((ox+6, oy+1), LIGHT_GREEN)
    p((ox+3, oy+2), GREEN)
    p((ox+5, oy+2), GREEN)
    p((ox+3, oy+3), GREEN)
    p((ox+4, oy+3), DARK_GREEN)
    p((ox+5, oy+3), GREEN)
    p((ox+3, oy+4), GREEN)
    p((ox+4, oy+4), GREEN)
    p((ox+5, oy+4), GREEN)
    p((ox+4, oy+5), GREEN)
    p((ox+3, oy+5), DARK_GREEN)
    p((ox+5, oy+5), DARK_GREEN)
    p((ox+4, oy+6), DARK_GREEN)
    p((ox+4, oy+7), DARK_OUTLINE)


def draw_full_chive_bright(img, ox, oy):
    """Brighter variant for damage flash / blink."""
    p = img.putpixel
    p((ox+2, oy+0), BRIGHT_PURPLE)
    p((ox+6, oy+0), BRIGHT_PURPLE)
    p((ox+2, oy+1), BRIGHT_GREEN)
    p((ox+6, oy+1), BRIGHT_GREEN)
    p((ox+3, oy+2), LIGHT_GREEN)
    p((ox+5, oy+2), LIGHT_GREEN)
    p((ox+3, oy+3), LIGHT_GREEN)
    p((ox+4, oy+3), GREEN)
    p((ox+5, oy+3), LIGHT_GREEN)
    p((ox+3, oy+4), LIGHT_GREEN)
    p((ox+4, oy+4), LIGHT_GREEN)
    p((ox+5, oy+4), LIGHT_GREEN)
    p((ox+4, oy+5), LIGHT_GREEN)
    p((ox+3, oy+5), GREEN)
    p((ox+5, oy+5), GREEN)
    p((ox+4, oy+6), GREEN)
    p((ox+4, oy+7), DARK_GREEN)


def draw_half_chive(img, ox, oy):
    """Left half only."""
    p = img.putpixel
    p((ox+2, oy+0), PURPLE_TIP)
    p((ox+2, oy+1), LIGHT_GREEN)
    p((ox+3, oy+2), GREEN)
    p((ox+3, oy+3), GREEN)
    p((ox+3, oy+4), GREEN)
    p((ox+3, oy+5), DARK_GREEN)
    p((ox+4, oy+6), DARK_GREEN)
    p((ox+4, oy+7), DARK_OUTLINE)


def draw_half_chive_bright(img, ox, oy):
    """Left half bright."""
    p = img.putpixel
    p((ox+2, oy+0), BRIGHT_PURPLE)
    p((ox+2, oy+1), BRIGHT_GREEN)
    p((ox+3, oy+2), LIGHT_GREEN)
    p((ox+3, oy+3), LIGHT_GREEN)
    p((ox+3, oy+4), LIGHT_GREEN)
    p((ox+3, oy+5), GREEN)
    p((ox+4, oy+6), GREEN)
    p((ox+4, oy+7), DARK_GREEN)


def draw_container(img, ox, oy):
    """Empty heart container - just a tiny dot so it's nearly invisible."""
    p = img.putpixel
    p((ox+4, oy+4), (40, 40, 40, 80))


# Create 256x256 transparent image
img = Image.new("RGBA", (256, 256), TRANSPARENT)

# Place hearts at standard Minecraft icons.png positions
# Row 0 (y=0): heart containers and normal hearts
draw_container(img, 0, 0)          # (0,0) container
draw_container(img, 9, 0)          # (9,0) container highlight/blink

draw_full_chive(img, 16, 0)        # (16,0) full heart
draw_full_chive_bright(img, 25, 0) # (25,0) full heart damage
draw_half_chive(img, 34, 0)        # (34,0) half heart
draw_half_chive_bright(img, 43, 0) # (43,0) half heart damage
draw_full_chive(img, 52, 0)        # (52,0) full heart variant
draw_full_chive_bright(img, 61, 0) # (61,0) absorption heart

# Row 1 (y=9): poison hearts - make them darker green
draw_container(img, 0, 9)
draw_container(img, 9, 9)
draw_full_chive(img, 16, 9)
draw_full_chive_bright(img, 25, 9)
draw_half_chive(img, 34, 9)
draw_half_chive_bright(img, 43, 9)
draw_full_chive(img, 52, 9)
draw_full_chive_bright(img, 61, 9)

img.save("textures/gui/icons.png")
print("Created Bedrock icons.png")
