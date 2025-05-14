from enum import Enum

class RequestBodyCheckOperator(Enum):
    """Enum for request body check operators"""
    eq = "eq"
    ne = "ne"
    gt = "gt"
    gte = "gte"
    lt = "lt"
    lte = "lte"
    contains = "contains"
    not_contains = "not_contains"