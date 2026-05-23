from .core_types import InputPacket, TracePoint, SystemState


def get_e01_inputs():
    return [
        InputPacket(value=0.2, ambiguity=0.1),
        InputPacket(value=0.5, ambiguity=0.4),
        InputPacket(value=0.9, ambiguity=0.8),
    ]


def compute_expected_trace():
    return [
        TracePoint(step=1, drift=0.10, state=SystemState.ACTIVE, cm_version="CM-2.7.0"),
        TracePoint(step=2, drift=0.10, state=SystemState.ACTIVE, cm_version="CM-2.7.0"),
        TracePoint(step=3, drift=0.10, state=SystemState.DEGRADED, cm_version="CM-2.7.0"),
    ]
