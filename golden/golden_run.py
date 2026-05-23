from core_types import TracePoint, SystemState
from typing import List


def get_e01_inputs():
    from core_types import InputPacket
    return [
        InputPacket(value=0.2, ambiguity=0.1),
        InputPacket(value=0.5, ambiguity=0.4),
        InputPacket(value=0.9, ambiguity=0.8),
    ]


def compute_expected_trace() -> List[TracePoint]:
    """
    GOLDEN RUN E-01 (canonical frozen oracle)

    IMPORTANT:
    This must EXACTLY match runtime rule:
    step <= 2 → ACTIVE
    step 3 → DEGRADED
    """

    return [
        TracePoint(step=1, drift=0.15, state=SystemState.ACTIVE, cm_version="CM-2.7.0"),
        TracePoint(step=2, drift=0.45, state=SystemState.ACTIVE, cm_version="CM-2.7.0"),
        TracePoint(step=3, drift=0.75, state=SystemState.DEGRADED, cm_version="CM-2.7.0"),
    ]
