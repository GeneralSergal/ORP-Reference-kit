from src.orp_v2_7.core_types import InputPacket, TracePoint, SystemState


def get_e01_inputs():
    return [
        InputPacket(0.2, 0.1),
        InputPacket(0.5, 0.4),
        InputPacket(0.9, 0.8),
    ]


def compute_expected_trace():
    return [
        TracePoint(1, 0.03, SystemState.ACTIVE, "CM-2.7.0"),
        TracePoint(2, 0.07, SystemState.ACTIVE, "CM-2.7.0"),
        TracePoint(3, 0.13, SystemState.DEGRADED, "CM-2.7.0"),
    ]
