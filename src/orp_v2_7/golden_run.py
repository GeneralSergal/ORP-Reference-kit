from orp_v2_7.golden_run import get_e01_inputs, compute_expected_trace

def get_e01_inputs():
    return [
        InputPacket(value=0.2, ambiguity=0.1),
        InputPacket(value=0.5, ambiguity=0.4),
        InputPacket(value=0.9, ambiguity=0.8),
    ]


def compute_expected_trace():
    # MUST MATCH runtime logic exactly (deterministic oracle)
    return [
        TracePoint(step=1, drift=0.15, state=SystemState.ACTIVE, cm_version="CM-2.7.0"),
        TracePoint(step=2, drift=0.45, state=SystemState.DEGRADED, cm_version="CM-2.7.0"),
        TracePoint(step=3, drift=0.85, state=SystemState.FROZEN, cm_version="CM-2.7.0"),
    ]
