from mongoengine import StringField, ReferenceField
from base import BaseOrganisationDocument

class Environment(BaseOrganisationDocument):
    """Environment model representing different deployment environments.
    """
    name = StringField()

    meta = {
        'indexes': [
            {'fields': ['name', 'organisation'], 'unique': True}
        ]
    }