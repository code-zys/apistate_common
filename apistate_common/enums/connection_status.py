from enum import Enum

class ConnectionStatus(Enum):
    """Enum representing the status of a connection.
    """
    SUCCESSFUL = "SUCCESSFUL"
    DISABLED = "DISABLED"
    FAILED = "FAILED"
    NOT_TESTED = "NOT_TESTED"