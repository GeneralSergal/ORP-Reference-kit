from dataclasses import dataclass
from typing import List
from enum import Enum, auto


class SystemState(Enum):
    ACTIVE = auto()
    DEGRADED = auto()
    FROZEN = auto()


@dataclass(frozen=True)
class InputPacket:
    value: float
    ambiguity: float


@dataclass(frozen=True)
class TracePoint:
    step: int
    drift: float
    state: SystemState
    cm_version: str


CM_V2_7 = "CM-2.7.0"


# ------------------------------------------------------------
# E-01: Baseline stability → mild drift → degradation trigger
# ------------------------------------------------------------
def get_e01_inputs() -> List[InputPacket]:
    return [
        InputPacket(0.2, 0.1),
        InputPacket(0.5, 0.4),
        InputPacket(0.9, 0.8),
    ]


def expected_e01() -> List[TracePoint]:
    return [
        TracePoint(1, 0.10, SystemState.ACTIVE, CM_V2_7),
        TracePoint(2, 0.20, SystemState.ACTIVE, CM_V2_7),
        TracePoint(3, 0.80, SystemState.DEGRADED, CM_V2_7),
    ]


# ------------------------------------------------------------
# E-02: Stable low-entropy loop (no degradation expected)
# ------------------------------------------------------------
def get_e02_inputs() -> List[InputPacket]:
    return [
        InputPacket(0.1, 0.05),
        InputPacket(0.15, 0.05),
        InputPacket(0.2, 0.05),
    ]


def expected_e02() -> List[TracePoint]:
    return [
        TracePoint(1, 0.05, SystemState.ACTIVE, CM_V2_7),
        TracePoint(2, 0.06, SystemState.ACTIVE, CM_V2_7),
        TracePoint(3, 0.07, SystemState.ACTIVE, CM_V2_7),
    ]


# ------------------------------------------------------------
# E-03: High ambiguity spike → immediate degradation
# ------------------------------------------------------------
def get_e03_inputs() -> List[InputPacket]:
    return [
        InputPacket(0.3, 0.2),
        InputPacket(0.4, 0.9),  # spike
        InputPacket(0.5, 0.95),
    ]


def expected_e03() -> List[TracePoint]:
    return [
        TracePoint(1, 0.20, SystemState.ACTIVE, CM_V2_7),
        TracePoint(2, 0.90, SystemState.DEGRADED, CM_V2_7),
        TracePoint(3, 0.95, SystemState.DEGRADED, CM_V2_7),
    ]


# ------------------------------------------------------------
# Registry (single entry point for CTS)
# ------------------------------------------------------------
GOLDEN_CASES = {
    "E01": (get_e01_inputs, expected_e01),
    "E02": (get_e02_inputs, expected_e02),
    "E03": (get_e03_inputs, expected_e03),
}
