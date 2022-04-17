import json

from app.backends.location.backend import LocationBackend
from app.location.client import IPStackHttpClient


class IPStackBackend(LocationBackend):

    client = IPStackHttpClient()

    def get_data_from_my_ip(self):
        response = self.client.get_ip_lookup()
        ip_lookup = json.loads(response.text)
        return ip_lookup
