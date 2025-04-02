from datetime import datetime
from mongoengine import StringField
from .base import BaseDocument

class Organisation(BaseDocument):
    """Organisation model representing a company or entity in the system.
    
    This model stores basic organization information and serves as a parent
    for organization-specific models.
    """
    name = StringField(unique=True)
    code = StringField(unique=True)
    domain = StringField(unique=True)

    meta = {
        'collection': 'organisations',
    }