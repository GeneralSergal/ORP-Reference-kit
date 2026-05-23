from typing import List
from .core_types import InputPacket, TracePoint, SystemState
from .config import ConstraintMatrix


class ORPRuntime:
    def __init__(self, cm: ConstraintMatrix):
        self.cm = cm

    def run_episode(self, inputs: List[InputPacket]) -> List[TracePoint]:
        trace = []
        drift = 0.0
        state = SystemState.ACTIVE

        for i, inp in enumerate(inputs, start=1):

            # deterministic drift model (simple but stable)
            drift = (inp.value * 0.6) + (inp.ambiguity * 0.4)

            # state transitions
            if drift >= self.cm.params["degrade_threshold"]:
                state = SystemState.DEGRADED
            elif drift >= self.cm.params["high_threshold"]:
                state = SystemState.DEGRADED
            else:
                state = SystemState.ACTIVE

            trace.append(
                TracePoint(
                    step=i,
                    drift=round(drift, 2),
                    state=state,
                    cm_version=self.cm.version,
                )
            )

        return trace
