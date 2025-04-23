from mongoengine import StringField, ReferenceField, DictField
from .base import BaseOrganisationDocument

class Connection(BaseOrganisationDocument):
    """Connection model representing an active connection instance.
    """
    connector = ReferenceField('Connector')
    name = StringField()
    organisation_unit = ReferenceField('OrganisationUnit')
    credential_options = DictField(required=True)

    meta = {
        'indexes': [
            {'fields': ['name', 'organisation'], 'unique': True}
        ]
    }