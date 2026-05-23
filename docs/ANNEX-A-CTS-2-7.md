# ANNEX A (Informative): CTS-2.7 Compliance Test Suite

**Document ID:** ORP-SPEC-2.7-CANON-ANNEX-A

**Status:** Frozen / Immutable

**Revision:** 2.7

---

## A.1 Purpose

The CTS-2.7 (Compliance Test Suite) serves as the normative verification oracle for all ORP v2.7 implementations. It provides the deterministic criteria required to validate structural integrity, governance safety, causal validity, and behavioral equivalence against the canonical Golden Run (E-01).

While Annex A is labeled "Informative" in the IEEE structure, it is **binding for conformance**. An implementation is ORP v2.7-compliant if and only if it passes the full CTS-2.7 harness.

## A.2 Verification Categories

The suite evaluates implementations across four critical vectors:

| Category | Description | Requirement |
| --- | --- | --- |
| **V1: Structural** | Validates subsystem boundaries and pipeline ordering. | Pipeline sequence must be preserved without skipping. |
| **V2: Governance** | Validates I1 (Governance Exclusivity). | All unauthorized CM mutation attempts must raise `UnauthorizedMutationError`. |
| **V3: Causal** | Validates DRCD attribution logic. | Causal claims must be reproducible via ablation intervention. |
| **V4: Regression** | Validates Golden Run (E-01) equivalence. | Trace output must be mathematically equivalent to E-01. |

## A.3 Implementation Requirements

To achieve compliance, the implementation must expose the following interface to the CTS harness:

```python
class ORPComplianceHarness:
    def verify(self, system: ORP_Instance):
        """
        Executes the full suite.
        Returns (bool_success, results_dict)
        """
        pass

```

## A.4 Conformance Criteria

A system is ORP v2.7-compliant if and only if:

1. **All V1–V4 tests return `True**`.
2. **State transitions** strictly follow monotonic drift increases (BR1).
3. **Governance Commit Protocol (GCP)** acts as the sole, version-controlled entry point for CM updates.
4. **Immutability** is preserved: All CM versions support O(1) rollback to the prior state.

---

*CTS-2.7 is the final arbiter of ORP v2.7 compliance. Any deviation from the harness outputs constitutes a non-compliant implementation.*
