class LocationBackendException(Exception):
    def __init__(self, message=None):
        self.message = message
