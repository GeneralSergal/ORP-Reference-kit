# ORP Cross-Repository Contract Bridge

## Version
ORP Bridge Contract v1.0

---

## 1. PURPOSE

This document defines the strict boundary between:

- ORP Spec Repository (`orp`)
- ORP Execution Repository (`ORP-Reference-kit`)

It prevents implicit coupling between:
- governance specification
- runtime implementation
- CTS validation expectations

---

## 2. LAYER OWNERSHIP MODEL

### L3 — SPECIFICATION (orp repo)
- Defines system invariants
- Defines governance semantics
- Defines conceptual architecture
- MUST NOT define runtime behavior details
- MUST NOT define CTS expectations

---

### L2 — EXECUTION (ORP-Reference-kit repo)
- Implements deterministic runtime behavior
- Owns execution logic
- Owns CTS harness implementation
- MUST NOT redefine specification invariants

---

### L1 — RUNTIME OUTPUT
- Observed execution traces
- Golden runs
- Regression artifacts
- Immutable once generated per version

---

## 3. CTS AUTHORITY RULE

The CTS (Compliance Test Suite):

- is defined in ORP-Reference-kit ONLY
- is NOT a spec authority
- is a validation tool, not a truth source

CTS failures indicate:
- implementation drift OR
- spec/implementation mismatch

NOT spec invalidity.

---

## 4. CHANGE PROPAGATION RULE

Any change MUST follow:

1. Spec change (orp repo)
   ↓
2. Manual review / translation step
   ↓
3. Implementation update (reference-kit)
   ↓
4. CTS update ONLY if behavior contract changes
   ↓
5. Golden run regeneration ONLY if explicitly approved

---

## 5. FORBIDDEN PATHS

The following are explicitly disallowed:

- CTS defining spec behavior
- Runtime behavior defining spec truth
- Golden traces silently redefining invariants
- L4 planning artifacts directly altering CTS expectations

---

## 6. DRIFT RESOLUTION RULE

If CTS fails:

Classify root cause as one of:

- IMPLEMENTATION_DRIFT
- SPEC_MISMATCH
- TEST_STALE

Resolution must explicitly declare which category applies.

---

## 7. VERSIONING RULE

- ORP Spec versioning is independent of reference-kit versioning
- ORP-Reference-kit may lag spec by one major version
- CTS version must match reference-kit version exactly

---

## 8. FINAL AUTHORITY STATEMENT

No repository has global authority.

Authority is partitioned:

- Spec defines intent
- Implementation defines behavior
- CTS verifies consistency between them
- Runtime defines observed truth
