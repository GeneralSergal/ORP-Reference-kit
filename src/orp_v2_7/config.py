from .core_types import ConstraintMatrix

CM_V2_7_BASE = ConstraintMatrix(
    version="CM-2.7.0",
    params={
        "drift_threshold": (0.3, 0.7),
        "hysteresis": (1, 3),
    },
)
