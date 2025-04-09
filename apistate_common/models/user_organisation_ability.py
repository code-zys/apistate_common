from mongoengine import Document, ReferenceField, BooleanField, ListField
from ..enums.organisation_permission import OrganisationPermission
from .base import BaseOrganisationDocument
from .permission import OrganisationPermission

class UserOrganisationAbility(BaseOrganisationDocument):
    user = ReferenceField('User', required=True)
    permissions = ListField(ReferenceField(OrganisationPermission), default=[], required=True)
    
    meta = {
        'collection': 'user_organisation_abilities',
        'indexes': [
            {'fields': ['user', 'organisation'], 'unique': True}
        ]
    }
