from typing import List
from .core_types import InputPacket, TracePoint, SystemState, ConstraintMatrix


class ORPRuntime:
    def __init__(self, cm: ConstraintMatrix):
        self.cm = cm

    def _transition(self, prev_state: SystemState, packet: InputPacket, prev_drift: float):
        """
        Canonical deterministic transition function (SINGLE SOURCE OF TRUTH)
        """

        # deterministic drift model (no randomness allowed)
        drift = (
            0.5 * prev_drift +
            0.3 * packet.ambiguity +
            0.2 * packet.value
        )

        # state logic derived strictly from CM
        if drift >= self.cm.freeze_threshold:
            state = SystemState.FROZEN
        elif drift >= self.cm.drift_threshold:
            state = SystemState.DEGRADED
        else:
            state = SystemState.ACTIVE

        return drift, state

    def run_episode(self, inputs: List[InputPacket]) -> List[TracePoint]:
        trace = []

        state = SystemState.ACTIVE
        drift = 0.1

        for i, packet in enumerate(inputs, start=1):

            drift, state = self._transition(state, packet, drift)

            trace.append(
                TracePoint(
                    step=i,
                    drift=round(drift, 3),
                    state=state,
                    cm_version=self.cm.version,
                )
            )

        return trace
