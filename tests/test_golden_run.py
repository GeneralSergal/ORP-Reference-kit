from src.orp_v2_7.runtime import ORPRuntime
from src.orp_v2_7.config import CM_V2_7_BASE
from cts.cts_harness import CTS2_7


def test_orp_e01():
    system = ORPRuntime(CM_V2_7_BASE)
    cts = CTS2_7(system)
    assert cts.run()
