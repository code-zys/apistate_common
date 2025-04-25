from mongoengine import StringField, ReferenceField, DictField, IntField
from .base import BaseOrganisationDocument
from ..enums.connection_status import ConnectionStatus

class Connection(BaseOrganisationDocument):
    """Connection model representing an active connection instance.
    """
    connector = ReferenceField('Connector')
    name = StringField(required=True)
    description = StringField()
    organisational_unit = ReferenceField('OrganisationalUnit')
    credential_options = DictField(required=True)
    last_refresh_date = IntField(default=0)
    expiration_date = IntField(default=0)
    status = StringField(required=True, choices=[status.value for status in ConnectionStatus], default=ConnectionStatus.NOT_TESTED.value)

    meta = {
        'indexes': [
            {'fields': ['name', 'organisation'], 'unique': True}
        ]
    }