import json
import logging
import requests

from app.location.constants import ACCESS_KEY, HTTP_URL
from app.location.exceptions import (
    UnableToGetDataDueAPIHttpException,
    UnableToGetDataDueTimeoutException,
)

logger = logging.getLogger(__name__)


class IPStackHttpClient:
    def _build_endpoint(self, resource: str) -> str:
        return f"{HTTP_URL}/{resource}?access_key={ACCESS_KEY}&format=1"

    def get_check(self):
        try:
            response = requests.get(url=self._build_endpoint(resource="check"))
            return response

        except requests.exceptions.Timeout as e:
            logger.exception(f"[LocationClient] Raised exception: {str(e)}")
            raise UnableToGetDataDueTimeoutException(str(e))

        except requests.exceptions.RequestException as e:
            logger.exception(f"[LocationClient] Raised exception: {str(e)}")
            raise UnableToGetDataDueAPIHttpException(str(e))

    def get_ip_lookup(self):
        check = self.get_check()
        ip = json.loads(check.text)["ip"]
        try:
            response = requests.get(url=self._build_endpoint(resource=ip))
            return response
        except requests.exceptions.RequestException as e:
            logger.exception(f"[LocationClient] Raised exception: {str(e)}")
            raise UnableToGetDataDueAPIHttpException(str(e))

    def get_bulk_ip_lookup(self):
        ...
