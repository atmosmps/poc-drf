from unittest import mock

from app.location.extensions import IPStackBackend


class TestIPStackBackend(object):
    backend = IPStackBackend()

    @mock.patch("app.location.extensions.IPStackBackend.client")
    def test_should_returns_data_from_my_ip_successfully(
        self, client_mock, ip_stack_http_client_successfully_response
    ):
        client_mock.return_value = ip_stack_http_client_successfully_response
        response = self.backend.get_data_from_my_ip()
        assert response
