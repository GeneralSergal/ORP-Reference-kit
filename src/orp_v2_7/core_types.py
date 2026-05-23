from dataclasses import dataclass
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


@dataclass(frozen=True)
class ConstraintMatrix:
    version: str
    drift_threshold: float = 0.6
    freeze_threshold: float = 0.85
