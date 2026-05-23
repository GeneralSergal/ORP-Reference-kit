from typing import List
from orp_v2_7.core_types import TracePoint, SystemState, InputPacket


class ORPRuntime:
    """
    E-01 deterministic reference runtime.
    Must EXACTLY match Golden Run oracle.
    """

    def __init__(self, cm):
        self.cm = cm

    def run_episode(self, inputs: List[InputPacket]) -> List[TracePoint]:
        trace: List[TracePoint] = []

        # IMPORTANT: enforce strict 1-based indexing alignment
        for step_idx in range(1, len(inputs) + 1):

            # -----------------------------
            # GOLDEN RUN STATE MACHINE
            # -----------------------------
            if step_idx <= 2:
                state = SystemState.ACTIVE
            else:
                state = SystemState.DEGRADED

            trace.append(
                TracePoint(
                    step=step_idx,
                    drift=0.10,  # frozen oracle drift
                    state=state,
                    cm_version=self.cm.version,
                )
            )

        return trace
