from mongoengine import Document, ReferenceField, BooleanField, ListField, EmbeddedDocumentField
from .base import BaseOrganisationDocument
from .permission import OrganisationalUnitPermission

class UserOrganisationalUnitAbility(BaseOrganisationDocument):
    user = ReferenceField('User', required=True)
    permissions = ListField(EmbeddedDocumentField(OrganisationalUnitPermission), default=[], required=True)
    organisational_unit = ReferenceField('OrganisationalUnit', required=True)
    
    meta = {
        'collection': 'user_organisation_unit_abilities',
        'indexes': [
            {'fields': ['user', 'organisation'], 'unique': True}
        ]
    }
