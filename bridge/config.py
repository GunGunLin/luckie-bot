# Twelfth Night Bridge — Configuration
# =====================================

# Serial port for M5StickC Plus hardware companion
# Set to None for auto-detection, or specify a port name:
#   Windows: 'COM3'
#   macOS:   '/dev/cu.usbserial-*'
#   Linux:   '/dev/ttyUSB0'
SERIAL_PORT = None

# Serial communication baud rate (must match firmware)
BAUD_RATE = 115200

# WebSocket server
WS_HOST = 'localhost'
WS_PORT = 9000

# HTTP static file server
HTTP_PORT = 8080
