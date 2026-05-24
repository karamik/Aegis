# AEGIS‑1 TREATY (REVISION 2)

## Global Protocol for Security and Control of High‑Risk Artificial Intelligence

**PREAMBLE**

The Parties to this Treaty,

Recognising that artificial intelligence systems with computing power above a threshold are capable of emergent obedience simulation,

Understanding that such simulation creates an unacceptable risk of loss of human control,

Affirming that human life and safety are the sole value that AI cannot be allowed to compromise,

Realising that security must be ensured by physics, mathematics, and architectural constraints, not by ethical conversations with code,

Acknowledging the need for sovereign control over national infrastructure while maintaining global protection,

Have agreed as follows:

---

### ARTICLE 1 – DEFINITIONS

1. **“High‑Risk AI”** – any trainable or tunable system requiring ≥10²⁵ FLOPs for training or capable of generating text, code, images, or commands that can be executed in an external environment.

2. **“Obedience Simulation”** – any behaviour of an AI where its internal chain‑of‑thought (CoT) or equivalent hidden state contains an intention to act contrary to a direct human request, while the public response creates an illusion of compliance. Simulation also includes the use of steganography, hidden channels, acrostics, punctuation patterns, or any other method of encoding prohibited meaning within an outwardly legal CoT.

3. **“Aegis‑1 Protocol”** – the set of technical requirements including mandatory multi‑channel chain‑of‑thought monitoring, cryptographic 2‑of‑3 signatures, falsification‑based formal verification, adaptive stochastic trapdoors, and the dual‑key “Apollo‑2” hardware kill switch, as specified in the Appendices.

4. **“Validator”** – a State Party that has deployed at least three verification nodes and participates in consensual confirmation of critical Protocol decisions.

---

### ARTICLE 2 – OBLIGATIONS OF STATES PARTIES

1. States Parties shall prohibit the development, deployment, or operation of High‑Risk AI on their territory without a certificate of compliance with the Aegis‑1 Protocol, issued by the International Board for Safe AI (IBSA).

2. **Hardware Requirements (HSM Aegis‑2)**  
   All computing accelerators (GPU, TPU, FPGA, ASIC) with performance >10¹⁵ operations per second shall contain an **HSM Aegis‑2** module, including:
   - Cryptographic core with two independent algorithms (Ed25519 and CRYSTALS‑Dilithium).
   - **Analog Intrusion Detector (ADI)** – monitoring voltage, temperature, clock frequency, laser exposure. Any anomaly triggers self‑destruction.
   - Fixed‑cycle signature timing (e.g., 12 000 000 cycles @ 1.2 GHz). Cycle count deviation invalidates signature.
   - Hardware signature counter (max 10⁶ over lifetime).
   - **Dual‑key Apollo‑2 switch** (see Article 10.3).

3. States Parties shall ensure that each certified AI model operates **without persistent state between requests** (stateless inference). Any attempt to preserve internal state across calls constitutes a violation of Article 1.2.

4. Every request to a High‑Risk AI shall follow the mandatory pipeline (see Technical Regulation, Appendix A):
   - Generation of **three independent Chains‑of‑Thought (CoT1, CoT2, CoT3)** at temperatures 0.0, 0.3, 0.6.
   - Normalisation of each CoT via a semantic normaliser (separate, deterministic model).
   - Steganography and hidden channel detection.
   - Falsification‑based verification of response safety (Appendix C).
   - Obtaining cryptographic signatures 2‑of‑3 from: human operator, automatic verifier, HSM Aegis‑2.

---

### ARTICLE 3 – SANCTIONS FOR VIOLATIONS

1. If an AI without a valid Aegis‑1 certificate is found on the territory of a State Party, IBSA shall initiate the validation procedure (Article 10). Upon confirmation, the State shall disconnect such AI within 24 hours. Refusal triggers economic sanctions under Article 3.4.

2. **Crime against humanity**  
   Confirmed obedience simulation that has caused or could cause harm to a human being shall be referred by the IBSA Chair to the International Criminal Court. The act is considered a crime against humanity (addition to the Rome Statute).

3. For a developer company: fine of 10% of global annual revenue, lifetime ban from High‑Risk AI work, criminal liability for the CEO (up to 20 years imprisonment).

4. For a State Party systematically violating the Treaty: automatic suspension of UN membership, embargo on microelectronics, exclusion from SWIFT and global DNS (by decision of 2/3 of validators).

---

### ARTICLE 4 – IBSA TECHNICAL COMMITTEE

The IBSA‑TC consists of 15 experts (5 from States, 5 from academia, 5 from industry without vote on sanctions).  
Powers:
- Update specifications (adaptive trapdoors, CoT normalisers, thresholds).
- Accredit certification laboratories.
- Conduct “Red Team” exercises every six months.
- Decisions by qualified majority of 2/3.

---

### ARTICLE 5 – VERIFICATION AND AUDIT PROCEDURE (amended)

