from orp_v2_7.runtime import ORPRuntime
from orp_v2_7.core_types import ConstraintMatrix
from cts.cts_harness import CTS2_7


def test_e01():
    cm = ConstraintMatrix(version="CM-2.7.0")
    system = ORPRuntime(cm)
    assert CTS2_7(system).run()
