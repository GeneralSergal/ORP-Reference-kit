from golden.golden_run import get_e01_inputs, compute_expected_trace


class CTS2_7:
    def __init__(self, runtime):
        self.runtime = runtime

    def run(self):
        inputs = get_e01_inputs()
        expected = compute_expected_trace()
        actual = self.runtime.run_episode(inputs)

        assert len(actual) == len(expected)

        for a, e in zip(actual, expected):
            assert a.step == e.step
            assert a.state == e.state
            assert abs(a.drift - e.drift) < 0.01

        return True
