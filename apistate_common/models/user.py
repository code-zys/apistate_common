from datetime import datetime
from mongoengine import StringField, EmailField, BooleanField, ReferenceField, EnumField
from .base import BaseDocument, BaseOrganisationDocument

class User(BaseDocument):
    """User model representing a user in the system.
    
    This model stores user information and authentication details.
    """
    email = EmailField(required=True, unique=True)
    hashed_password = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    is_active = BooleanField(default=True)
    is_superuser = BooleanField(default=False)
    change_password_on_first_connection = BooleanField(default=True)

    meta = {
        'collection': 'users',
        'indexes': [
            'email',
            'created_at'
        ]
    }

    def __str__(self):
        return f"User(email={self.email})"