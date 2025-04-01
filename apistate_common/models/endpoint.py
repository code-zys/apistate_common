from base import BaseOrganisationDocument
from mongoengine import StringField, ReferenceField

class Endpoint(BaseOrganisationDocument):
    """Endpoint model representing an API endpoint.
    """
    url = StringField()
    method = StringField()
    environment = ReferenceField('Environment')
    api = ReferenceField('API')

    meta = {
        'indexes': [
            {'fields': ['url', 'method', 'environment'], 'unique': True}
        ]
    }