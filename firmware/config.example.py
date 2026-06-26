# Twelfth Night — Firmware Configuration
# =======================================
# Copy relevant values into main.py when customising your hardware setup.

# ── LED Strip ──────────────────────────────────────────
NUM_LEDS = 16          # Number of SK6812 LEDs in the strip
LED_PIN = 26           # GPIO pin for LED data line
LED_TYPE = "SK6812"    # LED chip type (SK6812 or WS2812)

# ── Display ────────────────────────────────────────────
LCD_ROTATION = 1       # 0=portrait, 1=landscape
LCD_WIDTH = 240        # Display width in pixels
LCD_HEIGHT = 135       # Display height in pixels

# ── Interaction Categories ─────────────────────────────
# Displayed on the category selection screen
CATEGORIES = ['Wealth', 'Study', 'Love', 'General']

# ── LED Animation ──────────────────────────────────────
STRIP_UPDATE_INTERVAL = 3   # Update every N ticks (20ms per tick)
BREATHE_BRIGHTNESS = 55     # Max brightness for breathe mode (0-255)
PULSE_BRIGHTNESS = 75       # Max brightness for pulse mode (0-255)

# ── Serial ─────────────────────────────────────────────
BAUD_RATE = 115200
