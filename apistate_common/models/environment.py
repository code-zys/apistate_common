from mongoengine import StringField, ReferenceField
from .base import BaseOrganisationDocument

class Environment(BaseOrganisationDocument):
    """Environment model representing different deployment environments.
    """
    name = StringField()
    organisational_unit = ReferenceField('OrganisationalUnit', required=False)

    meta = {
        'indexes': [
            {'fields': ['name', 'organisation'], 'unique': True}
        ],
        'collection': 'environments',
    }