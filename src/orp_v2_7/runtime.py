from .core_types import TracePoint, SystemState
from .protected_cm import ProtectedCM


class ORPRuntime:
    def __init__(self, cm):
        self.cm = ProtectedCM(cm)
        self.trace = []

    def run_episode(self, inputs):
        self.trace = []

        for i, inp in enumerate(inputs, start=1):
            drift = self._compute_drift(inp)
            state = self._compute_state(drift)

            self.trace.append(
                TracePoint(
                    step=i,
                    drift=round(drift, 2),
                    state=state,
                    cm_version=self.cm.version,
                )
            )

        return self.trace

    def _compute_drift(self, inp):
        return inp.value * 0.1 + inp.ambiguity * 0.05

    def _compute_state(self, drift):
        low, high = self.cm.params["drift_threshold"]

        if drift < low:
            return SystemState.ACTIVE
        elif drift < high:
            return SystemState.ACTIVE
        else:
            return SystemState.DEGRADED
