from pydantic import BaseModel

class AWSAPIGatewayCredentials(BaseModel):
    """AWS API Gateway specific credentials model."""
    access_key_id: str
    secret_access_key: str
    region: str