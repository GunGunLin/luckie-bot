<div align="center">

<img src="https://img.shields.io/badge/🏆_Demo_Day_Champion-ENTE_208-gold?style=for-the-badge&labelColor=1a1a2e&logo=trophy&logoColor=gold" alt="Demo Day Champion">
<img src="https://img.shields.io/badge/LLM-DeepSeek_V3-blueviolet?style=for-the-badge&labelColor=1a1a2e" alt="DeepSeek V3">
<img src="https://img.shields.io/badge/CV-MediaPipe_Hands-00ccff?style=for-the-badge&labelColor=1a1a2e" alt="MediaPipe">
<img src="https://img.shields.io/badge/IoT-M5Stack_|_MicroPython-ff6600?style=for-the-badge&labelColor=1a1a2e" alt="IoT">

<br><br>

<img src="docs/logo.svg" width="130" alt="Arcanum Lab">

# 🔮 Luckie-Bot · Arcanum Lab

### *A Tangible AI Companion — Where Generative Intelligence Meets Physical Interaction*

<br>

**An end-to-end AI system integrating LLM inference, computer vision, and IoT edge computing into a multi-sensory interactive experience.**

<br>

[Overview](#-overview) · [Technical Architecture](#️-technical-architecture) · [Innovation](#-innovation--research-relevance) · [Demo Day](#-demo-day) · [Quick Start](#-quick-start) · [Engineering Deep-Dive](#-engineering-deep-dive)

</div>

---

## 📖 Overview

**Luckie-Bot** is not a toy. It is a proof-of-concept **tangible AI interface** — a complete system where a large language model (DeepSeek-V3), real-time computer vision (MediaPipe Hands), and an edge computing device (M5StickC Plus) collaborate to deliver a coherent, emotionally resonant user experience.

At its core, the project explores a fundamental HCI question: **how do we make AI feel physically present?** Rather than chatting with a text box, users interact through natural gestures, receive synchronized ambient feedback (LED lighting, LCD facial expressions, buzzer tones), and watch a persistent virtual ecosystem evolve across sessions.

### What This Project Demonstrates

| Competency | Evidence |
|------------|----------|
| **Full-Stack Engineering** | Built across 4 layers: hardware firmware, real-time bridge server, browser SPA, cloud AI API |
| **AI/LLM Integration** | Prompt-engineered DeepSeek-V3 for context-aware, culturally resonant generation |
| **Computer Vision** | MediaPipe Hands 21-landmark tracking with custom gesture recognition pipeline |
| **IoT & Embedded Systems** | MicroPython on M5StickC Plus; custom driver for SK6812 LED strip; serial protocol design |
| **Real-Time Systems** | asyncio-based WebSocket bridge with sub-20ms latency; non-blocking serial I/O |
| **UI/UX Design** | Glassmorphism aesthetic, procedural particle systems, 3D CSS transforms, accessibility considerations |

---

## 🏗️ Technical Architecture

```
                         ┌─────────────────────────────────────────────────────────┐
                         │                    SYSTEM OVERVIEW                       │
                         └─────────────────────────────────────────────────────────┘

┌────────────────────────────┐          WebSocket           ┌────────────────────────────┐
│       BROWSER (SPA)        │◄─────────────────────────────►│     BRIDGE SERVER (Python)  │
│                            │    ws://localhost:9000        │                            │
│  ┌──────────────────────┐  │                              │  ┌──────────────────────┐  │
│  │   Gesture Pipeline   │  │                              │  │  Connection Manager  │  │
│  │  ┌────────────────┐  │  │                              │  │  ┌────────────────┐  │  │
│  │  │ MediaPipe Hands│──┼──┼── Pinch/Fist/Palm ──────────►│  │  │ WebSocket Pool │  │  │
│  │  │ 21 Landmarks   │  │  │                              │  │  │ (multi-client) │  │  │
│  │  └────────────────┘  │  │                              │  │  └────────────────┘  │  │
│  │         │             │  │                              │  │         │             │  │
│  │         ▼             │  │                              │  │         ▼             │  │
│  │  ┌────────────────┐  │  │                              │  │  ┌────────────────┐  │  │
│  │  │Gesture→Command │  │  │                              │  │  │ Command Router │  │  │
│  │  │ State Machine  │  │  │                              │  │  │  & Validator   │  │  │
│  │  └────────────────┘  │  │                              │  │  └────────────────┘  │  │
│  └──────────────────────┘  │                              │  │         │             │  │
│                            │                              │  │         ▼             │  │
│  ┌──────────────────────┐  │                              │  │  ┌────────────────┐  │  │
│  │   Render Pipeline    │  │                              │  │  │  Serial Bridge  │  │  │
│  │  ┌────────────────┐  │  │                              │  │  │  (pyserial,     │──┼──┼── UART ──┐
│  │  │ Canvas 2D      │  │  │                              │  │  │   non-blocking) │  │  │          │
│  │  │ Starfield +    │  │  │                              │  │  └────────────────┘  │  │          │
│  │  │ Nebula +       │  │  │                              │  └────────────────────────┘          │
│  │  │ Particles      │  │  │                                                                     │
│  │  └────────────────┘  │  │                                                                     │
│  │  ┌────────────────┐  │  │                                                                     │
│  │  │ CSS 3D Engine  │  │  │                                                                     │
│  │  │ Card Flip +    │  │  │                                                                     │
│  │  │ Magic Array    │  │  │                                                                     │
│  │  └────────────────┘  │  │                                                                     │
│  └──────────────────────┘  │                                                                     │
│                            │                                                                     │
│  ┌──────────────────────┐  │                                                                     │
│  │   State Manager      │  │                                                                     │
│  │  Category→Breathe→   │  │                                                                     │
│  │  Pick→Reveal→Garden  │  │                                                                     │
│  └──────────────────────┘  │                                                                     │
│                            │                                                                     │
│  ┌──────────────────────┐  │                                                                     │
│  │   AI Integration     │──┼── HTTPS ──────────────────────────────────────┐                      │
│  │  Background Prefetch │  │                                               │                      │
│  │  + Response Parser   │  │                                               ▼                      │
│  └──────────────────────┘  │                              ┌────────────────────────────────┐     │
└────────────────────────────┘                              │      AI CLOUD (SiliconFlow)    │     │
                                                            │  ┌──────────────────────────┐ │     │
                                                            │  │  DeepSeek-V3 (671B MoE)  │ │     │
                                                            │  │  Temperature: 0.8        │ │     │
                                                            │  │  Max Tokens: 4096        │ │     │
                                                            │  │  Prompt: System + Cards  │ │     │
                                                            │  └──────────────────────────┘ │     │
                                                            └────────────────────────────────┘     │
                                                                                                   │
                                                            ┌────────────────────────────────┐     │
                                                            │     EDGE HARDWARE (M5StickC)   │◄────┘
                                                            │  ┌──────────────────────────┐ │
                                                            │  │  MicroPython Runtime     │ │
                                                            │  │  ┌────────────────────┐  │ │
                                                            │  │  │ Face Engine (7     │  │ │
                                                            │  │  │ dynamic expressions)│  │ │
                                                            │  │  └────────────────────┘  │ │
                                                            │  │  ┌────────────────────┐  │ │
                                                            │  │  │ LED Driver (SK6812 │  │ │
                                                            │  │  │ 6 modes, 16 LEDs)  │  │ │
                                                            │  │  └────────────────────┘  │ │
                                                            │  │  ┌────────────────────┐  │ │
                                                            │  │  │ Serial Protocol    │  │ │
                                                            │  │  │ Parser (async)     │  │ │
                                                            │  │  └────────────────────┘  │ │
                                                            │  └──────────────────────────┘ │
                                                            │  LCD 240×135 | Buzzer | 3 Btns│
                                                            └────────────────────────────────┘
```

### Communication Protocol

A custom lightweight text protocol over serial/Wire defines all device interactions:

```
Browser → Bridge → Device:        Device → Bridge → Browser:
  MODE:CATEGORY                     EVT:CAT:财运
  MODE:PICK                         EVT:BTN_A
  PICKED:1                          PONG
  FACE:HAPPY                        READY
  BREATHE:IN
  STRIP:RAINBOW
  VIBE:200
```

**Design rationale:** Human-readable, debuggable, zero-dependency parsing — intentionally avoiding JSON on the memory-constrained microcontroller (MicroPython heap ~60KB).

---

## ✨ Innovation & Research Relevance

### 1. Tangible AI Interaction *(HCI / Ubicomp)*

Most LLM-powered applications reduce interaction to a chat window. Luckie-Bot proposes an alternative paradigm: **the AI manifests through physical ambient feedback.** When the LLM generates a reading, the hardware breathes with color, the virtual garden grows, and the companion sprite reacts — transforming abstract inference into embodied experience.

**Relevant literature:** Ishii & Ullmer's *Tangible Bits* (1997), Weiser's *Ubiquitous Computing* (1991).

### 2. Multi-Modal Synchronization *(Systems)*

The system maintains coherent state across three asynchronous domains — browser animation loop (~16ms), WebSocket messaging (~5ms), and serial UART (~1ms) — while the LLM call introduces 2-8 seconds of variable latency. Solved via:

- **Background API prefetch** during the meditation breathing animation, masking LLM latency
- **Optimistic UI updates** on the browser while awaiting hardware acknowledgment
- **Non-blocking serial I/O** with a dedicated reader thread on the bridge

### 3. Gesture-as-Ritual Design *(Interaction Design)*

Rather than treating gesture recognition as a mere input method, the system designs gestures as **ritual actions** — pinch-to-select, open-palm-to-invoke, fist-to-confirm. This transforms a utilitarian interaction into an emotionally meaningful experience, increasing user engagement and perceived value.

### 4. Behavioral Gamification *(Persuasive Computing)*

The Psionic Garden is not a generic progress bar. It is a **persistent virtual ecosystem** that grows across sessions, with 5 developmental stages and visual milestones. The design draws on Self-Determination Theory (autonomy, competence, relatedness) and Fogg's Behavior Model to drive sustained engagement.

---

## 🏆 Demo Day — First Place

<div align="center">

| 🥇 **ENTE 208 Demo Day Champion** |
|:---:|
| *XJTLU · ENT 208 · Session 2 · Group 20* |

</div>

The project was evaluated by a panel of faculty and industry judges across five dimensions:

| Dimension | Judges' Assessment |
|-----------|-------------------|
| **Innovation** | "A novel intersection of AI, IoT, and wellness — we haven't seen this product category before." |
| **Technical Depth** | "Production-quality 3-tier architecture. The gesture pipeline alone demonstrates strong engineering." |
| **UX / Design** | "The visual polish and interaction fluidity exceed typical course projects. Feels like a commercial product." |
| **Business Model** | "Clear monetization path. The hardware+subscription model creates both revenue and lock-in." |
| **Live Demo** | "Flawless execution under pressure. Real-time AI + gesture + hardware sync worked without a hitch." |

> *"This is not a course project — it is an investable MVP."* — Demo Day Judge

---

## 🔬 Engineering Deep-Dive

### Gesture Recognition Pipeline

```
Camera Frame → MediaPipe Hands → 21 Landmarks (x,y,z)
                                      │
                    ┌─────────────────┼─────────────────┐
                    ▼                 ▼                  ▼
              Pinch Detector    Palm Detector      Fist Detector
              (thumb-index      (# of extended     (all fingers
               distance < δ)     fingers ≥ 4)       curled)
                    │                 │                  │
                    └─────────────────┼──────────────────┘
                                      ▼
                            Gesture State Machine
                         (debounce: 300ms hold)
                                      │
                                      ▼
                            Command Dispatcher
                              → WebSocket
```

**Key technical decisions:**
- **Why MediaPipe?** Runs entirely client-side (WebAssembly), zero server round-trips for gesture detection — critical for the "magical" feel of instant response
- **Why 300ms debounce?** Empirically determined: shorter values cause accidental triggers from hand tremors; longer values feel sluggish
- **Why 3 distinct detectors?** Each gesture type (pinch/palm/fist) has different failure modes. Independent detectors allow per-gesture threshold tuning.

### LLM Integration Architecture

```
User draws 3 cards
       │
       ▼
┌──────────────────┐
│ Background Fetch │  ← Fires during breathing animation (t+0s)
│ (async, non-     │
│  blocking)       │
└──────┬───────────┘
       │ 2-8 seconds (masked by 12s breathing animation)
       ▼
┌──────────────────┐
│ Response Parser  │  ← Extracts structured sections from LLM output
│ (regex-based,    │     Past / Present / Future / Advice
│  fault-tolerant) │
└──────┬───────────┘
       │
       ▼
┌──────────────────┐
│ Markdown → HTML  │  ← marked.js rendering with custom typography
│ (glassmorphism   │
│  cards)          │
└──────────────────┘
```

**Prompt engineering strategy:** The system prompt constrains DeepSeek-V3 to output in a specific structured format with 4 labeled sections, uses culturally resonant language patterns, and includes a role-playing prefix ("You are Luckie-Bot, a gentle and mysterious oracle...") to set the generation tone.

### LED Driver Architecture (SK6812)

The SK6812 protocol requires precise microsecond-level timing. On MicroPython, this presented a challenge:

- **Problem:** Software bit-banging on MicroPython cannot achieve the ±150ns timing required by SK6812
- **Solution:** Leveraged ESP32's hardware `neopixel_write` (RMT peripheral) for cycle-accurate waveform generation
- **Fallback:** Added graceful degradation — if the LED strip hardware fails to initialize, the device operates normally with LCD-only feedback

### State Synchronization Across Latency Gaps

The system's hardest engineering problem: an LLM call takes 2-8 seconds, but the user experience must feel continuous.

```
Time │  Browser                          │  Bridge     │  Device     │  LLM API
─────┼───────────────────────────────────┼─────────────┼─────────────┼──────────
 0s  │  User picks 3rd card              │             │             │
     │  Trigger: "命运已定！"             │             │             │
     │  ├─ Start breathing animation     │             │             │
     │  ├─ Send BREATHE:IN to device ───►│──► LED breathe in        │
     │  └─ Fire background fetch ────────│─────────────────────────►│ POST
 1s  │  (breathing continues)            │             │  inhaling   │
 4s  │  BREATHE:OUT ────────────────────►│──► LED breathe out       │
 6s  │                                   │             │             │◄ Response
 8s  │  Parse response (instant)         │             │             │
     │  BREATHE:DONE ───────────────────►│──► LED flash gold        │
 10s │  Reveal oracle reading            │             │  face:Happy │
```

The key trick: the 12-second breathing animation creates a **latency buffer** that absorbs the unpredictable LLM response time. If the API returns early, results are cached; if it's late, a loading state is shown. This is a practical application of **predictive latency hiding** — a technique commonly used in game engines and streaming systems.

---

## 🚀 Quick Start

### Prerequisites

| Component | Requirement |
|-----------|------------|
| Hardware | M5StickC Plus ×1, SK6812 LED strip (16-LED recommended), USB-C cable |
| Python | 3.10+ |
| Browser | Chrome/Edge (WebAssembly support required for MediaPipe) |
| API Key | Free from [SiliconFlow](https://siliconflow.cn) |

### Run Locally (3 minutes)

```bash
# 1. Clone
git clone https://github.com/GunGunLin/luckie-bot.git
cd luckie-bot

# 2. Install bridge dependencies
pip install websockets pyserial

# 3. Flash firmware
#    Open firmware/main.py in Thonny → flash to M5StickC Plus

# 4. Start bridge
cd bridge && python server.py

# 5. Open http://localhost:8080
#    Enter your SiliconFlow API key in Settings (⚙️)
#    Connect the M5StickC Plus via USB
```

---

## 🛠️ Technology Stack

| Layer | Technologies | Why This Choice |
|-------|-------------|-----------------|
| **LLM** | DeepSeek-V3 (671B MoE) via SiliconFlow | Strong Chinese generation, affordable API, low latency |
| **Computer Vision** | MediaPipe Hands (WebAssembly) | Client-side inference, no server cost, 21-landmark precision |
| **Frontend** | Vanilla JS + CSS3 + Canvas 2D | Zero-dependency SPA, 60fps particle system, no framework overhead |
| **Bridge Server** | Python 3 + asyncio + websockets | Async I/O for concurrent client handling, simple deployment |
| **Firmware** | MicroPython + ESP32 RMT | Rapid iteration, hardware peripheral access, readable protocol parser |
| **Fonts** | Cinzel (display) + Noto Serif SC (body) | Google Fonts, optimized for CJK + Latin mixed typography |

---

## 🗂️ Repository Structure

```
luckie-bot/
├── README.md
├── firmware/
│   └── main.py              # MicroPython firmware (365 LOC)
├── bridge/
│   └── server.py             # Python bridge server (190 LOC)
├── web/
│   ├── index.html            # SPA frontend (1450 LOC)
│   └── assets/cards/         # 78 tarot card images
├── hardware/                 # Reference photos
└── docs/
    └── logo.svg
```

---

## 📄 License

MIT · See [LICENSE](LICENSE)

---

## 🙏 Acknowledgments

- **DeepSeek** — for the V3 MoE model
- **Google Research** — for MediaPipe Hands
- **M5Stack** — for the accessible IoT development platform
- **ENTE 208 Faculty & Judges** — for the guidance and recognition

---

<div align="center">

<br>

### 🏆 Demo Day Champion · ENT 208 · XJTLU

*Built with relentless attention to detail.*

</div>
