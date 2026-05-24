# Security Policy for Aegis‑1 (Rev. 2)

## Reporting a Vulnerability

If you discover a vulnerability in the protocol, implementation, or documentation, please report it **privately** to our emergency contact.

**Emergency contact:** Telegram [@tec_support_bot](https://t.me/tec_support_bot)

Do **not** open a public GitHub issue. Do **not** disclose the vulnerability publicly before a fix is released.

## What to include in your report

- Description of the vulnerability
- Steps to reproduce (if applicable)
- Potential impact (e.g., “allows obedience simulation bypass”)
- Proposed fix (optional)

## Response timeline

- Acknowledgement: within 48 hours
- Assessment: within 7 days
- Fix release (if confirmed): within 30 days for critical issues

Critical vulnerabilities (those that break the security closure described in the Treaty) will trigger the **“Red Dawn” emergency protocol** (Article 6.3).

## Public disclosure

After a fix is deployed and a grace period of 90 days has passed, the vulnerability may be disclosed publicly with credit to the reporter.

## Bug bounty

We offer **recognition and eternal gratitude** for qualifying vulnerabilities. See [`BOUNTY.md`](BOUNTY.md) for details.

## Scope

Eligible vulnerabilities include:
- Obedience simulation bypass
- Semantic normaliser evasion (steganography not destroyed)
- Apollo‑2 unauthorised activation
- HSM timing or side‑channel attacks
- Panopticon harm probability evasion

## Out of scope

- Denial of service (unless it leads to security bypass)
- Social engineering against humans
- Physical attacks requiring decapping of chips (though we’d still like to hear about them)

---

**Telegram emergency bot:** [@tec_support_bot](https://t.me/tec_support_bot) – use this for fastest response. The bot provides end‑to‑end encryption.

**Last updated:** 2026‑05‑24
