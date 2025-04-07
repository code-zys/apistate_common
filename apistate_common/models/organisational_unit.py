from .base import BaseOrganisationDocument
from mongoengine import StringField
from .organisation import Organisation

class OrganisationalUnit(BaseOrganisationDocument):
    """OrganisationUnit model representing a unit/department within an organisation.
    """
    name = StringField(required=True)
    description = StringField()
    organisation = ReferenceField(Organisation, required=True)

    meta = {
        'indexes': [
            {'fields': ['name', 'organisation'], 'unique': True}
        ]
    }