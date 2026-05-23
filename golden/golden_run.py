from dataclasses import dataclass
from typing import List
from enum import Enum, auto


# -----------------------------
# Canonical Types (local oracle scope)
# -----------------------------

class SystemState(Enum):
    ACTIVE = auto()
    DEGRADED = auto()
    FROZEN = auto()


@dataclass(frozen=True)
class InputPacket:
    value: float
    ambiguity: float


@dataclass(frozen=True)
class TracePoint:
    step: int
    drift: float
    state: SystemState
    cm_version: str


# -----------------------------
# E-01 INPUT SEQUENCE
# -----------------------------
def get_e01_inputs() -> List[InputPacket]:
    """
    Canonical ORP v2.7 Golden Run input sequence (E-01)
    Deterministic stress escalation profile.
    """
    return [
        InputPacket(value=0.2, ambiguity=0.1),  # t0: stable
        InputPacket(value=0.5, ambiguity=0.4),  # t1: moderate load
        InputPacket(value=0.9, ambiguity=0.8),  # t2: drift trigger
    ]


# -----------------------------
# EXPECTED TRACE (ORACLE)
# -----------------------------
EXPECTED_E01_TRACE: List[TracePoint] = [
    TracePoint(
        step=1,
        drift=0.10,
        state=SystemState.ACTIVE,
        cm_version="CM-2.7.0",
    ),
    TracePoint(
        step=2,
        drift=0.10,
        state=SystemState.ACTIVE,
        cm_version="CM-2.7.0",
    ),
    TracePoint(
        step=3,
        drift=0.10,
        state=SystemState.DEGRADED,
        cm_version="CM-2.7.0",
    ),
]


# -----------------------------
# ORACLE VALIDATION FUNCTION
# -----------------------------
def validate_golden_run(actual_trace: List[TracePoint]) -> bool:
    """
    Deterministic oracle check for CTS-2.7 compliance.
    """
    assert len(actual_trace) == len(EXPECTED_E01_TRACE), (
        f"Trace length mismatch: {len(actual_trace)} != {len(EXPECTED_E01_TRACE)}"
    )

    for i, (expected, actual) in enumerate(zip(EXPECTED_E01_TRACE, actual_trace)):
        assert expected.step == actual.step, f"[step mismatch @ {i}]"
        assert expected.state == actual.state, f"[state mismatch @ step {i}]"
        assert expected.cm_version == actual.cm_version, f"[CM version mismatch @ step {i}]"
        assert abs(expected.drift - actual.drift) < 1e-6, f"[drift mismatch @ step {i}]"

    return True
