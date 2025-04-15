from pydantic import BaseModel
from ..enums.permission_action import PermissionAction
from ..enums.resource_type import OrganisationResourceType, OrganisationalUnitResourceType


class OrganisationPermissionDTO(BaseModel):
    actions: list[PermissionAction]
    resource_type: OrganisationResourceType

    class Config:
        orm_mode = True


class OrganisationalUnitPermissionDTO(BaseModel):
    actions: list[PermissionAction]
    resource_type: OrganisationalUnitResourceType

    class Config:
        orm_mode = True
