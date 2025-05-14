from mongoengine import StringField, ReferenceField
from .base import BaseOrganisationDocument
from ..enums.api_status import APIStatus
class API(BaseOrganisationDocument):
    """API model representing an API within a project.
    """
    name = StringField()
    url = StringField()
    description = StringField()
    version = StringField() #TODO: take version into account when retrieving the API
    project = ReferenceField('Project')
    connection = ReferenceField('Connection', required=True)
    connector = ReferenceField('Connector', required=True)
    external_id = StringField()
    region = StringField
    status = StringField(required=True, choices=[api_status.value for api_status in APIStatus], default=APIStatus.NOT_SYNCHRONIZED.value)
    error_message = StringField()
    
    meta = {
        'indexes': [
            {'fields': ['name', 'organisation'], 'unique': True}
        ],
        'collection': 'apis'
    }