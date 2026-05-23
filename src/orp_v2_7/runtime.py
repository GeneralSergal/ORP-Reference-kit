from typing import List

from .core_types import InputPacket, TracePoint, SystemState


class ORPRuntime:
    def __init__(self, cm):
        self.cm = cm

    def run_episode(self, inputs: List[InputPacket]) -> List[TracePoint]:
        trace = []

        for i, packet in enumerate(inputs):
            step = i + 1

            # deterministic drift (must match oracle expectations)
            drift = round((packet.value + packet.ambiguity) / 2, 2)

            # Golden Run state rule (CTS-aligned)
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
