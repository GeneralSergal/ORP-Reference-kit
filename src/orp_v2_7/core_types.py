from dataclasses import dataclass
from enum import Enum, auto
from typing import Dict, List


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
