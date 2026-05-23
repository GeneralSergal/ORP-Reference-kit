from dataclasses import dataclass
from enum import Enum, auto
from typing import Dict, Tuple


class SystemState(Enum):
    ACTIVE = auto()
    DEGRADED = auto()
    FROZEN = auto()


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
    params: Dict[str, Tuple[float, float]]
