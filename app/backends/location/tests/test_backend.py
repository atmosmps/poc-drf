import pytest

from app.backends.location.backend import LocationBackend


class TestLocationBackend(object):
    def test_location_backend_class_abstraction(self):
        with pytest.raises(TypeError):
            LocationBackend()
