from enum import Enum

class ResponseStatus(Enum):
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"
    PENDING = "PENDING"
    UNKNOWN = "UNKNOWN"