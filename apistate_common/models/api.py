from mongoengine import StringField, ReferenceField, DictField, EmbeddedDocumentField, ListField, EmbeddedDocument
from .base import BaseOrganisationDocument
from ..enums.api_status import APIStatus

class BodyCheck(EmbeddedDocument):
    """Embedded document for health check body validation rules."""
    path = StringField(required=True)
    operator = StringField(required=True)
    value = StringField(required=True)

class StatusMapping(EmbeddedDocument):
    """Embedded document for health check status mapping."""
    status_codes = ListField(StringField())
    body_checks = ListField(EmbeddedDocumentField(BodyCheck))

class APIHealthCheck(EmbeddedDocument):
    """Embedded document for API health check configuration."""
    path = StringField(required=True)
    method = StringField(required=True)
    params = DictField()
    interval = StringField(required=True)
    status_mapping = DictField(field=EmbeddedDocumentField(StatusMapping))

class APIConnection(EmbeddedDocument):
    """Embedded document for API connection configuration."""
    connection_id = StringField(required=True)
    connection_data = DictField()

class SwaggerConnection(EmbeddedDocument):
    """Embedded document for swagger configuration."""
    connection_id = StringField(required=True)
    connection_data = DictField()

class API(BaseOrganisationDocument):
    """API model representing an API within a project."""
    name = StringField(required=True)
    version = StringField()
    api_connection = EmbeddedDocumentField(APIConnection, required=True)
    region = StringField(required=True)
    external_id = StringField(required=True)
    swagger_connection = EmbeddedDocumentField(SwaggerConnection)
    health_check = EmbeddedDocumentField(APIHealthCheck)  # Renamed from health_check_config to match JSON
    project = ReferenceField('Project')
    connection = ReferenceField('Connection', required=True)
    connector = ReferenceField('Connector', required=True)
    status = StringField(required=True, choices=[api_status.value for api_status in APIStatus], default=APIStatus.NOT_SYNCHRONIZED.value)
    error_message = StringField()
    
    meta = {
        'indexes': [
            {'fields': ['name', 'organisation'], 'unique': True}
        ],
        'collection': 'apis'
    }