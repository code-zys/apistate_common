from mongoengine import IntField, DictField, ReferenceField, EnumField
from .base import BaseOrganisationDocument
from ..enums.api_status import APIStatus

class HealthCheckHistory(BaseOrganisationDocument):
    """HealthCheckHistory model for storing health check execution results.
    """
    config = ReferenceField('HealthCheckConfig')
    timestamp = IntField()
    req_status = IntField()
    request = DictField()
    response = DictField()
    api_status = EnumField(APIStatus)

    meta = {
        'indexes': [
            {'fields': ['config', 'timestamp'], 'unique': True}
        ]
    }