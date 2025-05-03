from pydantic import BaseModel

class ApigeeCredentials(BaseModel):
    """Apigee specific credentials model."""
    username: str
    password: str
    organization: str
    environment: str