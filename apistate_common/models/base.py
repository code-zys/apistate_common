from datetime import datetime
from mongoengine import (
    Document, EmbeddedDocument, StringField, ObjectIdField, IntField,
    ReferenceField, BooleanField, EmailField
)

class BaseDocument(Document):
    """Base document class for all models.
    
    Provides common fields and functionality for tracking creation and updates.
    """
    created_at = IntField(default=lambda: int(datetime.utcnow().timestamp()))
    updated_at = IntField(default=lambda: int(datetime.utcnow().timestamp()))
    created_by = ReferenceField('User', required=True)
    updated_by = ReferenceField('User', null=True)

    meta = {
        'abstract': True
    }

    def save(self, *args, **kwargs):
        self.updated_at = int(datetime.utcnow().timestamp())
        return super().save(*args, **kwargs)

class BaseEmbeddedDocument(EmbeddedDocument):
    """Base embedded document class.
    
    Provides common fields for embedded documents that need tracking.
    """
    created_at = IntField(default=lambda: int(datetime.utcnow().timestamp()))
    updated_at = IntField(default=lambda: int(datetime.utcnow().timestamp()))
    created_by = ReferenceField('User', required=False)
    updated_by = ReferenceField('User', null=True)

    meta = {
        'allow_inheritance': True
    }

class BaseOrganisationDocument(BaseDocument):
    """Base document class for organization-specific models.
    
    Extends BaseDocument to include organization reference.
    """
    organisation = ReferenceField('Organisation', required=True)

    meta = {
        'abstract': True
    }