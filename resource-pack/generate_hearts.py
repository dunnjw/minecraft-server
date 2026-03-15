"""Generate chive-themed heart sprites for The Chive resource pack.

Each heart sprite is 9x9 pixels. We're replacing the red hearts with
green chive-shaped icons.
"""
from PIL import Image

# Colors
DARK_GREEN = (34, 120, 15, 255)
GREEN = (60, 180, 30, 255)
LIGHT_GREEN = (100, 210, 70, 255)
PURPLE_TIP = (180, 100, 200, 255)  # chive flower bud
DARK_OUTLINE = (20, 70, 10, 255)
TRANSPARENT = (0, 0, 0, 0)
GRAY_OUTLINE = (50, 50, 50, 255)
DARK_GRAY = (30, 30, 30, 255)
CONTAINER_GRAY = (30, 30, 30, 180)

def make_full_chive():
    """Full chive heart - a little chive stalk with purple tip."""
    img = Image.new("RGBA", (9, 9), TRANSPARENT)
    p = img.putpixel

    # Chive stalk shape (two stalks leaning together like a heart)
    # Row 0 (top) - purple flower tips
    p((2, 0), PURPLE_TIP)
    p((6, 0), PURPLE_TIP)

    # Row 1
    p((2, 1), LIGHT_GREEN)
    p((6, 1), LIGHT_GREEN)

    # Row 2 - stalks angle inward
    p((3, 2), GREEN)
    p((5, 2), GREEN)

    # Row 3
    p((3, 3), GREEN)
    p((4, 3), DARK_GREEN)
    p((5, 3), GREEN)

    # Row 4 - stalks merge
    p((3, 4), GREEN)
    p((4, 4), GREEN)
    p((5, 4), GREEN)

    # Row 5
    p((4, 5), GREEN)
    p((3, 5), DARK_GREEN)
    p((5, 5), DARK_GREEN)

    # Row 6
    p((4, 6), DARK_GREEN)

    # Row 7 - base
    p((4, 7), DARK_OUTLINE)

    return img


def make_half_chive():
    """Half chive - left stalk only."""
    img = Image.new("RGBA", (9, 9), TRANSPARENT)
    p = img.putpixel

    # Left stalk only
    p((2, 0), PURPLE_TIP)
    p((2, 1), LIGHT_GREEN)
    p((3, 2), GREEN)
    p((3, 3), GREEN)
    p((3, 4), GREEN)
    p((3, 5), DARK_GREEN)
    p((4, 6), DARK_GREEN)
    p((4, 7), DARK_OUTLINE)

    return img


def make_container():
    """Container/outline - subtle dark outline of the chive shape."""
    img = Image.new("RGBA", (9, 9), TRANSPARENT)
    p = img.putpixel

    p((2, 0), DARK_GRAY)
    p((6, 0), DARK_GRAY)
    p((2, 1), DARK_GRAY)
    p((6, 1), DARK_GRAY)
    p((3, 2), DARK_GRAY)
    p((5, 2), DARK_GRAY)
    p((3, 3), DARK_GRAY)
    p((4, 3), DARK_GRAY)
    p((5, 3), DARK_GRAY)
    p((3, 4), DARK_GRAY)
    p((4, 4), DARK_GRAY)
    p((5, 4), DARK_GRAY)
    p((3, 5), DARK_GRAY)
    p((4, 5), DARK_GRAY)
    p((5, 5), DARK_GRAY)
    p((4, 6), DARK_GRAY)
    p((4, 7), DARK_GRAY)

    return img


out = "assets/minecraft/textures/gui/sprites/hud/heart"

# Full heart
make_full_chive().save(f"{out}/full.png")
print("Created full.png")

# Half heart
make_half_chive().save(f"{out}/half.png")
print("Created half.png")

# Container (empty heart outline)
make_container().save(f"{out}/container.png")
print("Created container.png")

# Blinking variants (same but slightly brighter)
full_blink = make_full_chive()
# Brighten slightly for blink effect
for x in range(9):
    for y in range(9):
        r, g, b, a = full_blink.getpixel((x, y))
        if a > 0:
            full_blink.putpixel((x, y), (min(r + 40, 255), min(g + 40, 255), min(b + 40, 255), a))
full_blink.save(f"{out}/full_blinking.png")
print("Created full_blinking.png")

half_blink = make_half_chive()
for x in range(9):
    for y in range(9):
        r, g, b, a = half_blink.getpixel((x, y))
        if a > 0:
            half_blink.putpixel((x, y), (min(r + 40, 255), min(g + 40, 255), min(b + 40, 255), a))
half_blink.save(f"{out}/half_blinking.png")
print("Created half_blinking.png")

container_blink = make_container()
for x in range(9):
    for y in range(9):
        r, g, b, a = container_blink.getpixel((x, y))
        if a > 0:
            container_blink.putpixel((x, y), (min(r + 30, 255), min(g + 30, 255), min(b + 30, 255), a))
container_blink.save(f"{out}/container_blinking.png")
print("Created container_blinking.png")

print("\nDone! All chive heart sprites generated.")
