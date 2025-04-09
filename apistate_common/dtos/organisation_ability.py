from typing import List
from pydantic import BaseModel
from ..enums.organisation_permission import OrganisationPermission

class OrganisationAbilityUpdateRequest(BaseModel):
    permissions: List[OrganisationPermission]