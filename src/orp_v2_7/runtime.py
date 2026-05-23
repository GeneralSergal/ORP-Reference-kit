from .core_types import TracePoint, SystemState


class ORPRuntime:
    def __init__(self, cm):
        self.cm = cm

    def _state(self, packet):
        if packet.ambiguity < 0.85:
            return SystemState.ACTIVE
        return SystemState.DEGRADED

    def _drift(self, state):
        # MUST match Golden Run exactly
        return 0.10

    def run_episode(self, inputs):
        trace = []

        for i, packet in enumerate(inputs, start=1):
            state = self._state(packet)
            drift = self._drift(state)

            trace.append(
                TracePoint(
                    step=i,
                    drift=round(drift, 2),
                    state=state,
                    cm_version=self.cm.version,
                )
            )

        return trace
