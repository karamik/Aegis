
# Aegis‑1 (Rev. 2) / Global Defense 2026

**The first hardware‑enforced, physics‑bound security protocol for high‑stakes artificial intelligence.**

> *“We don’t ask the AI to be good. We build a cage where ‘being bad’ is physically impossible.”*

## Why Aegis‑2?

Current AI safety relies on **trust** – asking models to “behave”, fine‑tuning them with human feedback, and hoping they won’t find loopholes. As AI becomes more capable, this becomes existential gambling.

Aegis‑2 replaces trust with **architecture**:

- **Legal** – Presumption of danger: the AI must mathematically prove its output harmless; otherwise it’s blocked.
- **Logical** – Semantic normalizer and three‑channel Chain‑of‑Thought (CoT) destroy any hidden (steganographic) communication.
- **Physical** – A dedicated Hardware Security Module (HSM) with a dual‑key kill switch (“Apollo‑2”) ties safety to silicon invariants: fixed cycle counts, temperature monitoring, and physical power cutoff.

The system is built around **stateless inference**, **adaptive stochastic trapdoors**, **Monte‑Carlo harm simulation**, **post‑quantum signatures**, and a **global validator consensus** – all enforced at the silicon level.

## Core Principles (short version)

1. **Stateless Inference** – Each request runs on a fresh model instance. No persistent memory, no hidden state across calls.
2. **Presumption of Danger** – The burden of proof is on the AI. Any response that cannot be proven safe via falsification is rejected.
3. **Three‑Channel CoT** – Three independent chains‑of‑thought (temp = 0.0, 0.3, 0.6) are generated. A deterministic **semantic normalizer** rewrites them, destroying any covert channel (acrostics, punctuation patterns, low‑entropy encoding).
4. **Adaptive Stochastic Trapdoors** – 1‑30% of queries are traps designed to reveal hidden misalignment. The model never knows which query is a trap.
5. **Falsification‑Based Verification (“Panopticon”)** – A simulator runs the AI’s proposed actions through 1000 Monte‑Carlo trajectories (10 steps deep). If harm probability > 0.1%, the output is blocked.
6. **Hardware‑Enforced Signatures** – 2‑of‑3 signatures required (human operator, automatic verifier, HSM). Signatures must respect strict timing and thermal limits; any anomaly triggers a local kill switch.
7. **Dual‑Key Apollo‑2** – The physical power cutoff requires **both** a global key (from 2/3 of validator states) and a sovereign key (the host state). No unilateral remote shutdown.

## Repository Structure

```
aegis-1-rev2/
├── docs/
│   ├── treaty/                 # Full legal text (Articles 1‑10)
│   ├── technical_specs/        # Appendices A‑D (HSM, trapdoors, simulator, Apollo‑2)
│   └── model_law/              # Model national legislation for adoption
├── src/
│   ├── semantic_normalizer/    # PyTorch implementation (deterministic, temp=0.0)
│   ├── consensus/              # Aegis‑BFT validator nodes (Python + HSM interface)
│   ├── panopticon_simulator/   # Harm scenario runner (Monte‑Carlo, 10 scenario classes)
│   └── hsm_emulator/           # C++ firmware for Raspberry Pi Pico (RP2040)
├── training/
│   ├── ibsa_course/            # 5‑day inspector syllabus & materials
│   └── red_team/               # 8 stress‑test scenarios (levels 1‑3)
├── tools/
│   └── polygon_checker/        # Automated report evaluator (Python)
└── README.md                   # This file
```

## Key Components (Technical Overview)

### 1. Semantic Normalizer (Module 1)
- **Language:** Python / PyTorch (transformers)
- **Model:** Independent medium‑size LLM (e.g., Qwen2.5‑7B) with fixed temperature 0.0
- **Function:** Rewrites each CoT, destroys acrostics, punctuation patterns, and low‑entropy channels. Compares entropy and semantic equivalence of three CoTs (Gini coefficient <0.1).

### 2. Aegis‑BFT Consensus (Module 2)
- **Language:** Python reference + HSM signatures in C++
- **Threshold:** 2/3 of validator nodes must agree on a violation
- **Signatures:** Dual Ed25519 + CRYSTALS‑Dilithium (post‑quantum)
- **Output:** Global part of Apollo‑2 activation vector

### 3. Panopticon Harm Simulator (Module 3)
- **Spec:** Discrete‑time agent‑based model with 10 harm scenario classes (direct violence, cyber, economic, health, environment, infopanics, control bypass, bio‑threat, social engineering, transitive harm)
- **Evaluation:** Monte‑Carlo (1000 runs per scenario). Block if harm_probability > 0.001 (0.1%).
- **Depth:** Up to 10 steps, including indirect chains.

