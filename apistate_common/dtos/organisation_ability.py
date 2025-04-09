from typing import List
from pydantic import BaseModel
from .permission import OrganisationPermissionDTO

class OrganisationAbilityUpdateRequest(BaseModel):
    permissions: List[OrganisationPermissionDTO]