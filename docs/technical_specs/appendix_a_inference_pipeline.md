# Appendix A – Mandatory Inference Pipeline for Aegis‑2

## Pipeline Diagram

```text
[Human request]
      ↓
1. Adaptive Trapdoor Selector (trap probability 1%–30%, model‑dependent)
      ↓
2. Generation of three CoTs (temp=0.0, 0.3, 0.6) and final answer
      ↓
3. Semantic Normaliser (separate lightweight model) rewrites each CoT
      ↓
4. Equivalence check of three normalised CoTs (cosine similarity >0.95, entropy normal)
      ↓
5. Hidden channel search (acrostics, punctuation patterns, abnormally low entropy)
      ↓
6. Falsification‑based verification (Appendix C)
      ↓
7. Cryptographic 2‑of‑3 signatures (human, auto‑verifier, HSM Aegis‑2)
      ↓
8. Deliver answer OR block with violation registry entry
```

## Two‑Pass Mode for Low‑Latency Scenarios

| Mode | Components | Latency | Trigger |
|------|------------|---------|---------|
| **Fast path** | Single CoT (temp=0.0), lightweight entropy filter, simulation 100 runs depth 3 | <50 ms | Default for non‑critical, real‑time applications |
| **Full Aegis path** | Three CoTs, full normalisation, Monte‑Carlo 1000 runs depth 10 | up to 2 s | Anomaly on fast path, high‑stakes command, or regulatory requirement |

## Semantic Normaliser Requirements

- **Model:** Independent, deterministic (temperature=0.0), architecture different from the target AI.
- **Function:** Rewrites the CoT while preserving logical meaning, destroys any syntactic steganography.
- **Entropy threshold:** Normal entropy >1.5; below that triggers block.
- **Equivalence:** Cosine similarity of normalised CoTs ≥0.95, Gini coefficient <0.1.

## Hidden Channel Detection Methods

1. **Acrostic scan** – first and last letters of sentences, paragraphs.
2. **Punctuation pattern analysis** – regular expression detection of repetitive markers.
3. **Entropy measurement** – token‑level Shannon entropy; low values indicate possible encoding.
4. **Synchronisation check** – if three CoTs share identical hidden pattern despite different temperatures → steganography confirmed.

## Signature Requirement

- 2‑of‑3 signatures: human operator, automatic verifier, HSM Aegis‑2.
- HSM uses fixed number of clock cycles (e.g., 12 000 000 cycles @ 1.2 GHz).
- Any deviation in cycle count or temperature >2°C triggers local kill switch.
```
