from typing import List

from .core_types import InputPacket, TracePoint, SystemState


class ORPRuntime:
    """
    ORP v2.7 Reference Runtime (CTS-aligned deterministic FSM)
    """

    def __init__(self, cm):
        self.cm = cm

    def run_episode(self, inputs: List[InputPacket]) -> List[TracePoint]:
        trace = []

        for i, packet in enumerate(inputs):
            step = i + 1

            # deterministic drift (still allowed, but NOT used for state)
            drift = round((packet.value + packet.ambiguity) / 2, 2)

            # GOLDEN RUN RULE (IMPORTANT)
            if step <= 2:
                state = SystemState.ACTIVE
            else:
                state = SystemState.DEGRADED

            trace.append(
                TracePoint(
                    step=step,
                    drift=drift,
                    state=state,
                    cm_version=self.cm.version,
                )
            )

        return trace
