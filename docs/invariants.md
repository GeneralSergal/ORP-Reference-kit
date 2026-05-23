# ORP v2.7 — System Invariants

This document defines the non-negotiable constraints governing the ORP (Operational Reasoning Pipeline) system.

Invariants are global rules that must hold true for all execution states, transitions, and recovery operations.

Violation of any invariant constitutes a system fault and triggers rollback or halting behavior.

---

## I1 — Governance Exclusivity

All persistent state transitions MUST pass through the GCP (Governance Control Point).

### Rules

- No direct transition from any execution node to OUTPUT without GCP validation.
- No bypass paths are permitted around GCP under any condition.
- Failure recovery outputs MUST also pass through GCP before reinjection into CM.

### Intent

Ensures centralized control over system state authorization.

---

## I2 — Observability Non-Mutation

Observability signals MUST NOT directly mutate execution state.

### Rules

- Metrics, diagnostics, and proposals are read-only with respect to CM.
- Observability outputs may influence reasoning but not directly alter state.
- No feedback channel may bypass CPA/DRCD/ARS mediation.

### Allowed Flows

- CPA → CM (metrics influence only)
- DRCD → CM (diagnostic awareness only)
- ARS → CPA (proposal refinement only)

### Disallowed

- Observability → direct CM mutation
- Observability → OUTPUT path injection

---

## I3 — Recovery Containment

Failure recovery MUST remain isolated from primary execution flow.

### Rules

- The failure loop operates as a side-channel subsystem.
- It MUST NOT directly inject output into the execution pipeline.
- All recovered states MUST re-enter the system via CM → GCP validation.

### Required Flow

Drift → CPA → DRCD → ARS → GCP → Versioned CM → CM

### Prohibited Behavior

- Direct Failure Loop → OUTPUT injection
- Skipping GCP validation during recovery
- Overwriting CM without versioned commit

---

## I4 — Deterministic Transition Constraint

All node transitions MUST be deterministic given identical inputs.

### Rules

- No hidden state mutation between invocations.
- No external side effects altering node outputs unpredictably.
- Each node behaves as a pure transformation function.

---

## I5 — Single Source of Truth (CM)

CM is the only authoritative system state container.

### Rules

- All system states must originate or be reflected in CM.
- No parallel or shadow state stores are permitted.
- All updates to system state must be reconciled through CM versioning.

---

## I6 — Acyclic Execution Guarantee

The execution pipeline MUST remain acyclic under normal operation.

### Rules

- No circular dependencies in EXECUTION plane.
- Feedback loops are allowed only in OBSERVABILITY and FAILURE planes.
- GCP does not create cyclic execution dependencies.

---

## Enforcement Model

Invariant violations trigger:

1. Execution halt or suspension
2. State rollback to last valid CM version
3. Re-validation through GCP
4. Re-entry into execution only after PASS condition

---

## Relationship to Other Documents

- `architecture.md` → Defines structural layout enforcing invariants
- `interfaces.md` → Defines node-level contract constraints
- `glossary.md` → Defines semantic meaning of invariant-related terms

---

## VERSION

- Spec Version: ORP v2.7
- Document Type: System Invariants
