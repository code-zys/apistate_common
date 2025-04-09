from mongoengine import StringField
from ..enums.permission_action import PermissionAction
from ..enums.resource_type import OrganisationResourceType, OrganisationalUnitResourceType
from .base import BaseEmbeddedDocument


class OrganisationPermission(BaseEmbeddedDocument):
    """
    Embedded model for Permission with action and resource fields of organisation
    """
    action = StringField(required=True, choices=[action.value for action in PermissionAction])
    resource_type = StringField(required=True, choices=[res_type.value for res_type in OrganisationResourceType])


class OrganisationalUnitPermission(BaseEmbeddedDocument):
    """
    Embedded model for Permission with action and resource fields of organisational unit
    """
    action = StringField(required=True, choices=[action.value for action in PermissionAction])
    resource_type = StringField(required=True, choices=[res_type.value for res_type in OrganisationalUnitResourceType])