from typing import List, Optional
from pydantic import BaseModel
from .permission import OrganisationPermissionDTO

class OrganisationAbilityUpdateRequest(BaseModel):
    permissions: Optional[List[OrganisationPermissionDTO]] = []