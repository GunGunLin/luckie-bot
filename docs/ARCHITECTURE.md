# Architecture — Twelfth Night

## System Overview

Twelfth Night implements a three-layer architecture that connects gesture-based user interaction, LLM-powered response generation, and hardware-synchronised feedback into a single real-time experience.

```
┌──────────────────────────────────────────────────────────┐
│                     LAYER 1: BROWSER                      │
│                                                          │
│  ┌─────────────┐  ┌──────────────┐  ┌────────────────┐  │
│  │ MediaPipe   │  │ LLM Response  │  │ Visual Render  │  │
│  │ Hand Track  │  │ Generator     │  │ Pipeline       │  │
│  │ (WASM)      │  │ (fetch API)   │  │ (Canvas + CSS) │  │
│  └──────┬──────┘  └──────┬───────┘  └───────┬────────┘  │
│         │                │                   │           │
│         └────────────────┼───────────────────┘           │
│                          │                               │
│                   WebSocket Client                       │
└──────────────────────────┬───────────────────────────────┘
                           │ ws://localhost:9000
                           │
┌──────────────────────────┴───────────────────────────────┐
│                     LAYER 2: BRIDGE                       │
│                                                          │
│  ┌─────────────┐  ┌──────────────┐  ┌────────────────┐  │
│  │ WebSocket   │  │ Command      │  │ Serial Bridge  │  │
│  │ Server      │──│ Router       │──│ (pyserial)     │  │
│  │ (asyncio)   │  │ & Validator  │  │                │  │
│  └─────────────┘  └──────────────┘  └───────┬────────┘  │
│                                              │           │
│                                        UART / USB        │
└──────────────────────────────────────────────┬───────────┘
                                               │
┌──────────────────────────────────────────────┴───────────┐
│                     LAYER 3: DEVICE                       │
│                                                          │
│  ┌─────────────┐  ┌──────────────┐  ┌────────────────┐  │
│  │ LED Driver  │  │ Face Engine  │  │ Serial Parser  │  │
│  │ (SK6812)    │  │ (7 modes)    │  │ (non-blocking) │  │
│  │ 6 modes     │  │ LCD 240×135  │  │                │  │
│  └─────────────┘  └──────────────┘  └────────┬───────┘  │
│                                              │           │
│                           ┌──────────────────┘           │
│                           │                              │
│                    Buzzer / Audio                        │
└──────────────────────────────────────────────────────────┘
```

## Layer Details

### Layer 1 — Browser (Interaction & Rendering)

The browser runs a single-page application (zero framework dependencies) that handles:

- **Gesture Pipeline:** MediaPipe Hands (WebAssembly) performs client-side hand landmark detection at 30fps. No server round-trips for gesture inference. Three detectors (pinch, palm, fist) feed a debounced state machine that dispatches interaction commands.

- **LLM Integration:** Responses are fetched from the DeepSeek-V3 API via HTTPS. The request fires during the breathing animation to mask LLM latency (2–8 seconds). Responses are parsed client-side and rendered through a markdown-to-HTML pipeline.

- **Visual Rendering:** A Canvas 2D starfield with parallax nebula runs at 60fps. CSS 3D transforms handle the card flip animation. The glassmorphism UI layer uses backdrop-filter and border effects.

### Layer 2 — Bridge (Communication Relay)

A Python asyncio server bridges the browser and hardware device:

- **WebSocket Server:** Handles multiple concurrent browser clients. Receives interaction commands (category selection, card picks, breathing states) and forwards them to the device.

- **Command Router:** Validates and translates browser commands into the device protocol. Lightweight text-based protocol — human-readable, debuggable, no parser overhead on the microcontroller.

- **Serial Bridge:** Non-blocking serial I/O using pyserial with a dedicated reader thread. Device-to-browser messages (button events, status responses) are forwarded back through WebSocket.

- **HTTP File Server:** Serves the static web application on port 8080, making the system self-contained.

### Layer 3 — Device (Physical Presence)

The M5StickC Plus runs MicroPython firmware that provides:

- **LED Driver:** Controls a SK6812 addressable LED strip (16 LEDs) through ESP32's RMT peripheral for cycle-accurate waveform generation. Six animation modes: Breath, Pulse, Rainbow, Warm, Static, Off.

- **Face Engine:** Seven facial expressions rendered on the 240×135 LCD: Idle, Awake, Thinking, Happy, Love, Breathe In, Breathe Out. Each face is drawn procedurally using arcs and circles — no bitmap assets.

- **Serial Protocol Parser:** Non-blocking command processing integrated into the main update loop. Supports 15+ commands for mode switching, face control, LED control, and buzzer triggering.

- **Standalone Mode:** The device can operate independently as a category selector using its physical buttons, with all feedback rendered locally.

## Communication Protocol

The browser and device communicate through a lightweight text protocol over WebSocket → Serial:

```
Browser → Device:              Device → Browser:
  MODE:CATEGORY                  EVT:CAT:Wealth
  MODE:PICK                      EVT:BTN_A
  PICKED:1                       PONG
  FACE:HAPPY                     READY
  BREATHE:IN
  STRIP:RAINBOW
```

Design rationale: human-readable, zero-dependency parsing, minimal memory footprint on the MicroPython heap (~60KB available).

## Design Decisions

| Decision | Rationale |
|----------|-----------|
| MediaPipe client-side (WASM) | Zero latency for gesture detection; no server dependency |
| Background LLM prefetch | Masks 2–8s API latency behind 12s breathing animation |
| Text protocol over JSON on device | MicroPython heap constraints; simpler debugging |
| Vanilla JS (no framework) | Minimises bundle size; no build step; fast iteration |
| ESP32 RMT for LEDs | Hardware-precise waveform timing vs. unreliable software bit-banging |
| Graceful degradation | LED strip failure → device operates with LCD-only feedback |
