<div align="center">

<br>

<img src="docs/logo.svg" width="96" alt="Arcanum Lab">

<br>

# Luckie-Bot

### *The AI Companion That Lives in Your Hands*

<br>

[![Demo Day](https://img.shields.io/badge/🏆_Demo_Day_Champion-ENTE_208-gold?style=for-the-badge&labelColor=0d0d1e&color=d4af37)]()
[![DeepSeek](https://img.shields.io/badge/AI-DeepSeek_V3-6a5acd?style=for-the-badge&labelColor=0d0d1e)]()
[![MediaPipe](https://img.shields.io/badge/CV-MediaPipe_Hands-00ccff?style=for-the-badge&labelColor=0d0d1e)]()
[![Python](https://img.shields.io/badge/Python-3.10+-3776ab?style=for-the-badge&labelColor=0d0d1e)]()
[![License](https://img.shields.io/badge/License-MIT-2ea44f?style=for-the-badge&labelColor=0d0d1e)]()

<br>
<br>

<p>
  <img src="docs/screenshots/ui-demo.gif" width="80%" alt="Product Demo">
</p>

### Fortune-Telling Meets Generative AI · Gesture-Powered · Hardware-Synchronized

</div>

<br>

---

## The Product

Luckie-Bot is a **tangible AI experience**. Pick a life category, draw three tarot cards through hand gestures in the air, and receive a personalized oracle reading generated in real time by DeepSeek-V3 — while a physical companion device on your desk breathes with light, displays facial expressions, and responds to every moment.

**It's a tarot reading. It's an AI companion. It's a living ecosystem that grows with you.**

<br>

<p align="center">
  <img src="docs/screenshots/user-testing.png" width="75%" alt="Real user testing Luckie-Bot">
</p>

<br>

---

## ✨ Why Luckie-Bot?

<table>
<tr>
<td width="50%">

### 🎴 AI That Reads You
Not canned horoscopes. DeepSeek-V3 crafts unique, poetic interpretations for every draw — across **Wealth**, **Study**, **Love**, and **General** life categories. Each reading is a one-of-a-kind AI generation.

### ✋ Touch the Invisible
Google MediaPipe tracks 21 hand landmarks at 30fps. **Pinch** to select. **Palm** to invoke. **Fist** to confirm. No mouse. No keyboard. Pure ritual.

### 💡 Light You Can Feel
The M5StickC Plus hardware companion reacts in real time. **6 LED modes** (Breath, Pulse, Rainbow, Warm, Static, Off). **7 facial expressions**. Built-in buzzer tones. Software isn't intangible anymore.

</td>
<td width="50%">

### 🌱 A Garden That Grows With You
Every divination feeds your Psionic Garden. **5 growth stages** — from Seed to Cosmic Tree — across sessions. This isn't a progress bar. It's a living record of your journey with the AI.

<p align="center">
  <img src="docs/screenshots/garden-growth.gif" width="90%" alt="Garden Growth">
</p>

### 🧘 Breathe Before You Believe
A guided breathing orb with particle absorption effects precedes every reading. 12 seconds of calm. Hardware-synchronized LED breathing. The perfect ritual before the AI speaks.

</td>
</tr>
</table>

<br>

---

## 🏆 Proven. Not Hypothetical.

<p align="center">
  <img src="docs/screenshots/demo-day-01.jpg" width="45%">
  &nbsp;&nbsp;
  <img src="docs/screenshots/demo-day-02.jpg" width="45%">
</p>

<br>

| | |
|---|---|
| 🥇 | **First Place** at XJTLU ENT 208 Demo Day |
| 🎤 | Live demo with real-time AI + gesture + hardware sync — zero failures |
| 🗣️ | Judge verdict: *"This isn't a course project — it's an investable MVP."* |

<br>

---

## 🏗️ Under the Hood

```
┌─────────────────────────────────────────────────────────────┐
│  Browser                    Bridge                    Device │
│  ┌──────────┐    WS     ┌──────────┐   Serial   ┌──────────┐│
│  │ Gesture  │◄─────────►│ asyncio  │◄──────────►│ LED LCD  ││
│  │ AI Call  │           │ Router   │           │ Face Btn ││
│  │ Render   │           │ HTTP     │           │ Buzzer   ││
│  └──────────┘           └──────────┘           └──────────┘│
│       │                                                    │
│       ▼ HTTPS                                              │
│  ┌──────────┐                                              │
│  │DeepSeek  │                                              │
│  │V3 (671B) │                                              │
│  └──────────┘                                              │
└─────────────────────────────────────────────────────────────┘
```

**Three clean layers. One seamless experience.** The browser handles AI + vision + rendering. The Python bridge relays commands in under 20ms. The hardware provides feedback you can see and feel.

<br>

| | |
|---|---|
| 🖥️ **Frontend** | `Vanilla JS` `Canvas 2D` `CSS 3D` `MediaPipe WASM` — zero framework, 60fps |
| 🌉 **Bridge** | `Python` `asyncio` `WebSocket` `pyserial` — multi-client, non-blocking |
| 🔌 **Firmware** | `MicroPython` `ESP32 RMT` `SK6812` — 7 dynamic faces, 6 LED modes |

<br>

---

## 🚀 One Command to Run

```bash
git clone https://github.com/GunGunLin/luckie-bot.git && cd luckie-bot
pip install websockets pyserial
cd bridge && python server.py
```

**Open `http://localhost:8080`** — enter your free [SiliconFlow](https://siliconflow.cn) API key — done.

> The web app works standalone. Flash `firmware/main.py` to M5StickC Plus only when you want the hardware companion.

<br>

---

## 📂 Repository

```
luckie-bot/
├── web/
│   ├── index.html          ← The entire SPA in one file
│   └── assets/cards/       ← 78 tarot card illustrations
├── bridge/
│   └── server.py           ← WebSocket ⟷ Serial relay
├── firmware/
│   └── main.py             ← M5StickC Plus MicroPython
├── hardware/               ← Device photos
└── docs/                   ← Demos, screenshots
```

<br>

---

## 💼 The Business Case

> Gen Z is spending $2.1B/year on spiritual wellness. But every product is either a generic app or a paper deck. **No one has bridged the physical-digital gap. Until now.**

| Tier | Price | Includes |
|------|-------|----------|
| **Device** | `$49–79` | M5StickC Plus + SK6812 LED strip |
| **Premium** | `$4.99/mo` | Unlimited AI readings, advanced card spreads, custom companion skins |
| **Deluxe** | `$129` | Device + 1yr premium + limited-edition physical tarot deck + case |

**Moat:** Hardware-software integration creates a barrier pure apps cannot cross. The device, the garden, the rituals — they compound into an ecosystem, not a feature list.

<br>

---

<div align="center">

<br>

<img src="docs/logo.svg" width="48" alt="Arcanum Lab">

### Arcanum Lab · XJTLU ENT 208

**🥇 Demo Day Champion**

</div>
