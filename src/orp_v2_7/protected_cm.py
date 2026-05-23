class ProtectedCM:
    def __init__(self, cm):
        self._cm = cm
        self._history = [cm]

    @property
    def params(self):
        return self._cm.params

    @property
    def version(self):
        return self._cm.version

    def commit(self, new_cm):
        self._history.append(new_cm)
        self._cm = new_cm

    def rollback(self):
        if len(self._history) > 1:
            self._history.pop()
            self._cm = self._history[-1]

    def __setattr__(self, key, value):
        if key in {"_cm", "params"} and hasattr(self, "_cm"):
            raise AttributeError("I1 VIOLATION: CM is immutable outside GCP")
        super().__setattr__(key, value)
