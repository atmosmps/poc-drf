import requests
from django.conf import settings

BASE_URL = settings.IPSTACK_URL
ACCESS_KEY = settings.IPSTACK_ACCESS_KEY


class LocationClient:

    def get(self,):
        response = requests.get(
            f"{BASE_URL}/check?access_key={ACCESS_KEY}&format=1"
        )
        return response.json()

    def get_data_from_my_ip(self,):
        my_ip = self.get()['ip']

        response = requests.get(
            f"{BASE_URL}/{my_ip}?access_key={ACCESS_KEY}"
        )

        return response.json()
