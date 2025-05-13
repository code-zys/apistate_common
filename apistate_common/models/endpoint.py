from .base import BaseOrganisationDocument
from mongoengine import StringField, ReferenceField
from apistate_common.enums.endpoint_method_type import EndpointMethodType

class Endpoint(BaseOrganisationDocument):
    """Endpoint model representing an API endpoint.
    """
    url = StringField()
    method = StringField(choices=EndpointMethodType.values())
    environment = ReferenceField('Environment')
    api = ReferenceField('API')

    meta = {
        'indexes': [
            {'fields': ['url', 'method', 'environment'], 'unique': True}
        ]
    }