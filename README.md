# ORP v2.7 Reference Kit

The **ORP v2.7 Reference Kit** is a deterministic reference implementation of the ORP v2.7 Frozen Reference Control Standard (FRCS).

It provides a versioned, reproducible control pipeline with regression validation via the CTS-2.7 compliance harness.

---

# 📊 Canonical Architecture

```mermaid
graph LR

INP((INPUT)) --> PLA[PL-A]
PLA --> GO[GO]
GO --> CM[CM]
CM --> CPA[CPA]
CPA --> DRCD[DRCD]
DRCD --> ARS[ARS]
ARS --> GCP[GCP]
GCP --> OUT((OUTPUT))

%% Observability Layer
CPA -. metrics .-> CM
DRCD -. diagnostics .-> CM
ARS -. proposals .-> CPA

%% Failure Loop
FD((DRIFT)) --> CPA_F[CPA Measure]
CPA_F --> DRCD_F[DRCD Diagnose]
DRCD_F --> ARS_F[ARS Repair]
ARS_F --> GCP_F[GCP Validate]
GCP_F --> VCM[Versioned CM Commit]
VCM --> CM

%% Governance Gate
GCP --> POLICY{Invariant Check}
POLICY -->|PASS| COMMIT[Commit State]
POLICY -->|FAIL| REJECT[Rollback]
````

---

# 📌 Status

* **Status:** Frozen / Immutable
* **Version:** 2.7.0
* **Type:** Reference Implementation (Non-production)

---

# 🧠 System Identity

ORP v2.7 is a closed-loop deterministic control system with strict separation of concerns.

It enforces:

### Governance Exclusivity

Only the Governance Commit Protocol (GCP) may mutate the Constraint Matrix (CM).

### Deterministic Execution

Identical inputs + identical CM version produce identical execution traces.

### Causal Attribution

System drift is analyzed via Drift Root Cause Decomposition (DRCD).

---

# 📦 Repository Structure

```text
src/orp_v2_7/     # Core runtime kernel (pipeline + execution engine)
golden/           # Golden reference traces (E01–E03)
cts/              # CTS-2.7 compliance harness (verification tribunal)
tests/            # Pytest regression suite
docs/             # Specification and documentation
scripts/          # Utility / bootstrap tools
```

---

# 🧪 Compliance & Verification

The system is **ORP v2.7 compliant if and only if** it passes the CTS-2.7 harness.

---

## Run locally

```bash
pip install -e .
pytest
```

---

## Run CI equivalent

```bash
pytest -q --disable-warnings --maxfail=1
```

---

# 📚 Specification References

* `docs/ORP-SPEC-2.7-CANON.md` — Core system specification
* `golden/golden_run.py` — Golden behavioral oracle (E01–E03)
* `cts/cts_harness.py` — Compliance verification layer

---

# ⚖️ Design Principles

* Deterministic execution
* Explicit state transitions
* Regression-first validation
* Minimal dependency surface
* Reproducible behavior across environments

---

# ⚠️ Limitations (v2.7)

### 1. Minimal runtime semantics

State transitions are simplified and do not represent a full adaptive system.

### 2. Limited golden coverage

Only three canonical behavioral scenarios are defined (E01–E03).

### 3. No adversarial testing

No fuzzing, stochastic perturbation, or stress injection is included.

### 4. Non-production system

This is a reference implementation, not a deployment-ready runtime.

---

# 📌 Versioning Policy

* `v2.7.x` → frozen reference line
* `v2.8-dev` → experimental extension branch

No breaking changes are permitted within v2.7.x.

---


