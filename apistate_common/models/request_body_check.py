from mongoengine import StringField
from .base import BaseEmbeddedDocument
from apistate_common.enums.request_body_check_operator import RequestBodyCheckOperator
class RequestBodyCheck(BaseEmbeddedDocument):
    """RequestBodyCheck model for configuring health check body validations.
    """
    path = StringField(required=True)
    value = StringField(required=True)
    operator = StringField(required=True, choices=[r.value for r in RequestBodyCheckOperator])