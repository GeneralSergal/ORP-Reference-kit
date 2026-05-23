from orp_v2_7.core_types import InputPacket, TracePoint, SystemState
from orp_v2_7.config import CM_V2_7_BASE


def get_e01_inputs():
    return [
        InputPacket(0.2, 0.1),
        InputPacket(0.5, 0.4),
        InputPacket(0.9, 0.8),
    ]


def expected_e01():
    return [
        TracePoint(1, 0.18, SystemState.ACTIVE, CM_V2_7_BASE.version),
        TracePoint(2, 0.46, SystemState.DEGRADED, CM_V2_7_BASE.version),
        TracePoint(3, 0.86, SystemState.DEGRADED, CM_V2_7_BASE.version),
    ]


def expected_e02():
    return [
        TracePoint(1, 0.08, SystemState.ACTIVE, CM_V2_7_BASE.version),
        TracePoint(2, 0.10, SystemState.ACTIVE, CM_V2_7_BASE.version),
        TracePoint(3, 0.14, SystemState.ACTIVE, CM_V2_7_BASE.version),
    ]


def expected_e03():
    return [
        TracePoint(1, 0.30, SystemState.ACTIVE, CM_V2_7_BASE.version),
        TracePoint(2, 0.82, SystemState.DEGRADED, CM_V2_7_BASE.version),
        TracePoint(3, 0.90, SystemState.DEGRADED, CM_V2_7_BASE.version),
    ]


GOLDEN_CASES = {
    "E01": (get_e01_inputs, expected_e01),
    "E02": (lambda: get_e01_inputs(), expected_e02),
    "E03": (lambda: get_e01_inputs(), expected_e03),
}
