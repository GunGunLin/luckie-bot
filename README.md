<div align="center">

<img src="https://img.shields.io/badge/🏆-Demo_Day_Champion-gold?style=for-the-badge&labelColor=1a1a2e" alt="Demo Day Champion">
<img src="https://img.shields.io/badge/AI_Powered-DeepSeek_V3-blueviolet?style=for-the-badge&labelColor=1a1a2e" alt="DeepSeek V3">
<img src="https://img.shields.io/badge/Made_with-Python_|_MicroPython_|_MediaPipe-00ccff?style=for-the-badge&labelColor=1a1a2e" alt="Tech Stack">

<br><br>

<img src="docs/logo.svg" width="120" alt="Arcanum Lab">

# 🔮 Luckie-Bot · Arcanum Lab

### *Where Ancient Wisdom Meets Artificial Intelligence*

<br>

**An AI-powered mystical companion that blends tarot divination, gesture recognition, and IoT hardware into a magical wellness experience.**

<br>

[Overview](#-overview) · [Architecture](#️-architecture) · [Features](#-features) · [Demo Day](#-demo-day) · [Getting Started](#-getting-started) · [Business Logic](#-business-logic)

</div>

---

## 📖 Overview

**Luckie-Bot** is an AI-driven interactive companion system that reimagines tarot reading for the digital age. It combines:

- 🤖 **Generative AI** (DeepSeek-V3 via SiliconFlow) for personalized, context-aware tarot readings
- ✋ **Computer Vision** (Google MediaPipe Hands) for touchless gesture interaction
- 🔌 **Edge Hardware** (M5StickC Plus + SK6812 LED strip) for tangible, ambient feedback
- 🌐 **Real-time Bridge** (Python WebSocket ↔ Serial) connecting all layers seamlessly

Users select a divination category, draw virtual tarot cards through hand gestures, receive AI-generated oracle interpretations, and watch their **Psionic Garden** grow — all while the physical companion device responds with dynamic lighting and facial expressions in real time.

> **Note:** While the product concept is positioned in the mystical/spiritual wellness market, all "AI divination" is presented as an entertainment-experience product. The underlying technology stack is real and production-grade.

---

## 🏗️ Architecture

```
┌──────────────────────┐        WebSocket         ┌────────────────────┐        Serial         ┌──────────────────────┐
│                      │◄─────────────────────────►│                    │◄──────────────────────►│                      │
│    Web Frontend      │                           │   Bridge Server    │                        │   Edge Hardware      │
│                      │                           │                    │                        │                      │
│  • HTML5/CSS3/JS     │                           │  • Python 3        │                        │  • M5StickC Plus     │
│  • MediaPipe Hands   │                           │  • asyncio         │                        │  • MicroPython       │
│  • Canvas 2D Effects │                           │  • websockets      │                        │  • SK6812 LED Strip  │
│  • 3D Card Flip      │                           │  • pyserial        │                        │  • LCD 240×135       │
│  • Glassmorphism UI  │                           │  • HTTP Server     │                        │  • Physical Buttons  │
│                      │                           │                    │                        │                      │
└─────────┬────────────┘                           └────────────────────┘                        └──────────────────────┘
          │
          │ HTTPS
          ▼
┌──────────────────────┐
│   AI Cloud API       │
│                      │
│  • DeepSeek-V3       │
│  • SiliconFlow       │
│  • Prompt Engineering│
│                      │
└──────────────────────┘
```

### Data Flow

1. **User** selects tarot category (Wealth / Study / Love / General) via web UI or hardware buttons
2. **MediaPipe Hands** tracks gestures → triggers card draw animation via WebSocket
3. **Bridge Server** relays commands between browser and M5Stack device
4. **DeepSeek-V3** generates a personalized oracle reading based on the drawn cards
5. **Hardware** responds with synchronized LED breathing patterns, sound tones, and LCD facial expressions
6. **Psionic Garden** grows as users accumulate divination sessions (gamification)

---

## ✨ Features

### 🎴 AI-Powered Tarot Divination
- **4 Categories:** 💰 Wealth (财运) · 📚 Study (学业) · 💕 Love (情感) · 🌟 General (综合)
- 3-card spreads with AI interpretation via DeepSeek-V3
- Background API prefetch during meditation animation (sub-second response)
- Readings presented in elegant, poetic Chinese with mystic aesthetics

### ✋ Gesture Recognition (Touchless)
- Real-time hand tracking with **Google MediaPipe Hands** (21 landmarks)
- Pinch-to-select, open-palm-to-draw, fist-to-confirm gestures
- Visual feedback: floating particles, magic dot following fingertip
- No mouse or keyboard needed during the ritual

### 🧚 AI Companion Sprite
- Animated mascot with contextual dialogue bubbles
- Support for **custom image upload** as your personal companion
- Emotion overlay system reacting to divination results
- Float animation, hover effects

### 🌱 Psionic Garden (Gamification)
- **Plant growth system** tied to divination frequency
- 5 growth stages: Seed → Sprout → Budding → Blooming → Cosmic Tree
- Progress bar with stage milestones and star-dust point accumulation
- Visualizes user engagement and retention as a living ecosystem

### 🧘 Energy Meditation Mode
- Guided breathing orb with inhale/exhale cycles
- Absorbing particle effects during inhalation
- Hardware-synced LED breathing light on the M5Stack device
- Calming transition to oracle revelation

### 💡 Hardware Companion (M5StickC Plus)
- **Dynamic LED strip** with 6 modes: Breath, Pulse, Rainbow, Warm, Static, Off
- **7 facial expressions:** Idle, Awake, Thinking, Happy, Love, Breathe In, Breathe Out
- Physical button input for standalone operation
- Buzzer tones for multi-sensory feedback

### 🌌 Visual Atmosphere
- Procedural starfield background with parallax nebula
- Glassmorphism panels with animated light sweeps
- 3D card flip animations (CSS 3D transforms)
- Magic circle array with rotating runes
- Particle system for card selection

---

## 🏆 Demo Day

<div align="center">

### 🥇 **First Place — ENTE 208 Demo Day**

</div>

**Luckie-Bot** won the championship at the ENTE 208 course Demo Day, evaluated on:

| Dimension | Assessment |
|-----------|-----------|
| **Innovation** | Fusion of AI, IoT, and spiritual wellness — a novel product category |
| **Technical Depth** | 3-layer architecture spanning edge hardware, real-time bridge, and cloud AI |
| **User Experience** | Immersive multi-sensory interaction with fluid animations and tangible feedback |
| **Business Viability** | Clear target market, revenue model, and competitive moat |
| **Presentation** | Live demo with hardware device, real-time AI readings, and gesture interaction |

> *"This isn't just a class project — it's an investable MVP."* — Demo Day Judge

---

## 📸 Screenshots

*[Screenshots coming soon]*

| Scene | Description |
|-------|-------------|
| **Category Selection** | 4 mystical cards for Wealth, Study, Love, General |
| **Card Drawing** | 3-tarot-card spread with gesture-controlled interaction |
| **AI Oracle** | AI-generated reading with elegant typography |
| **Psionic Garden** | Plant growth visualization with progression stages |
| **Meditation Orb** | Breathing guide with particle effects |
| **Hardware Device** | M5StickC Plus with LED strip and LCD face |

---

## 🚀 Getting Started

### Prerequisites

- **Hardware:** M5StickC Plus, SK6812 LED strip (16 LEDs), USB-C cable
- **Software:** Python 3.10+, a modern browser (Chrome/Edge recommended)
- **API Key:** [SiliconFlow](https://siliconflow.cn) API key (free tier available)

### Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/luckie-bot.git
cd luckie-bot

# 2. Install bridge server dependencies
cd bridge
pip install websockets pyserial

# 3. Flash the firmware to M5StickC Plus
#    Open firmware/main.py in Thonny or M5Burner
#    Flash to your M5StickC Plus device

# 4. Start the bridge server
python server.py
# Output: 
#   WebSocket 服务: ws://localhost:9000
#   HTTP 服务: http://localhost:8080

# 5. Open the web app
#    Visit http://localhost:8080 in your browser
#    (The bridge server serves index.html automatically)
```

### Configuration

1. Replace `YOUR_SILICONFLOW_API_KEY` in `web/index.html` with your actual API key
2. Adjust `SERIAL_PORT` in `bridge/server.py` if auto-detection fails
3. Customize `NUM_LEDS` in `firmware/main.py` to match your LED strip

---

## 💼 Business Logic

### Problem
Modern urbanites face rising anxiety and uncertainty. The global wellness market ($6.3T) and spiritual services market ($2.1B) are growing rapidly, but digital solutions remain superficial — generic horoscope apps with no personalization, no tangible feedback, and no emotional connection.

### Solution
**Luckie-Bot** bridges the physical-digital divide in spiritual wellness:

- **AI Personalization:** DeepSeek-V3 generates unique, context-aware readings for each session — not canned responses
- **Tangible Hardware:** The physical companion device provides real-world feedback (light, sound, display) that a screen-only app cannot
- **Gesture Ritual:** Hand tracking creates a ceremonial, immersive experience that feels "magical" — increasing perceived value and user stickiness
- **Gamified Retention:** The Psionic Garden turns repeat usage into a growth journey, driving DAU/MAU

### Target Market
- Gen Z & Millennials interested in spirituality, astrology, and wellness
- Tech-savvy consumers seeking unique gadgets
- Gift market (aesthetic packaging, mystical branding)

### Revenue Model

| Tier | Price | Value |
|------|-------|-------|
| **Device** | $49-79 | M5StickC Plus + LED strip + enclosure |
| **Free Tier** | $0 | 1 reading/day, basic garden |
| **Premium** | $4.99/mo | Unlimited readings, advanced spreads, custom companion skins |
| **Deluxe Kit** | $129 | Device + 1 year premium + tarot card deck + packaging |

### Competitive Moat
- **Hardware + AI integration** — no pure-software competitor can replicate the tangible experience
- **Proprietary prompt engineering** — tuned for culturally resonant Chinese oracle readings
- **Gesture interaction IP** — MediaPipe pipeline optimized for divination ritual UX
- **Garden gamification** — patent-pending engagement loop

---

## 🗂️ Project Structure

```
luckie-bot/
├── README.md                    # This file
├── LICENSE                      # MIT License
├── .gitignore
├── firmware/
│   └── main.py                  # M5StickC Plus MicroPython firmware
├── bridge/
│   └── server.py                # WebSocket ↔ Serial bridge server
├── web/
│   ├── index.html               # Main web application (SPA)
│   └── assets/
│       └── cards/               # 78 Tarot card face images
├── hardware/
│   └── *.png                    # Hardware reference photos
└── docs/
    └── (architecture diagrams, screenshots)
```

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **AI/LLM** | DeepSeek-V3 (via SiliconFlow) | Oracle text generation |
| **Computer Vision** | MediaPipe Hands | Real-time gesture recognition |
| **Frontend** | Vanilla HTML5/CSS3/JavaScript | SPA with glassmorphism UI |
| **Backend Bridge** | Python 3 + asyncio + websockets | WebSocket-Serial relay |
| **Hardware** | MicroPython + M5Stack | Edge device with LED/LCD/buttons |
| **Effects** | Canvas 2D API | Starfield, particles, nebula |
| **Font** | Cinzel + Noto Serif SC | Mystic typography |

---

## 👥 Team

| Role | Member |
|------|--------|
| Product Lead & Hardware | — |
| AI & Full-Stack | — |
| Design & UX | — |
| Business Strategy | — |

*Team members from CUHK ENTE 208, Session 2, Group 20.*

---

## 📄 License

This project is licensed under the **MIT License** — see [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgments

- **DeepSeek** for the V3 language model
- **SiliconFlow** for affordable LLM API access
- **Google MediaPipe** for the hand tracking framework
- **M5Stack** for the fantastic IoT hardware platform
- **ENTE 208 Faculty** for the entrepreneurship guidance

---

<div align="center">

<br>

### 🏆 Demo Day Champion | ENTE 208 | CUHK

*Built with ❤️ by Group 20, Session 2*

</div>
