from mongoengine import IntField, StringField, ListField, ReferenceField, EmbeddedDocumentField
from .base import BaseOrganisationDocument
from .request_body_check import RequestBodyCheck

class HealthCheckConfig(BaseOrganisationDocument):
    """HealthCheckConfig model for configuring API health checks.
    """
    endpoint = ReferenceField('Endpoint', null=True)
    cron = StringField()
    status_code = IntField()
    body_checks = ListField(EmbeddedDocumentField(RequestBodyCheck))
    api = ReferenceField('API')
    query_params_data = DictField()
    path_params_data = DictField()

    meta = {
        'indexes': [
            {'fields': ['api', 'endpoint'], 'unique': True}
        ]
    }