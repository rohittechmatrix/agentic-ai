class Event:
    def __init__(self, service, error=None, signals=None):
        self.service = service
        self.error = error
        self.signals = signals or {}