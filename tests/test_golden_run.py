from orp_v2_7.runtime import ORPRuntime
from orp_v2_7.config import CM_V2_7_BASE
from orp_v2_7.cts_harness import CTS2_7

def test_e01():
    system = ORPRuntime(CM_V2_7_BASE)
    assert CTS2_7(system).run()
