from src.orp_v2_7.runtime import ORPRuntime
from src.orp_v2_7.config import CM_V2_7_BASE
from src.orp_v2_7.core_types import InputPacket

def run_stress():
    system = ORPRuntime(CM_V2_7_BASE)
    
    # Sequence designed to cross the 0.7 threshold
    inputs = [
        InputPacket(0.1, 0.1), # Low
        InputPacket(9.0, 0.0), # High (forces DEGRADED)
    ]
    
    trace = system.run_episode(inputs)
    for point in trace:
        print(f"Status at step {point.step}: {point.state.name} (Drift: {point.drift})")

if __name__ == "__main__":
    run_stress()
