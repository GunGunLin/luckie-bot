"""
Luckie-Bot Bridge Server: 浏览器 WebSocket <-> M5Stack 串口
运行: cd bridge && python server.py
然后浏览器打开: http://localhost:8080
"""
import asyncio
import json
import os
import serial
import serial.tools.list_ports
from websockets.server import serve

# === 配置 ===
SERIAL_PORT = None  # 自动检测
BAUD_RATE = 115200
WS_HOST = 'localhost'
WS_PORT = 9000
HTTP_PORT = 8080

# Serve web files from the sibling web/ directory
WEB_ROOT = os.path.join(os.path.dirname(__file__), '..', 'web')

def find_m5_port():
    """自动查找 M5Stack 串口"""
    ports = serial.tools.list_ports.comports()
    for p in ports:
        desc = (p.description or '').lower()
        mfg = (p.manufacturer or '').lower()
        if any(k in desc + mfg for k in ['cp210', 'ch340', 'silicon', 'usb serial', 'm5']):
            return p.device
    # 没找到就列出所有端口让用户选
    if ports:
        print("可用串口:")
        for i, p in enumerate(ports):
            print(f"  [{i}] {p.device} - {p.description}")
        idx = int(input("选择串口编号: "))
        return ports[idx].device
    return None

# === 串口读写 ===
ser = None
ws_clients = set()

def serial_read_loop(loop):
    """在后台线程中读取串口数据，转发给所有 WebSocket 客户端"""
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
                                asyncio.run_coroutine_threadsafe(
                                    ws.send(line), loop
                                )
                            print(f"<< 设备: {line}")
                else:
                    import time; time.sleep(0.01)
            except Exception as e:
                print(f"串口读取错误: {e}")
                break
    t = threading.Thread(target=_read, daemon=True)
    t.start()

# === WebSocket 处理 ===
async def ws_handler(ws):
    ws_clients.add(ws)
    print(f"浏览器已连接 ({len(ws_clients)} 个客户端)")
    try:
        async for message in ws:
            # 浏览器发来的指令 -> 转发给串口
            if ser and ser.is_open:
                cmd = message.strip() + '\n'
                ser.write(cmd.encode('utf-8'))
                print(f">> 发送: {message.strip()}")
            else:
                print(f"串口未连接, 丢弃: {message}")
    except Exception as e:
        print(f"WebSocket 错误: {e}")
    finally:
        ws_clients.discard(ws)
        print(f"浏览器断开 ({len(ws_clients)} 个客户端)")

# === HTTP 服务 (简单文件服务器) ===
async def http_handler(reader, writer):
    data = await reader.read(4096)
    request = data.decode('utf-8', errors='ignore')
    first_line = request.split('\n')[0]

    # 提取路径
    try:
        path = first_line.split(' ')[1]
    except:
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
        # 简单 MIME 类型
        if filepath.endswith('.html'):
            ct = 'text/html'
        elif filepath.endswith('.js'):
            ct = 'application/javascript'
        elif filepath.endswith('.css'):
            ct = 'text/css'
        elif filepath.endswith('.jpg') or filepath.endswith('.jpeg'):
            ct = 'image/jpeg'
        elif filepath.endswith('.png'):
            ct = 'image/png'
        else:
            ct = 'application/octet-stream'

        header = f'HTTP/1.1 200 OK\r\nContent-Type: {ct}\r\nContent-Length: {len(content)}\r\nConnection: close\r\n\r\n'
        writer.write(header.encode() + content)
        await writer.drain()
    except FileNotFoundError:
        msg = b'HTTP/1.1 404 Not Found\r\nContent-Length: 9\r\n\r\nNot Found'
        writer.write(msg)
        await writer.drain()
    writer.close()

# === 主程序 ===
async def main():
    global ser, SERIAL_PORT

    print("=" * 50)
    print("  🔮 Luckie-Bot · Arcanum Lab 桥接服务器")
    print("=" * 50)

    # 查找串口
    if not SERIAL_PORT:
        SERIAL_PORT = find_m5_port()

    if not SERIAL_PORT:
        print("未找到串口! 请连接 M5Stack 后重试")
        return

    # 打开串口
    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=0)
        print(f"串口已打开: {SERIAL_PORT} @ {BAUD_RATE}")
    except Exception as e:
        print(f"串口打开失败: {e}")
        print("请关闭 Thonny/M5Burner 后重试")
        return

    loop = asyncio.get_event_loop()
    serial_read_loop(loop)

    # 启动 WebSocket 服务
    ws_server = await serve(ws_handler, WS_HOST, WS_PORT)
    print(f"WebSocket 服务: ws://{WS_HOST}:{WS_PORT}")

    # 启动 HTTP 服务
    http_server = await asyncio.start_server(http_handler, '0.0.0.0', HTTP_PORT)
    print(f"HTTP 服务: http://localhost:{HTTP_PORT}")
    print()
    print("请在浏览器打开:")
    print(f"  http://localhost:{HTTP_PORT}")
    print()
    print("按 Ctrl+C 停止")

    await asyncio.Future()  # 永久运行

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n已停止")
        if ser:
            ser.close()
