import json
from cgitb import text
from unittest import mock

import pytest
import requests
from app.location.client import IPStackHttpClient
from app.location.exceptions import (
    UnableToGetDataDueAPIHttpException,
    UnableToGetDataDueTimeoutException,
)
from app.location.tests.conftest import response_usage_limit_reached_data

from ..constants import ACCESS_KEY, HTTP_URL, HTTPS_URL

LOGGER_NAME = "app.location.client"

client = IPStackHttpClient()
response = client.get_check()


class TestGlobalErrorsResponsesFromIPStack:
    @mock.patch("app.location.client.IPStackHttpClient._build_endpoint")
    def test_that_raise_missing_access_key_when_access_key_is_not_provided(
        self, build_endpoint_mock
    ):
        response_message = "You have not supplied an API Access Key. [Required format: access_key=YOUR_ACCESS_KEY]"
        build_endpoint_mock.return_value = f"{HTTP_URL}/check?access_key="
        response_data = json.loads(response.text)

        assert response.status_code == 200
        assert not response_data["success"]
        assert "error" in response_data
        assert response_data["error"]["code"] == 101
        assert response_data["error"]["type"] == "missing_access_key"
        assert response_data["error"]["info"] == response_message

    @mock.patch("app.location.client.IPStackHttpClient._build_endpoint")
    def test_that_raise_missing_access_key_when_access_key_filter_url_is_not_provided(
        self, build_endpoint_mock
    ):
        response_message = "You have not supplied an API Access Key. [Required format: access_key=YOUR_ACCESS_KEY]"
        build_endpoint_mock.return_value = f"{HTTP_URL}/check"
        response_data = json.loads(response.text)

        assert response.status_code == 200
        assert not response_data["success"]
        assert "error" in response_data
        assert response_data["error"]["code"] == 101
        assert response_data["error"]["type"] == "missing_access_key"
        assert response_data["error"]["info"] == response_message

    @mock.patch("app.location.client.IPStackHttpClient._build_endpoint")
    def test_that_response_invalid_ip_address_when_a_invalid_ip_is_provided(
        self, build_endpoint_mock
    ):
        expected_info_message = "The IP Address supplied is invalid."
        build_endpoint_mock.return_value = (
            f"{HTTP_URL}/some-ip-address?access_key={ACCESS_KEY}&format=1"
        )
        response_data = json.loads(response.text)

        assert response.status_code == 200
        assert not response_data["success"]
        assert "error" in response_data
        assert response_data["error"]["code"] == 106
        assert response_data["error"]["type"] == "invalid_ip_address"
        assert response_data["error"]["info"] == expected_info_message

    @mock.patch("app.location.client.IPStackHttpClient._build_endpoint")
    def test_that_does_not_find_a_non_valid_resource(self, build_endpoint_mock):
        build_endpoint_mock.return_value = (
            f"{HTTP_URL}/check/some-resource?access_key={ACCESS_KEY}"
        )
        response_data = json.loads(response.text)

        assert response.status_code == 200
        assert response_data["detail"] == "Not Found"

    @mock.patch("app.location.client.IPStackHttpClient._build_endpoint")
    def test_that_raise_invalid_fields_when_a_invalid_field_is_provided(
        self, build_endpoint_mock
    ):
        response_message = (
            "One or more invalid fields were specified using the fields parameter."
        )
        build_endpoint_mock.return_value = (
            f"{HTTP_URL}/check?access_key={ACCESS_KEY}&fields=invalid_fied"
        )
        response_data = json.loads(response.text)

        assert response.status_code == 200
        assert not response_data["success"]
        assert "error" in response_data
        assert response_data["error"]["code"] == 301
        assert response_data["error"]["type"] == "invalid_fields"
        assert response_data["error"]["info"] == response_message

    @mock.patch("app.location.client.IPStackHttpClient._build_endpoint")
    def test_that_raise_https_access_restricted_when_a_secure_protocol_is_provided(
        self, build_endpoint_mock
    ):
        response_message = "Access Restricted - Your current Subscription Plan does not support HTTPS Encryption."
        build_endpoint_mock.return_value = f"{HTTPS_URL}/check?access_key={ACCESS_KEY}"
        response_data = json.loads(response.text)

        assert response.status_code == 200
        assert not response_data["success"]
        assert "error" in response_data
        assert response_data["error"]["code"] == 105
        assert response_data["error"]["type"] == "https_access_restricted"
        assert response_data["error"]["info"] == response_message

    def test_that_usage_limit_reached_when_a_limit_request_is_reaching(
        self, requests_mock
    ):
        response_text = {
            "success": False,
            "error": {
                "code": 104,
                "type": "usage_limit_reached",
                "info": "Your monthly usage limit has been reached. Please upgrade your Subscription Plan.",
            },
        }
        status_code = 200
        endpoint = client._build_endpoint(resource="check")

        requests_mock.get(endpoint, status_code=status_code, json=response_text)

        response = client.get_check()
        response_data = json.loads(response.text)

        assert response.status_code == 200
        assert not response_data["success"]
        assert "error" in response_data
        assert response_data["error"]["code"] == response_text["error"]["code"]
        assert response_data["error"]["type"] == response_text["error"]["type"]
        assert response_data["error"]["info"] == response_text["error"]["info"]


class TestLocationClientGetCheck:
    def test_should_raise_unable_to_get_data_due_timeout_exception(
        self, requests_mock, log_capture
    ):
        response_message: str = "Request Timeout"
        endpoint = client._build_endpoint(resource="check")
        requests_mock.get(endpoint, exc=requests.exceptions.Timeout(response_message))

        with pytest.raises(UnableToGetDataDueTimeoutException) as ex:
            client.get_check()

        assert ex.value.message == response_message
        assert requests_mock.called
        log_capture.check_present(
            *(
                (
                    LOGGER_NAME,
                    "ERROR",
                    f"[LocationClient] Raised exception: {str(response_message)}",
                ),
            )
        )

    def test_should_raise_unable_to_get_data_due_http_exception(
        self, requests_mock, log_capture
    ):
        response_message: str = "Internal Server Error"
        endpoint = client._build_endpoint(resource="check")
        requests_mock.get(
            endpoint, exc=requests.exceptions.RequestException(response_message)
        )

        with pytest.raises(UnableToGetDataDueAPIHttpException) as ex:
            client.get_check()

        assert ex.value.message == response_message
        assert requests_mock.called
        log_capture.check_present(
            *(
                (
                    LOGGER_NAME,
                    "ERROR",
                    f"[LocationClient] Raised exception: {str(response_message)}",
                ),
            )
        )

    def test_should_return_ip_data_successfully(self, requests_mock):
        ...
