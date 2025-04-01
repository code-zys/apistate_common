from base import BaseOrganisationDocument
from mongoengine import ReferenceField, EnumField
from ..enums.member_type import MemberType

class Member(BaseOrganisationDocument):
    """Member model representing a user's membership in an organisation.
    """
    user = ReferenceField('User', unique=True)
    type = EnumField(MemberType)

    meta = {
        'indexes': [
            {'fields': ['user', 'organisation'], 'unique': True}
        ]
    }