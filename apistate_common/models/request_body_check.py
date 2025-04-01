from mongoengine import StringField
from base import BaseEmbeddedDocument

class RequestBodyCheck(BaseEmbeddedDocument):
    """RequestBodyCheck model for configuring health check body validations.
    """
    key = StringField()
    value = StringField()