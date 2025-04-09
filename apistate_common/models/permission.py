from pydantic import BaseModel
from typing import Optional
from ..enums.permission_action import PermissionAction
from ..enums.resource_type import OrganisationResourceType, OrganisationalUnitResourceType
from .base import BaseEmbeddedDocument

class OrganisationPermission(BaseEmbeddedDocument):
    """
    Embedded model for Permission with action and resource fields of organisation
    """
    action: PermissionAction
    resource_type: OrganisationResourceType


class OrganisationalUnitPermission(BaseEmbeddedDocument):
    """
    Embedded model for Permission with action and resource fields of organisational unit
    """
    action: PermissionAction
    resource_type: OrganisationalUnitResourceType