# Contributing to Aegis‑1 (Rev. 2)

Thank you for your interest in contributing to the Aegis‑1 project. This repository defines the global protocol for secure AI deployment. Any contribution must not weaken the security closure.

## Scope of Contributions

We welcome:
- **Bug fixes** (typos, broken links, code errors)
- **Performance optimisations** (without reducing safety guarantees)
- **Additional test scenarios** for the Red Team package
- **Translations** of documentation (official languages: English, Russian, Chinese, Arabic, Spanish, French)
- **Hardware implementation notes** for different platforms

We **do not accept**:
- Relaxation of timing constraints (cycle counts, temperature thresholds)
- Removal of any safety layer (e.g., skipping semantic normalisation)
- Changes that introduce stochastic behaviour into deterministic components

## Contribution Workflow

1. **Fork** the repository.
2. **Create a branch** with a descriptive name: `fix/typo-readme` or `feat/new-test-scenario`.
3. **Make your changes**, keeping code style consistent with existing files.
4. **Run tests** (if applicable): `python -m pytest tests/`
5. **Sign your commit** using `git commit -s` (Developer Certificate of Origin).
6. **Open a pull request** against the `main` branch.
7. **Wait for review** by IBSA‑TC members. Critical changes require 2 approvals.

## Developer Certificate of Origin (DCO)

By signing your commits, you certify that you have the right to submit the contribution under the IBSA Public License v1.0.

## Code Style

- Python: PEP 8, type hints required
- C++ (HSM firmware): Google style, no dynamic allocation
- Markdown: wrap at 120 characters, use `bash` for code blocks

## Review Process

- Automated checks: licence header, trailing whitespace, JSON schema for reports
- Human review: within 7 days
- Merge by IBSA‑TC member

## Security Vulnerability Reporting

**Do NOT open a public issue.** Send encrypted email to `security@ibsa.aegis` (PGP key in repository). See `SECURITY.md`.

---

Thank you for making AI safety a reality.

— IBSA Technical Committee
