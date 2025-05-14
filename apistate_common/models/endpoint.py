from .base import BaseOrganisationDocument
from mongoengine import StringField, ReferenceField, ListField, DictField
from apistate_common.enums.endpoint_method_type import EndpointMethodType

class Endpoint(BaseOrganisationDocument):
    """Endpoint model representing an API endpoint.
    """
    path = StringField(required=True)  # Changed from url to path to match DTO
    method = StringField(choices=[e.value for e in EndpointMethodType])
    resource_id = StringField(required=True)  # Added to match DTO
    query_params = ListField(StringField())  # Added to match DTO
    path_params = ListField(StringField())  # Added to match DTO
    body_type = DictField()  # Added to match DTO
    metadata = DictField()  # Added to match DTO
    description = StringField()  # Added to match DTO
    environment = ReferenceField('Environment')
    api = ReferenceField('API')

    meta = {
        'indexes': [
            {'fields': ['path', 'method', 'environment'], 'unique': True}  # Updated url to path in index
        ]
    }