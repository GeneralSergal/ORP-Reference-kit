from golden.golden_run import (
    get_e01_inputs, compute_expected_trace,
    get_e02_inputs, compute_expected_trace_e02,
    get_e03_inputs, compute_expected_trace_e03
)


class CTS2_7:
    def __init__(self, runtime):
        self.runtime = runtime

        self.GOLDEN_CASES = {
            "E01": (get_e01_inputs, compute_expected_trace),
            "E02": (get_e02_inputs, compute_expected_trace_e02),
            "E03": (get_e03_inputs, compute_expected_trace_e03),
        }

    def run(self):
        for name, (inputs_fn, expected_fn) in self.GOLDEN_CASES.items():

            inputs = inputs_fn()
            expected = expected_fn()
            actual = self.runtime.run_episode(inputs)

            assert len(actual) == len(expected), f"{name}: length mismatch"

            for a, e in zip(actual, expected):
                assert a.step == e.step, f"{name}: step mismatch"
                assert a.state == e.state, f"{name}: state mismatch"
                assert abs(a.drift - e.drift) < 0.01, f"{name}: drift mismatch"

        return True
