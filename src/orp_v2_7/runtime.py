from typing import List
from .core_types import InputPacket, TracePoint, SystemState, ConstraintMatrix


class ORPRuntime:
    def __init__(self, cm: ConstraintMatrix):
        self.cm = cm

    def _compute_drift(self, prev_drift: float, packet: InputPacket) -> float:
        # deterministic model (single source of truth)
        return (
            0.5 * prev_drift +
            0.3 * packet.ambiguity +
            0.2 * packet.value
        )

    def _compute_state(self, drift: float) -> SystemState:
        if drift >= self.cm.freeze_threshold:
            return SystemState.FROZEN
        elif drift >= self.cm.drift_threshold:
            return SystemState.DEGRADED
        return SystemState.ACTIVE

    def run_episode(self, inputs: List[InputPacket]) -> List[TracePoint]:
        trace = []
        drift = 0.1

        for i, packet in enumerate(inputs, start=1):
            drift = self._compute_drift(drift, packet)
            state = self._compute_state(drift)

            trace.append(
                TracePoint(
                    step=i,
                    drift=round(drift, 6),
                    state=state,
                    cm_version=self.cm.version,
                )
            )

        return trace
