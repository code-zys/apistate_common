from mongoengine import connect
from apistate_common.models.user import User
from apistate_common.models.organisation import Organisation
from apistate_common.models.project import Project
from apistate_common.models.member import Member
from apistate_common.models.api import API
from apistate_common.models.connector import Connector
from apistate_common.models.connection import Connection
from apistate_common.models.endpoint import Endpoint
from apistate_common.models.environment import Environment
from apistate_common.models.health_config import HealthCheckConfig
from apistate_common.models.health_history import HealthCheckHistory
from apistate_common.models.request_body_check import RequestBodyCheck
from apistate_common.utils.db import DatabaseHandler

def test_imports():
    """Test importing and basic functionality of apistate_common models."""
    try:
        # Test model imports
        print("✓ Successfully imported models")
        
        # Test model class attributes
        assert hasattr(User, 'email'), "User model missing email field"
        assert hasattr(Organisation, 'name'), "Organisation model missing name field"
        assert hasattr(Project, 'name'), "Project model missing name field"
        assert hasattr(Member, 'user'), "Member model missing user field"
        assert hasattr(API, 'name'), "API model missing name field"
        assert hasattr(Connector, 'name'), "Connector model missing name field"
        assert hasattr(Connection, 'name'), "Connection model missing name field"
        assert hasattr(Endpoint, 'url'), "Endpoint model missing path field"
        assert hasattr(Environment, 'name'), "Environment model missing name field"
        assert hasattr(HealthCheckConfig, 'cron'), "HealthCheckConfig model missing name field"
        assert hasattr(HealthCheckHistory, 'api_status'), "HealthCheckHistory model missing status field"
        assert hasattr(RequestBodyCheck, 'key'), "RequestBodyCheck model missing body field"
        print("✓ Model attributes verified")
        
        print("All imports and basic model structure verified successfully!")
        return True
    except ImportError as e:
        print(f"Import Error: {str(e)}")
        return False
    except AssertionError as e:
        print(f"Model Structure Error: {str(e)}")
        return False
    except Exception as e:
        print(f"Unexpected Error: {str(e)}")
        return False

if __name__ == "__main__":
    test_imports()