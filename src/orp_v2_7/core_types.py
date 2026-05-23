from dataclasses import dataclass
from enum import Enum
from typing import Dict, Tuple


class SystemState(Enum):
    ACTIVE = "ACTIVE"
    DEGRADED = "DEGRADED"
    FROZEN = "FROZEN"


@dataclass
class InputPacket:
    value: float
    ambiguity: float


@dataclass
class TracePoint:
    step: int
    drift: float
    state: SystemState
    cm_version: str


@dataclass
class ConstraintMatrix:
    version: str
    drift_threshold: Tuple[float, float] = (0.3, 0.7)
