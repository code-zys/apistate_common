from mongoengine import DateTimeField, IntField, DictField, ReferenceField, EnumField, ListField, StringField
from .base import BaseOrganisationDocument
from ..enums.api_status import APIStatus

class HealthCheckHistory(BaseOrganisationDocument):
    """HealthCheckHistory model for storing health check execution results.
    """
    config = ReferenceField('HealthCheckConfig')
    timestamp = DateTimeField(required=True)
    req_status = IntField(required=True)
    request = DictField()
    response = DictField()
    api_status = ListField(StringField(choices=[status.value for status in APIStatus]), required=True)
    api = ReferenceField('API', required=True)
    request_duration = IntField(required=True)
    #TODO: start/pause health check
    meta = {
        'collection': 'health_check_histories',
        'timeseries': {
            'timeField': 'timestamp',
            'metaField': 'config',
            'granularity': 'seconds'
        }
    }