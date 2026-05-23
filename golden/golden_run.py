from dataclasses import dataclass
from typing import List
from enum import Enum, auto


# =========================
# Canonical ORP Types
# =========================

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


# =========================
# E-01 INPUT SEQUENCE
# =========================

def get_e01_inputs() -> List[InputPacket]:
    """
    Canonical ORP v2.7 Golden Run input sequence (E-01)
    Deterministic stress progression.
    """
    return [
        InputPacket(value=0.2, ambiguity=0.1),  # t0
        InputPacket(value=0.5, ambiguity=0.4),  # t1
        InputPacket(value=0.9, ambiguity=0.8),  # t2 (drift trigger)
    ]


# =========================
# CANONICAL EXPECTED TRACE
# =========================

EXPECTED_E01_TRACE: List[TracePoint] = [
    TracePoint(step=1, drift=0.10, state=SystemState.ACTIVE, cm_version="CM-2.7.0"),
    TracePoint(step=2, drift=0.10, state=SystemState.ACTIVE, cm_version="CM-2.7.0"),
    TracePoint(step=3, drift=0.10, state=SystemState.DEGRADED, cm_version="CM-2.7.0"),
]


# =========================
# CTS COMPATIBILITY API
# =========================

def compute_expected_trace() -> List[TracePoint]:
    """
    Adapter layer for CTS harness compatibility.
    Returns canonical oracle trace for comparison.
    """
    return EXPECTED_E01_TRACE


# =========================
# VALIDATION ORACLE (optional direct use)
# =========================

def validate_golden_run(actual_trace: List[TracePoint]) -> bool:
    """
    Hard oracle validation for debugging / local execution.
    CTS uses compute_expected_trace instead.
    """
    expected = EXPECTED_E01_TRACE

    assert len(actual_trace) == len(expected), "Trace length mismatch"

    for i, (a, e) in enumerate(zip(actual_trace, expected)):
        assert a.step == e.step, f"Step mismatch @ {i}"
        assert a.state == e.state, f"State mismatch @ {i}"
        assert a.cm_version == e.cm_version, f"CM mismatch @ {i}"
        assert abs(a.drift - e.drift) < 1e-6, f"Drift mismatch @ {i}"

    return True
