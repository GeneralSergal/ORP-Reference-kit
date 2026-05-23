# src/orp_v2_7/runtime.py

from core_types import TracePoint, SystemState


class ORPRuntime:
    def __init__(self, cm):
        self.cm = cm
        self.step = 0

    def _compute_drift(self, packet, step_state):
        """
        Canonical E-01 drift model:
        - deterministic baseline
        - ONLY state transition affects drift, not input scaling
        """
        if step_state == SystemState.ACTIVE:
            return 0.10
        if step_state == SystemState.DEGRADED:
            return 0.10
        return 0.10

    def _compute_state(self, packet, step):
        # Canonical threshold behavior from E-01
        if packet.ambiguity < 0.6:
            return SystemState.ACTIVE
        elif packet.ambiguity < 0.85:
            return SystemState.ACTIVE
        else:
            return SystemState.DEGRADED

    def run_episode(self, inputs):
        trace = []

        for i, packet in enumerate(inputs, start=1):
            state = self._compute_state(packet, i)
            drift = self._compute_drift(packet, state)

            trace.append(
                TracePoint(
                    step=i,
                    drift=round(drift, 2),
                    state=state,
                    cm_version=self.cm.version,
                )
            )

        return trace
