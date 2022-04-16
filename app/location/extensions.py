import requests
from app.backends.location.backend import LocationBackend
from app.location.client import IPStackHttpClient


class IPStackBackend(LocationBackend):

    client = IPStackHttpClient()

    def get_data_from_my_ip(self):
        my_ip = self.client.get()["ip"]
        response = requests.get(url=self._build_endpoint(resource=my_ip))
        return response.json()
