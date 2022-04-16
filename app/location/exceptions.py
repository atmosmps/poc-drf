from app.backends.location.exceptions import LocationBackendException


class UnableToGetDataDueAPIHttpException(LocationBackendException):
    ...


class UnableToGetDataDueTimeoutException(LocationBackendException):
    ...
