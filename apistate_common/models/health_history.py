from mongoengine import IntField, DictField, ReferenceField, EnumField
from .base import BaseOrganisationDocument
from ..enums.api_status import APIStatus

class HealthCheckHistory(BaseOrganisationDocument):
    """HealthCheckHistory model for storing health check execution results.
    """
    config = ReferenceField('HealthCheckConfig')
    timestamp = IntField(required=True)
    req_status = IntField(required=True)
    request = DictField()
    response = DictField()
    api_status = EnumField(APIStatus)
    api = ReferenceField('API', required=True)
    request_duration = IntField(required=True)
    #TODO: start/pause health check
    meta = {
        'collection': 'health_check_history',
        'indexes': [
            {'fields': ['config', 'timestamp'], 'unique': True}
        ],
        'timeseries': {
            'timeField': 'timestamp',
            'metaField': 'config', #TODO: check if this is correct
            'granularity': 'seconds'
        }
    }