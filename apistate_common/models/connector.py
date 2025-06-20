from mongoengine import StringField, ReferenceField, ListField, DictField, IntField
from .base import BaseOrganisationDocument
from ..enums.connector_status import ConnectorStatus

class Connector(BaseOrganisationDocument):
    """Connector model representing a connection configuration.
    """
    name = StringField(required=True)
    code = StringField(required=True)
    logo = StringField()
    host_url = StringField()
    status = StringField(choices=[c.value for c in ConnectorStatus], default=ConnectorStatus.NOT_AVAILABLE.value)
    date_status = IntField(required=True, default=0)
    credential_options = ListField(DictField(), default=[])

    meta = {
        'indexes': [
            {'fields': ['name', 'organisation'], 'unique': True},
            {'fields': ['code', 'organisation'], 'unique': True}
        ],
        'collection': 'connectors'
    }