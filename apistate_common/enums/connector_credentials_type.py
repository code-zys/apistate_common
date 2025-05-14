from enum import Enum

class ConnectorCredentialsType(Enum):
    AWS_ROLE_ARN = 'AWS_ROLE_ARN'
    AWS_CREDENTIALS = 'AWS_CREDENTIALS'