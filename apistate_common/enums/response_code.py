from enum import Enum

class ResponseCode(Enum):
    # General
    UNKNOWN = "UNKNOWN"
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"
    NOT_FOUND = "NOT_FOUND"
    # Authentication
    LOGIN_SUCCESS = "LOGIN_SUCCESS"
    LOGIN_FAILED = "LOGIN_FAILED"
    PASSWORD_CHANGE_SUCCESS = "PASSWORD_CHANGE_SUCCESS"
    PASSWORD_CHANGE_FAILED = "PASSWORD_CHANGE_FAILED"
    INVALID_CREDENTIALS = "INVALID_CREDENTIALS"

    # User Management
    USER_CREATED = "USER_CREATED"
    USER_UPDATED = "USER_UPDATED"
    USER_DELETED = "USER_DELETED"
    USER_NOT_FOUND = "USER_NOT_FOUND"
    USER_ALREADY_EXISTS = "USER_ALREADY_EXISTS"

    # Organization Management
    ORGANIZATION_CREATED = "ORGANIZATION_CREATED"
    ORGANIZATION_UPDATED = "ORGANIZATION_UPDATED"
    ORGANIZATION_NOT_FOUND = "ORGANIZATION_NOT_FOUND"
    ORGANIZATION_ALREADY_EXISTS = "ORGANIZATION_ALREADY_EXISTS"

    # Member Management
    MEMBER_CREATED = "MEMBER_CREATED"
    MEMBER_UPDATED = "MEMBER_UPDATED"
    MEMBER_DELETED = "MEMBER_DELETED"
    MEMBER_NOT_FOUND = "MEMBER_NOT_FOUND"
    MEMBER_ALREADY_EXISTS = "MEMBER_ALREADY_EXISTS"

    # Organizational Unit
    ORGANISATIONAL_UNIT_CREATED = "ORGANISATIONAL_UNIT_CREATED"
    ORGANISATIONAL_UNIT_UPDATED = "ORGANISATIONAL_UNIT_UPDATED"
    ORGANISATIONAL_UNIT_DELETED = "ORGANISATIONAL_UNIT_DELETED"
    ORGANISATIONAL_UNIT_NOT_FOUND = "ORGANISATIONAL_UNIT_NOT_FOUND"

    # Project Management
    PROJECT_CREATED = "PROJECT_CREATED"
    PROJECT_UPDATED = "PROJECT_UPDATED"
    PROJECT_DELETED = "PROJECT_DELETED"
    PROJECT_NOT_FOUND = "PROJECT_NOT_FOUND"

    # Environment Management
    ENVIRONMENT_CREATED = "ENVIRONMENT_CREATED"
    ENVIRONMENT_UPDATED = "ENVIRONMENT_UPDATED"
    ENVIRONMENT_DELETED = "ENVIRONMENT_DELETED"
    ENVIRONMENT_NOT_FOUND = "ENVIRONMENT_NOT_FOUND"

    # Connection Management
    CONNECTION_CREATED = "CONNECTION_CREATED"
    CONNECTION_UPDATED = "CONNECTION_UPDATED"
    CONNECTION_DELETED = "CONNECTION_DELETED"
    CONNECTION_NOT_FOUND = "CONNECTION_NOT_FOUND"

    UNAUTHORIZED = "UNAUTHORIZED"