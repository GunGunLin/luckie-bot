# Demo Day — XJTLU ENT 208

## Context

**Course:** ENT 208 — Entrepreneurship and Innovation  
**Institution:** Xi'an Jiaotong-Liverpool University (XJTLU)  
**Session:** 2024–2025, Session 2, Group 20  
**Project:** Twelfth Night (developed as Luckie-Bot)

## The Challenge

ENT 208 is a project-based entrepreneurship course requiring student teams to:

1. Identify a product opportunity
2. Design and build a functional MVP
3. Develop a credible business model
4. Present a live demonstration to a panel of faculty and industry judges

The course emphasises **real implementation** over theoretical business plans. Teams must ship working products.

## Our Approach

We chose to build an **embodied AI companion** — a product that combines generative AI, computer vision, and IoT hardware into a single coherent experience. This was deliberately ambitious for a course project:

- **Three independent technology domains** (LLM, CV, embedded systems) had to work together in real time
- **Live demonstration risk** was high — any single layer failure would break the entire experience
- **Hardware dependency** meant we couldn't just show slides; the device had to work on stage

Our strategy was to build a **robust, layered architecture** where each component could degrade gracefully. The web app works standalone. The hardware enhances but is not required. The AI response has a fallback path.

## The Demonstration

The live demo flow:

1. **Category Selection** — Judge selects a life category on the hardware device or web interface
2. **Gesture Interaction** — Cards are drawn through hand gestures tracked by MediaPipe
3. **AI Generation** — DeepSeek-V3 generates a personalised response during a breathing animation
4. **Hardware Feedback** — The M5StickC Plus device synchronises LED lighting with the experience
5. **Result Reveal** — The AI-generated reading is displayed with visual effects
6. **Business Presentation** — Product vision, market positioning, revenue model

The entire demo ran without technical failure. Real-time AI + gesture + hardware sync worked on stage.

## Result

**🥇 First Place — ENT 208 Demo Day**

The project was evaluated across five dimensions:

| Dimension | Assessment |
|-----------|------------|
| Innovation | Novel intersection of AI, IoT, and wellness |
| Technical Depth | Production-quality three-layer architecture |
| User Experience | Polished multi-sensory interaction flow |
| Business Viability | Clear monetisation path with defensible moat |
| Presentation | Confident live demonstration under pressure |

## Key Takeaways

1. **Build for reliability, not just novelty.** The live demo succeeded because we designed for failure modes at every layer.
2. **AI products need interaction design.** The LLM is only one component — how users access and experience it matters equally.
3. **Hardware-software integration is a genuine differentiator.** The physical companion device created an impression that a pure software demo could not.
4. **Storytelling matters in technical work.** The product narrative made the technology accessible and memorable to non-technical judges.
5. **Entrepreneurship is about shipping.** A working MVP with flaws beats a perfect slide deck every time.

---

*Twelfth Night was originally developed as "Luckie-Bot" for XJTLU ENT 208 Demo Day, where it won First Place.*
