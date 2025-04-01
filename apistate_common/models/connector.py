from mongoengine import StringField, ReferenceField
from base import BaseOrganisationDocument

class Connector(BaseOrganisationDocument):
    """Connector model representing a connection configuration.
    """
    name = StringField()
    code = StringField()

    meta = {
        'indexes': [
            {'fields': ['name', 'organisation'], 'unique': True},
            {'fields': ['code', 'organisation'], 'unique': True}
        ]
    }