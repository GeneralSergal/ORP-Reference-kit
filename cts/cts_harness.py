from golden.golden_run import GOLDEN_CASES


class CTS2_7:
    def __init__(self, runtime):
        self.runtime = runtime

    def run(self):
        for name, (inputs_fn, expected_fn) in GOLDEN_CASES.items():

            inputs = inputs_fn()
            expected = expected_fn()
            actual = self.runtime.run_episode(inputs)

            assert len(actual) == len(expected), f"{name}: length mismatch"

            for a, e in zip(actual, expected):
                assert a.step == e.step, f"{name}: step mismatch"
                assert a.state == e.state, f"{name}: state mismatch"
                assert abs(a.drift - e.drift) < 0.05, f"{name}: drift mismatch"

        return True
