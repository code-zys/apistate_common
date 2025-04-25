from mongoengine import StringField, ReferenceField, DictField, IntField
from .base import BaseOrganisationDocument

class Connection(BaseOrganisationDocument):
    """Connection model representing an active connection instance.
    """
    connector = ReferenceField('Connector')
    name = StringField(required=True)
    description = StringField()
    organisation_unit = ReferenceField('OrganisationUnit')
    credential_options = DictField(required=True)
    last_refresh_date = IntField(default=0)
    expiration_date = IntField(default=0)

    meta = {
        'indexes': [
            {'fields': ['name', 'organisation'], 'unique': True}
        ]
    }