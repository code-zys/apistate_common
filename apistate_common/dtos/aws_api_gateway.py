from pydantic import BaseModel

class AWSAPIGatewayCredentials(BaseModel):
    """AWS API Gateway specific credentials model."""
    access_key_id: str
    secret_access_key: str
class AWSAPIGatewayRoleArnCredentials(BaseModel):
    """AWS API Gateway specific credentials model using role ARN."""
    role_arn: str