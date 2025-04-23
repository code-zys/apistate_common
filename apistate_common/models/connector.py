from mongoengine import StringField, ReferenceField
from .base import BaseOrganisationDocument

class Connector(BaseOrganisationDocument):
    """Connector model representing a connection configuration.
    """
    name = StringField(required=True)
    code = StringField(required=True)
    logo = StringField()
    health_check_endpoint = StringField()
    credential_options = ListField(DictField(), default=list)

    meta = {
        'indexes': [
            {'fields': ['name', 'organisation'], 'unique': True},
            {'fields': ['code', 'organisation'], 'unique': True}
        ],
        'collection': 'connectors'
    }