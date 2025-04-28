from mongoengine import StringField, ReferenceField, DictField
from .base import BaseOrganisationDocument

class Project(BaseOrganisationDocument):
    """Project model representing a project within an organisation.
    """
    name = StringField()
    description = StringField()
    environment = ReferenceField('Environment', required=True)
    config_file_url = StringField()
    config_file = DictField()  # Stores the API configuration as a dictionary
    organisational_unit = ReferenceField('OrganisationalUnit', required=False)

    meta = {
        'indexes': [
            {'fields': ['name', 'organisation'], 'unique': True}
        ],
        'collection': 'projects',
    }