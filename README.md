<div align="center">

<img src="docs/logo.svg" width="100" alt="Arcanum Lab">

# 🔮 Luckie-Bot

### AI-Powered Tarot Companion · Hardware × LLM × Computer Vision

<br>

[![Demo Day](https://img.shields.io/badge/🏆_Demo_Day-Champion-gold?style=flat-square&labelColor=1a1a2e)]()
[![LLM](https://img.shields.io/badge/AI-DeepSeek_V3-blueviolet?style=flat-square&labelColor=1a1a2e)]()
[![CV](https://img.shields.io/badge/CV-MediaPipe_Hands-00ccff?style=flat-square&labelColor=1a1a2e)]()
[![Hardware](https://img.shields.io/badge/HW-M5StickC_Plus-orange?style=flat-square&labelColor=1a1a2e)]()
[![License](https://img.shields.io/badge/license-MIT-green?style=flat-square&labelColor=1a1a2e)]()

</div>

<br>

---

## What is Luckie-Bot?

Luckie-Bot is an end-to-end AI product that combines a physical companion device with a beautiful web app for immersive tarot readings. Users interact through **natural hand gestures**, receive **AI-generated oracles** from DeepSeek-V3, and watch their **digital garden grow** — while a hardware device responds in real time with dynamic lighting and expressions.

> 🥇 **Won 1st Place** at XJTLU ENT 208 Demo Day, evaluated across innovation, technical depth, UX, and business viability.

<p align="center">
  <img src="docs/screenshots/user-testing.png" width="85%" alt="User testing Luckie-Bot">
</p>

---

## 🎯 Product at a Glance

| Feature | Description |
|---------|-------------|
| 🎴 **AI Oracle** | DeepSeek-V3 generates personalized, poetic readings across 4 life categories |
| ✋ **Gesture Control** | MediaPipe tracks 21 hand landmarks — pinch, palm, and fist to interact touch-free |
| 💡 **Hardware Companion** | M5StickC Plus reacts with LED breathing lights, LCD facial expressions, and sound |
| 🌱 **Psionic Garden** | Your virtual plant grows with each divination — 5 stages from Seed to Cosmic Tree |
| 🧘 **Meditation Mode** | Guided breathing orb with particle effects before each reading |

---

## 🏗️ Architecture

```
Web Browser ◄── WebSocket ──► Python Bridge ◄── Serial ──► M5StickC Plus
     │                              │                          │
     │ HTTPS                        │                          │
     ▼                              ▼                          ▼
 DeepSeek-V3               asyncio Server              LED · LCD · Buzzer
 (AI Oracle)               (Command Router)            (Ambient Feedback)
 MediaPipe Hands
 (Gesture Pipeline)
```

**Three layers, one experience:** the browser handles AI + vision + rendering, the Python bridge relays commands in real time, and the hardware provides tangible feedback you can see and feel.

---

## 🖼️ Demo Day

<p align="center">
  <img src="docs/screenshots/demo-day-01.jpg" width="45%" alt="Demo Day">
  <img src="docs/screenshots/demo-day-02.jpg" width="45%" alt="Demo Day">
</p>

Judges' takeaway: *"This isn't a course project — it's an investable MVP."*

---

## 🚀 Deploy in 3 Minutes

### Prerequisites
- **Hardware:** M5StickC Plus + SK6812 LED strip (optional — the web app works standalone)
- **Software:** Python 3.10+, a modern browser (Chrome/Edge)
- **API Key:** Free from [SiliconFlow](https://siliconflow.cn)

### Steps

```bash
# 1. Clone
git clone https://github.com/GunGunLin/luckie-bot.git
cd luckie-bot

# 2. Install
pip install websockets pyserial

# 3. Start bridge
cd bridge && python server.py

# 4. Open http://localhost:8080
#    Enter your SiliconFlow API key in Settings ⚙️
```

To use the hardware device, flash `firmware/main.py` to your M5StickC Plus via [Thonny](https://thonny.org/) or M5Burner.

---

## 📂 Project Structure

```
luckie-bot/
├── web/index.html          # SPA frontend (vanilla JS, zero dependencies)
│   └── assets/cards/       # 78 tarot card images
├── bridge/server.py        # WebSocket ↔ Serial relay (Python asyncio)
├── firmware/main.py        # M5StickC Plus firmware (MicroPython)
├── hardware/               # Reference photos
└── docs/                   # Logo, screenshots
```

---

## 💼 Why This Works as a Business

| | |
|---|---|
| **Problem** | Gen Z wellness seekers want personalized spiritual experiences, but existing apps are generic and screen-only |
| **Solution** | AI personalization + physical companion device = an experience that feels real |
| **Moat** | Hardware-software integration creates a barrier pure apps can't cross |
| **Model** | Device sale ($49–79) + premium subscription ($4.99/mo) for unlimited readings |

---

## 🛠️ Built With

`DeepSeek-V3` `MediaPipe Hands` `Python asyncio` `WebSocket` `MicroPython` `ESP32` `Canvas 2D` `CSS 3D` `SK6812 LED`

---

<div align="center">

<br>

**🏆 ENT 208 Demo Day Champion · XJTLU**

*Made with ❤️ by Group 20*

</div>
