from src.orp_v2_7.runtime import ORPRuntime
from src.orp_v2_7.config import CM_V2_7_BASE
from src.orp_v2_7.core_types import InputPacket

def run_minimal():
    # 1. Initialize
    system = ORPRuntime(CM_V2_7_BASE)
    
    # 2. Define single-step inputs
    inputs = [InputPacket(value=0.8, ambiguity=0.7)]
    
    # 3. Execute
    trace = system.run_episode(inputs)
    
    # 4. Observe
    for point in trace:
        print(f"Step: {point.step} | Drift: {point.drift} | State: {point.state.name}")

if __name__ == "__main__":
    run_minimal()
