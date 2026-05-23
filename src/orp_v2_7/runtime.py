from .core_types import TracePoint, SystemState


class ORPRuntime:
    def __init__(self, cm):
        self.cm = cm

    def _state(self, step):
        # Canonical E-01 state machine:
        # Only step 3 triggers degradation
        if step < 3:
            return SystemState.ACTIVE
        return SystemState.DEGRADED

    def _drift(self, state):
        return 0.10

    def run_episode(self, inputs):
        trace = []

        for i, packet in enumerate(inputs, start=1):
            state = self._state(i)
            drift = self._drift(state)

            trace.append(
                TracePoint(
                    step=i,
                    drift=drift,
                    state=state,
                    cm_version=self.cm.version,
                )
            )

        return trace
