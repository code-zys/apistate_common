from mongoengine import StringField, ReferenceField
from base import BaseOrganisationDocument

class Connection(BaseOrganisationDocument):
    """Connection model representing an active connection instance.
    """
    connector = ReferenceField('Connector')
    name = StringField()
    organisation_unit = ReferenceField('OrganisationUnit')

    meta = {
        'indexes': [
            {'fields': ['name', 'organisation'], 'unique': True}
        ]
    }