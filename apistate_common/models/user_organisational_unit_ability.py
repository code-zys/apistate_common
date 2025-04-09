from mongoengine import Document, ReferenceField, BooleanField
from .base import BaseOrganisationDocument
from .permission import OrganisationalUnitPermission

class UserOrganisationalUnitAbility(BaseOrganisationDocument):
    user = ReferenceField('User', required=True)
    permissions = ListField(ReferenceField(OrganisationalUnitPermission), default=[], required=True)
    
    meta = {
        'collection': 'user_organisation_abilities',
        'indexes': [
            {'fields': ['user', 'organisation'], 'unique': True}
        ]
    }
