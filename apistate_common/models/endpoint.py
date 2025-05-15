from .base import BaseOrganisationDocument
from mongoengine import StringField, ReferenceField, ListField, DictField
from apistate_common.enums.endpoint_method_type import EndpointMethodType

class Endpoint(BaseOrganisationDocument):
    """Endpoint model representing an API endpoint.
    """
    path = StringField(required=True)
    method = StringField(choices=[e.value for e in EndpointMethodType])
    resource_id = StringField()
    query_params = ListField(StringField())
    path_params = ListField(StringField())
    body_type = DictField()
    metadata = DictField()
    description = StringField()
    api = ReferenceField('API', required=True)

    meta = {
        'indexes': [
            {'fields': ['organisation', 'api', 'path', 'method', 'environment'], 'unique': True}  # Updated url to path in index
        ]
    }