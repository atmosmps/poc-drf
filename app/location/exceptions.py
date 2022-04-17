from app.backends.location.exceptions import LocationBackendException


class UnableToGetDataDueTimeoutException(LocationBackendException):
    ...


class UnableToGetDataDueAPIHttpException(LocationBackendException):
    ...
