from mongoengine import StringField, ReferenceField
from .base import BaseOrganisationDocument

class Project(BaseOrganisationDocument):
    """Project model representing a project within an organisation.
    """
    name = StringField()
    environment = ReferenceField('Environment')
    config_file_url = StringField()
    organisational_unit = ReferenceField('OrganisationalUnit', required=False)

    meta = {
        'indexes': [
            {'fields': ['name', 'organisation'], 'unique': True}
        ]
    }