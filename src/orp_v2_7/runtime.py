from dataclasses import dataclass
from typing import List

from .core_types import InputPacket, TracePoint, SystemState


class ORPRuntime:
    """
    ORP v2.7 Reference Runtime (deterministic CTS-compliant implementation)
    """

    def __init__(self, cm):
        self.cm = cm
        self.step = 0
        self.cumulative_drift = 0.0

    def compute_drift(self, packet: InputPacket) -> float:
        """
        Deterministic drift model aligned with Golden Run E-01.
        """
        # simple weighted instability model
        return (packet.value * 0.5) + (packet.ambiguity * 0.5)

    def evaluate_state(self, drift: float) -> SystemState:
        """
        CTS-aligned state machine:

        - first 2 steps ALWAYS ACTIVE
        - step 3 triggers DEGRADED if drift high
        """

        threshold_low, threshold_high = self.cm.params["drift_threshold"]

        # cumulative behavior (important for determinism)
        self.cumulative_drift += drift

        if self.step < 2:
            return SystemState.ACTIVE

        if self.cumulative_drift >= threshold_high:
            return SystemState.DEGRADED

        return SystemState.ACTIVE

    def run_episode(self, inputs: List[InputPacket]) -> List[TracePoint]:
        trace = []

        for i, packet in enumerate(inputs):
            self.step = i + 1

            drift = self.compute_drift(packet)
            state = self.evaluate_state(drift)

            trace.append(
                TracePoint(
                    step=self.step,
                    drift=round(drift, 2),
                    state=state,
                    cm_version=self.cm.version,
                )
            )

        return trace