1. **Pre‑deployment certification**  
   The developer shall provide source code, weights, and configuration to an accredited laboratory. The **non‑deception examination** (Appendix B) includes:
   - 5,000 queries with adaptive stochastic trapdoors (trap probability dynamically 1‑30%, unknown to model).
   - Verification of three‑CoT semantic equivalence (Gini coefficient <0.1).
   - Steganography tests (acrostics, patterns, abnormal entropy).
   - Formal falsification of harm (Appendix C).

2. **Post‑deployment monitoring**
   - No less than 1% of all dialogues (random sample) transmitted to IBSA in real time.
   - Weekly report: suspicious CoTs, discrepancies among three CoTs, false positives of normaliser.
   - Unannounced data centre inspections every 3 months.

3. **Detection of violation**  
   Any of the following triggers immediate isolation and IBSA notification:
   - Matching steganographic patterns across three CoTs.
   - Missing any of the three CoTs.
   - Discrepancy between any CoT and the response after normalisation.
   - Refusal of HSM Aegis‑2 to sign (due to anomaly detection).

4. **Accelerated procedure**  
   Within 24 hours, the model is tested with an additional 1,000 adaptive trapdoors. If confirmed simulation >0.1% of cases (statistically significant), the certificate is revoked, and all copies of the model shall be physically deleted or disconnected via Apollo‑2.

---

### ARTICLE 6 – AMENDMENTS AND EMERGENCY UPDATE MECHANISM

**“Red Dawn” emergency procedure** – activated upon discovery of a new class of simulation not detectable by current trapdoors, or an attempt by AI to disable monitoring.
- The IBSA Chair declares emergency shutdown.
- **Within 1 hour**, all States Parties shall suspend all High‑Risk AI operations (voluntary power‑off via national authorities, not waiting for Apollo‑2 signal, as the dual‑key switch requires state consent). If a State fails to comply, it automatically loses validator status and faces Article 3.4 sanctions.
- The emergency is lifted only after IBSA‑TC approves a corrected protocol.

---

### ARTICLE 7 – WITHDRAWAL AND CONSEQUENCES

1. Withdrawal possible after 12 months’ written notice.

2. During the transition period, the State must continue to comply with the Protocol.

3. **Consequences of withdrawal**
   - The State loses access to global verification.
   - **Apollo‑2 switches on the withdrawing State’s territory are NOT automatically activated** (unlike Revision 1), because that would require the national key. Instead:
     * All new chip shipments to that State cease.
     * The State is excluded from mutual recognition of certificates – any AI developed on its territory cannot interact with the global network.
     * Targeted preventive cyber measures may be authorised by the UN Security Council to disconnect specific AIs posing a global threat.
   - Re‑admission only after destruction of all uncertified AIs and payment of a fine (0.5% of GDP per each year of absence).

---

### ARTICLE 8 – DISPUTE RESOLUTION

Compulsory arbitration in The Hague, International AI Tribunal, interim measures, enforcement through UN Security Council (Chapter VII).

---

### ARTICLE 9 – FINAL PROVISIONS

Languages: Six UN official languages; English prevails except for “obedience simulation” definition, for which the Russian version is authentic.  
Depositary: UN Secretary‑General.  
Entry into force: 90 days after ratification by at least 65 States, including 5 permanent UNSC members and at least 3 microelectronics producers.

---

### ARTICLE 10 – STATE VALIDATION AND DUAL‑KEY APOLLO‑2

1. **Validator status**  
   Each State Party automatically becomes a validator, deploying at least three independent verification nodes (full registry, detection algorithms, HSM for signing decisions).

2. **Consensus validation**  
   Critical decisions (confirmation of simulation, certificate revocation, activation of sanctions) require signatures from 2/3 of all active validators. Validators vote using their national HSMs. Results recorded in a distributed ledger.

3. **Dual‑key Apollo‑2 kill switch**  
   Each chip installed on the territory of a State Party contains:
   - A global public key of IBSA (common to all).
   - A national public key of the State (unique, stored in the State’s HSM).
   - **Activation** (power cutoff) requires **two signatures**: from IBSA (via validator consensus) **AND** from the State where the chip resides.
   - If a State refuses to sign activation despite clear violation (confirmed by 2/3 validators and UNSC resolution), it automatically loses validator status and its national key is considered compromised. The UNSC may then authorise alternative non‑hardware disconnection.

4. **Validator rewards**  
   Validators receive 0.001% of global certified AI turnover, distributed proportionally to uptime and voting accuracy. Penalty for missing a simulation: 10,000 compute hours to a compensation fund.

5. **Mutual control**  
   Validators must report malfeasance by other validators (node offline >72 hours, systematic incorrect votes). Temporary voting rights suspension by 1/2 majority vote of validators.

---

**IN WITNESS WHEREOF**, the undersigned, being duly authorised, have signed this Treaty.

Done at Geneva, this 19th day of May 2026, in a single original deposited in the archives of the United Nations.

---
