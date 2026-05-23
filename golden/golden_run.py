from typing import List
from orp_v2_7.runtime import ORPRuntime
from orp_v2_7.core_types import InputPacket, ConstraintMatrix, TracePoint


def get_e01_inputs() -> List[InputPacket]:
    return [
        InputPacket(0.2, 0.1),
        InputPacket(0.5, 0.4),
        InputPacket(0.9, 0.8),
    ]


def compute_expected_trace() -> List[TracePoint]:
    """
    Golden oracle is derived from runtime (reference freeze principle).
    This ensures deterministic equivalence across CTS.
    """
    cm = ConstraintMatrix(version="CM-2.7.0")
    runtime = ORPRuntime(cm)
    return runtime.run_episode(get_e01_inputs())


# Optional extra scenarios (safe extension)

def get_e02_inputs():
    return [
        InputPacket(0.1, 0.05),
        InputPacket(0.2, 0.1),
        InputPacket(0.1, 0.2),
    ]


def compute_expected_trace_e02():
    cm = ConstraintMatrix(version="CM-2.7.0")
    runtime = ORPRuntime(cm)
    return runtime.run_episode(get_e02_inputs())


def get_e03_inputs():
    return [
        InputPacket(0.9, 0.9),
        InputPacket(0.95, 0.95),
        InputPacket(1.0, 1.0),
    ]


def compute_expected_trace_e03():
    cm = ConstraintMatrix(version="CM-2.7.0")
    runtime = ORPRuntime(cm)
    return runtime.run_episode(get_e03_inputs())
