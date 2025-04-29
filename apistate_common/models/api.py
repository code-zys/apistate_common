from mongoengine import StringField, ReferenceField
from .base import BaseOrganisationDocument
class API(BaseOrganisationDocument):
    """API model representing an API within a project.
    """
    name = StringField()
    version = StringField()
    project = ReferenceField('Project')

    meta = {
        'indexes': [
            {'fields': ['name', 'organisation'], 'unique': True}
        ],
        'collection': 'apis'
    }