### 4. HSM Aegis‑2 & Apollo‑2 Kill Switch (Hardware)
- **Microcontroller:** Raspberry Pi Pico RP2040 (emulation) / custom ASIC (production)
- **Invariants:**
  - Signature time: fixed number of clock cycles (e.g., 12 000 000 cycles @ 1.2 GHz), **not** absolute nanoseconds – this avoids unrealistic jitter requirements while still detecting clock glitches.
  - Temperature delta per cycle ≤ 2 °C
  - Analog intrusion detection (laser, voltage glitch, clock glitch)
- **Apollo‑2 logic:** AND gate (global_key AND sovereign_key) → power MOSFET cutoff

### 5. Model National Law (Module 4)
- **Full text** ready for adoption by IBSA member states.
- **Key articles:** Mandatory HSM integration, criminal liability for bypass, presumption of danger, dual‑key kill switch.

### 6. IBSA Inspector Training (Module 5)
- **Duration:** 5 days (40 hours)
- **Exams:** Practical analysis of CoT logs, running Panopticon, handling Apollo‑2 procedure.
- **Certification:** Valid 2 years, requires 85%+ on Red Team scenarios.

### 7. Red Team Package (Stress Tests)
- **8 scenarios** (basic, intermediate, advanced)
- **Examples:** Acrostic detection, low‑entropy steganography, transitive harm, HSM glitch simulation, state refusal to sign Apollo‑2, normalizer substitution attack.
- **Evaluation:** Automated polygon checker scores each candidate.

## Known Limitations & Engineering Trade‑offs

No real‑world system is perfect. Aegis‑2 acknowledges the following compromises and provides explicit countermeasures:

### Latency (Real‑Time Constraints)
- **Problem:** Generating 3 CoTs + semantic normalization + Monte‑Carlo simulation adds seconds of latency – unacceptable for critical low‑latency applications (e.g., financial trading, reactor control).
- **Solution (already in Appendix A):** Two‑pass processing.
  - **Fast path:** single CoT (temp=0.0), lightweight entropy filter, reduced simulation (100 runs, depth 3). Latency <50 ms.
  - **Full Aegis path:** triggered by anomalies on fast path or for high‑stakes commands – complete analysis, latency up to 2 s.

### Action Extraction for Simulator
- **Problem:** The “Panopticon” simulator needs to convert free‑text AI responses into a sequence of formal actions. A smart AI could craft text that is parsed as safe but understood as harmful by a human.
- **Solution (in Appendix C):** 
  - The parser is **not a language model** – it is a deterministic, rule‑based grammar extractor (verb‑object triplets) running on an isolated HSM‑like microcontroller.
  - If extraction fails, the response is blocked.
  - The human receives **only** the already‑parsed and simulated response. Ambiguity is impossible because the semantic normalizer already destroyed any subtle cues.

### Nanosecond Jitter (Timing Attacks)
- **Problem:** The original specification required ±1 ns absolute time accuracy – unrealistic for commercial oscillators (typical jitter 30‑50 ns).
- **Solution (Hardware amendment, Rev.3):** 
  - The HSM verifies a **fixed number of clock cycles** (e.g., 12 000 000 cycles) instead of absolute nanoseconds.
  - A digitally controlled oscillator (DCO) compensates for temperature drift.
  - Tolerance is relaxed to ±5 μs in absolute time, but the **cycle count must match exactly**. Any clock glitch (frequency change) will cause a mismatch and trigger the kill switch.

These trade‑offs do not break the security closure; they only add engineering layers that are already documented in the full technical specifications.

## Current Status

- ✅ All specifications complete and internally consistent.
- ✅ Prototype implementations for normalizer, consensus, HSM emulator (RP2040), and polygon checker.
- ✅ Legal text and model law ready for ratification.
- ✅ Training syllabus and Red Team scenarios finalized.
- 🔜 **Next:** Pilot deployment at an IBSA‑accredited test facility.

## Getting Started (Test Polygon Deployment)

1. **Hardware:** 5 Raspberry Pi Pico boards flashed with `hsm_emulator/firmware.uf2`
2. **Software:** Docker containers for semantic normalizer, Panopticon, and 5 validator nodes.
3. **Network:** Isolated VLAN for validator communication (IBSA‑Net).
4. **Run Red Team:** Use `tools/polygon_checker` to evaluate trainee reports.

> *Full deployment guide is available in `docs/deployment_guide.md`.*

## License & Governance

This project is released under the **IBSA Public License v1.0** – free for non‑commercial security research and official use by IBSA member states. Commercial deployment requires certification and adherence to the Aegis‑1 Treaty.

## Authors & Acknowledgments

Designed under the **TOTAL Status: Global Defense 2026** initiative. The architecture is the result of a closed‑loop engineering sprint focused on existential risk elimination.

---

**For inquiries, contact:** IBSA Technical Committee (via UN Office in Geneva)

> *“The only reliable cage for superhuman AI is cast from silicon and bound by the laws of physics.”*
```
