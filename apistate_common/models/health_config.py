from mongoengine import IntField, StringField, ListField, ReferenceField, EmbeddedDocumentField, DictField
from .base import BaseOrganisationDocument
from .request_body_check import RequestBodyCheck

class HealthCheckConfig(BaseOrganisationDocument):
    endpoint = ReferenceField('Endpoint', required=True)
    cron = StringField()
    api = ReferenceField('API', required=True)
    query_params_data = DictField()
    path_params_data = DictField()

    meta = {
        'indexes': [
            {'fields': ['api', 'endpoint'], 'unique': True}
        ]
    }