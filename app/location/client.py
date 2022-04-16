import logging

import requests
from app.location.exceptions import (
    UnableToGetDataDueAPIHttpException,
    UnableToGetDataDueTimeoutException,
)
from django.conf import settings

logger = logging.getLogger(__name__)


class IPStackHttpClient:
    URL = settings.IPSTACK_URL
    ACCESS_KEY = settings.IPSTACK_API_KEY

    def _build_endpoint(self, resource: str) -> str:
        return f"{self.URL}/{resource}?access_key={self.ACCESS_KEY}&format=1"

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
        ...

    def get_bulk_ip_lookup(self):
        ...
