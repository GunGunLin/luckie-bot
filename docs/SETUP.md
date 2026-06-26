# Setup Guide — Twelfth Night

This guide covers the complete setup process for running Twelfth Night locally, including the optional hardware companion.

## Prerequisites

| Component | Requirement | Notes |
|-----------|------------|-------|
| Python | 3.10 or later | Check with `python --version` |
| Browser | Chrome 90+ or Edge 90+ | Required for MediaPipe WebAssembly |
| pip | Latest stable | Update with `pip install --upgrade pip` |
| USB port | Available | For hardware companion only |
| SiliconFlow account | Free tier | Sign up at [siliconflow.cn](https://siliconflow.cn) |

## Quick Start (Web App Only)

The web application works standalone — no hardware required.

```bash
# 1. Clone the repository
git clone https://github.com/GunGunLin/luckie-bot.git
cd luckie-bot

# 2. Install Python dependencies
pip install -r requirements.txt

# 3. Start the bridge server
cd bridge
python server.py
```

You should see output similar to:

```
==================================================
  🔮 Luckie-Bot · Arcanum Lab 桥接服务器
==================================================
WebSocket 服务: ws://localhost:9000
HTTP 服务: http://localhost:8080

请在浏览器打开:
  http://localhost:8080
```

**4. Open the web app**

Navigate to `http://localhost:8080` in your browser.

**5. Configure your API key**

Click the settings icon (⚙️) in the top bar and enter your SiliconFlow API key. The key is stored locally in your browser's `localStorage` and is never sent to any server other than SiliconFlow's API.

**6. Start interacting**

Choose a category and follow the on-screen guidance. Use hand gestures in front of your webcam to draw cards.

## Hardware Setup (Optional)

To use the physical companion device:

### Hardware Required

- **M5StickC Plus** ×1 (ESP32-based IoT development board with LCD)
- **SK6812 LED strip** ×1 (16 LEDs recommended; 8-LED minimum)
- **USB-C cable** ×1 (for flashing and power)
- Optional: 3D-printed or custom enclosure

### Flashing the Firmware

1. Install [Thonny IDE](https://thonny.org/) or [M5Burner](https://docs.m5stack.com/en/download)
2. Connect the M5StickC Plus to your computer via USB-C
3. Open `firmware/main.py` in Thonny
4. Select the correct interpreter: **MicroPython (ESP32)** on the correct COM port
5. Click **Run** to upload and execute the firmware
6. The device LCD should display "Luckie-Bot" and show the category selection screen

### Connecting the LED Strip

The SK6812 LED strip connects to GPIO 26 on the M5StickC Plus:

```
M5StickC Plus         SK6812 LED Strip
─────────────         ────────────────
GND        ────────── GND
5V         ────────── VCC (5V)
GPIO 26    ────────── DATA IN
```

> **Note:** If using more than 16 LEDs, external 5V power may be required. The M5StickC Plus USB port can power up to ~16 LEDs at moderate brightness.

### Running with Hardware

1. Ensure the firmware is flashed and the device is connected via USB
2. Start the bridge server as described above
3. The bridge server will auto-detect the M5StickC Plus serial port
4. If auto-detection fails, you will be prompted to select the port manually
5. Once connected, the hardware device will respond to interactions from the web app

### Hardware-Only Mode

The M5StickC Plus can operate as a standalone device without the web app:

- **Button A:** Cycle through interaction categories
- **Button B:** Confirm selection / return to category menu
- **LED strip:** Displays colour feedback based on selected category
- **LCD:** Shows category selection and status information

## Troubleshooting

### Bridge server won't start

- Ensure no other process is using ports 8080 and 9000
- Check Python version: `python --version` (requires 3.10+)
- Verify dependencies: `pip install -r requirements.txt`

### Serial port not detected

- Close Thonny, M5Burner, or any other program using the serial port
- Unplug and reconnect the M5StickC Plus
- On Windows: check Device Manager for the COM port number
- On macOS: check `ls /dev/cu.*` for the device

### Gesture recognition not working

- Ensure your browser supports WebAssembly (Chrome/Edge recommended)
- Allow camera access when prompted
- Ensure adequate lighting on your hands
- Keep hands within the camera frame

### API key not working

- Verify your SiliconFlow account has available credits
- Check that the API key is entered correctly (no extra spaces)
- Test the key with a simple API call to verify it's active

### LED strip not lighting up

- Check the wiring connections (GND, VCC, DATA)
- Verify the GPIO pin matches the firmware configuration (default: GPIO 26)
- Try reducing the number of LEDs in `NUM_LEDS` if using a different strip length
- The system degrades gracefully — LED failure does not affect other functionality

## Development Notes

- The web app is a single HTML file — no build step, no bundler
- The Python bridge uses only standard library + websockets + pyserial
- The MicroPython firmware is self-contained and requires no additional libraries
- All three layers can be developed and tested independently
