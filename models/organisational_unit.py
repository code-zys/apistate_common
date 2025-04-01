from base import BaseDocument
from mongoengine import StringField
from organization import Organisation

class OrganisationUnit(BaseDocument):
    """OrganisationUnit model representing a unit/department within an organisation.
    """
    name = StringField()
    organisation = ReferenceField(Organisation, required=True)

    meta = {
        'indexes': [
            {'fields': ['name', 'organisation'], 'unique': True}
        ]
    }