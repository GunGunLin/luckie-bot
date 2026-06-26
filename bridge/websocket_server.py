# Twelfth Night Bridge — WebSocket Server
# =========================================

from .serial_client import ser, ws_clients


async def ws_handler(ws):
    """Handle a WebSocket client connection.

    Receives commands from the browser and forwards them to the
    hardware device over serial.
    """
    ws_clients.add(ws)
    print(f"Browser connected ({len(ws_clients)} client(s))")
    try:
        async for message in ws:
            if ser and ser.is_open:
                cmd = message.strip() + '\n'
                ser.write(cmd.encode('utf-8'))
                print(f">> Sent: {message.strip()}")
            else:
                print(f"Serial not connected, dropped: {message}")
    except Exception as e:
        print(f"WebSocket error: {e}")
    finally:
        ws_clients.discard(ws)
        print(f"Browser disconnected ({len(ws_clients)} client(s))")
