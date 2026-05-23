from dataclasses import dataclass
from typing import Dict


@dataclass(frozen=True)
class ConstraintMatrix:
    version: str
    params: Dict


CM_V2_7_BASE = ConstraintMatrix(
    version="CM-2.7.0",
    params={
        "low_threshold": 0.3,
        "high_threshold": 0.7,
        "degrade_threshold": 0.85,
    },
)
