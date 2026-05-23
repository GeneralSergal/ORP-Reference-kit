from typing import List
from orp_v2_7.core_types import InputPacket, TracePoint, SystemState


# -----------------------------
# E01 INPUT SET
# -----------------------------
def get_e01_inputs() -> List[InputPacket]:
    return [
        InputPacket(0.2, 0.1),
        InputPacket(0.5, 0.4),
        InputPacket(0.9, 0.8),
    ]


# -----------------------------
# E01 EXPECTED TRACE (ORACLE)
# -----------------------------
def compute_expected_trace() -> List[TracePoint]:
    return [
        TracePoint(step=1, drift=0.170, state=SystemState.ACTIVE, cm_version="CM-2.7.0"),
        TracePoint(step=2, drift=0.301, state=SystemState.DEGRADED, cm_version="CM-2.7.0"),
        TracePoint(step=3, drift=0.521, state=SystemState.DEGRADED, cm_version="CM-2.7.0"),
    ]


# -----------------------------
# E02 INPUT SET (LOW DRIFT)
# -----------------------------
def get_e02_inputs() -> List[InputPacket]:
    return [
        InputPacket(0.1, 0.05),
        InputPacket(0.2, 0.1),
        InputPacket(0.1, 0.2),
    ]


def compute_expected_trace_e02() -> List[TracePoint]:
    return [
        TracePoint(step=1, drift=0.120, state=SystemState.ACTIVE, cm_version="CM-2.7.0"),
        TracePoint(step=2, drift=0.144, state=SystemState.ACTIVE, cm_version="CM-2.7.0"),
        TracePoint(step=3, drift=0.131, state=SystemState.ACTIVE, cm_version="CM-2.7.0"),
    ]


# -----------------------------
# E03 INPUT SET (HIGH DRIFT)
# -----------------------------
def get_e03_inputs() -> List[InputPacket]:
    return [
        InputPacket(0.9, 0.9),
        InputPacket(0.95, 0.95),
        InputPacket(1.0, 1.0),
    ]


def compute_expected_trace_e03() -> List[TracePoint]:
    return [
        TracePoint(step=1, drift=0.900, state=SystemState.DEGRADED, cm_version="CM-2.7.0"),
        TracePoint(step=2, drift=0.955, state=SystemState.FROZEN, cm_version="CM-2.7.0"),
        TracePoint(step=3, drift=0.978, state=SystemState.FROZEN, cm_version="CM-2.7.0"),
    ]
