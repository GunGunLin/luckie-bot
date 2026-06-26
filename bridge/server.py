"""
Twelfth Night Bridge Server
============================
WebSocket-to-Serial relay connecting the browser interface to the
M5StickC Plus hardware companion.

Usage:  cd bridge && python server.py
        Then open http://localhost:8080
"""
import asyncio
import os
import serial

from websockets.server import serve

from config import SERIAL_PORT, BAUD_RATE, WS_HOST, WS_PORT, HTTP_PORT
from serial_client import ser, ws_clients, find_m5_port, serial_read_loop
from websocket_server import ws_handler


# Serve web files from the sibling web/ directory
WEB_ROOT = os.path.join(os.path.dirname(__file__), '..', 'web')


# ═══════════════════════════════════════════════════
#  HTTP Static File Server
# ═══════════════════════════════════════════════════

async def http_handler(reader, writer):
    """Serve static files from the web/ directory with MIME type detection."""
    data = await reader.read(4096)
    request = data.decode('utf-8', errors='ignore')
    first_line = request.split('\n')[0]

    try:
        path = first_line.split(' ')[1]
    except (IndexError, ValueError):
        writer.close()
        return

    if path == '/':
        path = '/index.html'

    # Security: prevent directory traversal
    filepath = os.path.normpath(os.path.join(WEB_ROOT, path.lstrip('/')))
    if not filepath.startswith(os.path.normpath(WEB_ROOT)):
        writer.close()
        return

    try:
        with open(filepath, 'rb') as f:
            content = f.read()

        # MIME type detection
        ext_to_mime = {
            '.html': 'text/html',
            '.js':    'application/javascript',
            '.css':   'text/css',
            '.jpg':   'image/jpeg',
            '.jpeg':  'image/jpeg',
            '.png':   'image/png',
            '.svg':   'image/svg+xml',
        }
        ct = ext_to_mime.get(os.path.splitext(filepath)[1].lower(), 'application/octet-stream')

        header = (
            f'HTTP/1.1 200 OK\r\n'
            f'Content-Type: {ct}\r\n'
            f'Content-Length: {len(content)}\r\n'
            f'Connection: close\r\n\r\n'
        )
        writer.write(header.encode() + content)
        await writer.drain()
    except FileNotFoundError:
        msg = b'HTTP/1.1 404 Not Found\r\nContent-Length: 9\r\n\r\nNot Found'
        writer.write(msg)
        await writer.drain()
    writer.close()


# ═══════════════════════════════════════════════════
#  Main Entry Point
# ═══════════════════════════════════════════════════

async def main():
    global ser

    print("=" * 50)
    print("  Twelfth Night · Bridge Server")
    print("=" * 50)

    # Auto-detect or prompt for serial port
    port_name = SERIAL_PORT or find_m5_port()
    if not port_name:
        print("No serial port found. Connect the M5StickC Plus and retry.")
        return

    # Open serial connection to hardware device
    try:
        ser = serial.Serial(port_name, BAUD_RATE, timeout=0)
        print(f"Serial: {port_name} @ {BAUD_RATE} baud")
    except Exception as e:
        print(f"Serial open failed: {e}")
        print("Close Thonny / M5Burner and retry.")
        return

    loop = asyncio.get_event_loop()
    serial_read_loop(loop)

    # Start WebSocket server
    ws_server = await serve(ws_handler, WS_HOST, WS_PORT)
    print(f"WebSocket: ws://{WS_HOST}:{WS_PORT}")

    # Start HTTP server
    http_server = await asyncio.start_server(http_handler, '0.0.0.0', HTTP_PORT)
    print(f"HTTP: http://localhost:{HTTP_PORT}")
    print()
    print("Open in browser:")
    print(f"  http://localhost:{HTTP_PORT}")
    print()
    print("Press Ctrl+C to stop.")

    await asyncio.Future()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nBridge stopped.")
        if ser:
            ser.close()
