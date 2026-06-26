# Twelfth Night Bridge — Serial Communication
# =============================================

import asyncio
import serial
import serial.tools.list_ports

# Shared state — accessible by websocket_server and server
ser = None
ws_clients = set()


def find_m5_port():
    """Auto-detect M5Stack serial port across platforms."""
    ports = serial.tools.list_ports.comports()
    for p in ports:
        desc = (p.description or '').lower()
        mfg = (p.manufacturer or '').lower()
        if any(k in desc + mfg for k in ['cp210', 'ch340', 'silicon', 'usb serial', 'm5']):
            return p.device
    # Fallback: let user pick from available ports
    if ports:
        print("Available serial ports:")
        for i, p in enumerate(ports):
            print(f"  [{i}] {p.device} - {p.description}")
        idx = int(input("Select port number: "))
        return ports[idx].device
    return None


def serial_read_loop(loop):
    """Read serial data in a background thread and forward to all WebSocket clients."""
    import threading

    def _read():
        buf = b''
        while ser and ser.is_open:
            try:
                data = ser.read(1)
                if data:
                    buf += data
                    if data == b'\n':
                        line = buf.decode('utf-8', errors='ignore').strip()
                        buf = b''
                        if line and ws_clients:
                            for ws in list(ws_clients):
                                asyncio.run_coroutine_threadsafe(ws.send(line), loop)
                            print(f"<< Device: {line}")
                else:
                    import time
                    time.sleep(0.01)
            except Exception as e:
                print(f"Serial read error: {e}")
                break

    t = threading.Thread(target=_read, daemon=True)
    t.start()
