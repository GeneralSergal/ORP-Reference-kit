# ORP v2.7 — Node Interfaces Specification

This document defines the canonical input/output contracts for each node in the ORP execution pipeline.

All interfaces are abstract and implementation-agnostic.

---

## INPUT

```yaml
input:
  type: any
  description: External entry point into the ORP system
````

---

## PL-A (Preprocessing Layer A)

```yaml
input:
  - raw_input

output:
  - normalized_input
```

---

## GO (Goal Formulation Operator)

```yaml
input:
  - normalized_input

output:
  - objective_state
```

---

## CM (Core Memory)

```yaml
input:
  - objective_state
  - feedback_signals (optional)

output:
  - system_state
```

---

## CPA (Computational Performance Analysis)

```yaml
input:
  - system_state

output:
  - metrics
  - performance_profile
```

---

## DRCD (Diagnostics & Root Cause Detection)

```yaml
input:
  - system_state

output:
  - anomaly_report
  - structural_analysis
```

---

## ARS (Adaptive Response Synthesis)

```yaml
input:
  - metrics
  - anomaly_report
  - structural_analysis

output:
  - repair_strategy
  - proposal_set
```

---

## GCP (Governance Control Point)

```yaml
input:
  - proposed_state
  - repair_strategy (optional)

output:
  - decision: PASS | FAIL
  - commit_authorization
```

---

## OUTPUT

```yaml
input:
  - validated_state

output:
  - final_result
```

---

## Interface Principles

### 1. Deterministic Contracts

Each node must produce outputs strictly derived from declared inputs.

### 2. No Hidden Side Effects

Nodes may not mutate upstream state without explicit return channels.

### 3. Governance Dependency

Any state transition that affects CM persistence must pass through GCP validation.

### 4. Observability Exclusion

Observability signals (metrics, diagnostics) are read-only and must not appear as control inputs unless explicitly routed.

---

## Version

* Spec Version: ORP v2.7
* Stability: Architectural Contract Layer


