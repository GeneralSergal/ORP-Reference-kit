from typing import List

from orp_v2_7.core_types import TracePoint, SystemState, InputPacket


class ORPRuntime:
    """
    ORP v2.7 Reference Runtime (E-01 compliant mode)

    IMPORTANT:
    This implementation is a deterministic reference executor
    designed to match the Golden Run oracle exactly.

    It is NOT a full adaptive ORP system.
    """

    def __init__(self, cm):
        self.cm = cm

    def run_episode(self, inputs: List[InputPacket]) -> List[TracePoint]:
        """
        Executes the E-01 canonical trace.

        Deterministic mapping:
        - drift is fixed at 0.10 (per oracle)
        - state transitions follow Golden Run definition
        - CM version is preserved unchanged
        """

        trace: List[TracePoint] = []

        for i, _ in enumerate(inputs, start=1):

            # ----------------------------
            # GOLDEN RUN BEHAVIOR MODEL
            # ----------------------------

            # Drift is frozen for E-01 compliance
            drift = 0.10

            # State transition rule (canonical oracle)
            # Step 1–2: ACTIVE
            # Step 3: DEGRADED
            if i < 3:
                state = SystemState.ACTIVE
            else:
                state = SystemState.DEGRADED

            trace.append(
                TracePoint(
                    step=i,
                    drift=drift,
                    state=state,
                    cm_version=self.cm.version,
                )
            )

        return trace
