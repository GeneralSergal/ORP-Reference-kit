from .core_types import InputPacket, TracePoint, SystemState, ConstraintMatrix


class ORPRuntime:
    def __init__(self, cm: ConstraintMatrix):
        self.cm = cm
        self.drift = 0.0

    def _compute_drift(self, packet: InputPacket) -> float:
        # deterministic toy model (IMPORTANT: must match golden)
        return round((packet.value + packet.ambiguity) / 2, 2)

    def _compute_state(self, drift: float) -> SystemState:
        low, high = self.cm.drift_threshold

        if drift < low:
            return SystemState.ACTIVE
        elif drift < high:
            return SystemState.DEGRADED
        return SystemState.FROZEN

    def run_episode(self, inputs):
        trace = []

        for i, packet in enumerate(inputs, start=1):
            drift = self._compute_drift(packet)
            self.drift = drift
            state = self._compute_state(drift)

            trace.append(
                TracePoint(
                    step=i,
                    drift=drift,
                    state=state,
                    cm_version=self.cm.version,
                )
            )

        return trace
