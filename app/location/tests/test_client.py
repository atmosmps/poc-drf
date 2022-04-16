import json
from unittest import mock

from app.location.client import IPStackHttpClient
from django.conf import settings


class TestLocationClientGetCheck(object):
    URL = settings.IPSTACK_URL
    ACCESS_KEY = settings.IPSTACK_API_KEY

    client = IPStackHttpClient()

    @mock.patch("src.location.client.IPStackHttpClient._build_endpoint")
    def test_that_response_invalid_ip_address_when_a_invalid_ip_is_provided(
        self, build_endpoint_mock
    ):
        expected_info_message = "The IP Address supplied is invalid."
        build_endpoint_mock.return_value = (
            f"{self.URL}/some-ip-address?access_key={self.ACCESS_KEY}&format=1"
        )
        response = self.client.get_check()
        response_data = json.loads(response.text)

        assert response.status_code == 200
        assert not response_data["success"]
        assert "error" in response_data
        assert response_data["error"]["code"] == 106
        assert response_data["error"]["type"] == "invalid_ip_address"
        assert response_data["error"]["info"] == expected_info_message

    @mock.patch("src.location.client.LocationClient._build_endpoint")
    def test_that_does_not_find_a_non_valid_resource(self, build_endpoint_mock):
        build_endpoint_mock.return_value = (
            f"{self.URL}/check/some-resource?access_key={self.ACCESS_KEY}"
        )
        response = self.client.get_check()
        response_data = json.loads(response.text)

        assert response.status_code == 200
        assert response_data["detail"] == "Not Found"
