# ORP v2.7 — Glossary

This glossary defines canonical terms used across the ORP (Operational Reasoning Pipeline) architecture.

All definitions are system-level and implementation-agnostic.

---

## A

### ARS (Adaptive Response Synthesis)
A system layer responsible for generating corrective strategies, optimizations, and structured proposals based on diagnostic and performance inputs.

---

## C

### CM (Core Memory)
The central state container of the ORP system. It represents the current working state of execution, including objective alignment and validated transitions.

### CPA (Computational Performance Analysis)
A monitoring and evaluation layer that computes system performance metrics, efficiency signals, and runtime behavior characteristics.

---

## D

### Drift
A divergence between expected invariant-compliant behavior and actual system state progression. Drift triggers the failure resolution pipeline.

### DRCD (Diagnostics & Root Cause Detection)
A subsystem responsible for identifying anomalies, structural inconsistencies, and root causes of system deviation.

---

## F

### Failure Loop
An isolated corrective subsystem that handles drift recovery without interfering with the main execution pipeline.

---

## G

### GCP (Governance Control Point)
A strict validation boundary that enforces system invariants (I1–I3). All state transitions affecting persistence must pass through GCP.

---

## I

### Invariants (I1–I3)
Core architectural rules that define correctness constraints:

- I1: Governance Exclusivity
- I2: Observability Non-Mutation
- I3: Recovery Containment

---

## O

### Observability Layer
A non-mutative feedback system that provides metrics, diagnostics, and proposals without directly modifying execution state.

### OUTPUT
The final result emitted by the ORP system after passing through all execution and governance stages.

---

## P

### PL-A (Preprocessing Layer A)
The initial transformation layer that normalizes raw input into structured system-readable data.

---

## R

### Recovery Loop
A structured correction pipeline that detects drift, diagnoses causes, generates repairs, and reinjects validated state into CM via GCP.

---

## S

### System State
The active, structured representation of all operational data within CM at a given moment in execution.

---

## T

### Transition
A state change within the ORP system. All transitions affecting persistent state must be validated by GCP.

---

## GLOSSARY PRINCIPLES

### Canonical Consistency
Each term has a single authoritative definition across the system.

### Non-Ambiguity Rule
No overlapping or conflicting definitions are allowed between architecture, interfaces, and invariants.

### Governance Binding
Any term involving state transition implicitly depends on GCP validation rules.

---

## VERSION

- Spec Version: ORP v2.7
- Document Type: System Glossary
