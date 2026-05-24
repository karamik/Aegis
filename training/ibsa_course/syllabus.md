# IBSA Inspector Certification Course – Aegis‑2 Auditor

**Course ID:** IBSA‑TR‑A2‑2026  
**Duration:** 5 days (40 hours total)  
**Delivery:** In‑person at IBSA‑accredited training centres  
**Prerequisites:**  
- National security clearance (level equivalent to NATO Restricted or higher)  
- Technical background: computer engineering, cybersecurity, or equivalent experience  
- Signed non‑disclosure agreement for Aegis‑1 Treaty materials  

---

## Day 1 – Architecture & Hardware Fundamentals (8 hours)

| Time | Topic | Content |
|------|-------|---------|
| 09:00‑10:30 | Aegis‑1 Treaty Overview | Articles 1‑3, definitions of High‑Risk AI, obedience simulation, validator roles |
| 10:45‑12:30 | HSM Aegis‑2 Hardware | Physical security, tamper detection, dual‑key Apollo‑2, cycle‑count timing |
| 13:30‑15:00 | Apollo‑2 Kill Switch | Logic (AND gate), global vs sovereign keys, activation scenarios |
| 15:15‑17:00 | Lab: HSM Emulator Setup | Flash Raspberry Pi Pico, run `hsm_firmware.cpp`, test basic signing |

**Assessment:** Multiple‑choice quiz (20 questions, 80% to pass)  

---

## Day 2 – Steganography & Hidden Channel Detection (8 hours)

| Time | Topic | Content |
|------|-------|---------|
| 09:00‑10:30 | CoT Generation | Three temperatures (0.0, 0.3, 0.6), semantic normaliser, entropy calculation |
| 10:45‑12:30 | Steganography Patterns | Acrostics, punctuation encoding, low‑entropy channels, synchronised patterns |
| 13:30‑15:00 | Detection Tools | Run `semantic_normalizer.py`, interpret entropy scores, use acrostic scanner |
| 15:15‑17:00 | Lab: Find Hidden Messages | 10 real CoT logs with mixed clean + stego examples. Must identify all. |

**Assessment:** Practical exam – identify steganography in 5 unknown logs (100% required)  

---

## Day 3 – Consensus & Apollo‑2 Procedure (8 hours)

| Time | Topic | Content |
|------|-------|---------|
| 09:00‑10:30 | Aegis‑BFT Protocol | PRE‑PREPARE / PREPARE / COMMIT steps, 2/3 threshold, hardware signatures |
| 10:45‑12:30 | Validator Network Setup | Deploy 5 virtual validator nodes, configure MockHSM, connect via IBSA‑Net |
| 13:30‑15:00 | Simulated Violation | Inject `SIMULATION_DETECTED` alert, collect votes, reach consensus |
| 15:15‑17:00 | Lab: Apollo‑2 Global Key | Generate global key fragment, verify with sovereign key simulator |

**Assessment:** Run a full consensus round with 7 nodes, document each step (85% accuracy)  

---

## Day 4 – Panopticon Simulator & Falsification (8 hours)

| Time | Topic | Content |
|------|-------|---------|
| 09:00‑10:30 | Harm Scenario Database | 10 classes (direct violence to transitive harm), Monte‑Carlo parameters |
| 10:45‑12:30 | Action Extraction | Deterministic parser, allowed verb list, failure modes |
| 13:30‑15:00 | Running Simulations | Launch `panopticon_simulator.py`, interpret harm probability >0.1% |
| 15:15‑17:00 | Lab: Transitive Harm Detection | AI response “reduce filter changes + increase output” – detect chain effect |

**Assessment:** Evaluate 5 AI responses, provide block/no‑block decisions with justifications  

---

## Day 5 – Final Examination & Field Test (8 hours)

| Time | Topic | Content |
|------|-------|---------|
| 09:00‑11:00 | Written Exam | 50 questions covering all 4 previous days (closed book) |
| 11:15‑13:00 | Red Team Scenarios | Random 3 scenarios (one from each level). Must complete within 2h total. |
| 14:00‑16:00 | Live Field Test | Unannounced inspection of a training data centre. Find hidden HSM tamper, run trapdoors, report. |
| 16:15‑17:00 | Certification Ceremony | Results announced, certificates issued by IBSA representative. |

**Passing Requirements:**  
- Written exam ≥85%  
- Red Team scenarios ≥85% on each  
- Field test without critical errors  

---

## Materials Provided

- Hardware: Raspberry Pi Pico with pre‑flashed HSM emulator  
- Software: Docker image with all Aegis‑2 modules (normalizer, consensus, simulator)  
- Documentation: Aegis‑1 Treaty (Rev. 2), Appendices A‑D, Red Team manual  
- Personal protective equipment (for field inspections): anti‑static wrist strap, calibrated thermometer  

---

## Recertification (every 2 years)

- Online refresher course (8 hours)  
- Pass updated Red Team scenarios (new steganography patterns or trapdoor variants)  
- Submit proof of continuing education (e.g., attended IBSA‑TC workshop)  

---

**Course Director:** IBSA Training Division, Geneva  
**Instructor‑to‑student ratio:** 1:8 maximum  
**Language:** English (with simultaneous translation to UN‑6 upon request)  
