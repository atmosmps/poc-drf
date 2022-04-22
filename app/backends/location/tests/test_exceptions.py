from app.backends.location.exceptions import LocationBackendException


class TestLocationBackendException:
    def test_init_method(self):
        message = "some gibberish"
        exception = LocationBackendException(message=message)
        assert exception.message == message
