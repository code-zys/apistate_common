# API State Common Package

This package contains common utilities, models, and DTOs shared across the API State microservices architecture.

## Overview

The apistate_common package provides a set of reusable components that ensure consistency and reduce code duplication across different microservices. It includes:

- Authentication utilities
- Database handling
- JWT management
- Password hashing and verification
- Base repository patterns
- Data validation utilities
- Common DTOs and models

## Installation

Add the following to your `requirements.txt`:

```
apistate_common
```

## Package Structure

### Utils

- `auth.py`: User authentication and authorization utilities
- `password.py`: Password hashing and verification
- `jwt.py`: JWT token handling
- `db.py`: Database connection and operations
- `repository.py`: Base repository pattern implementation
- `validation.py`: Data validation utilities

### Models

Shared database models including:

- User
- Organization
- Project
- API
- Endpoint
- Environment
- Health configurations
- Connections

### DTOs

Data Transfer Objects for:

- User operations
- Organization management
- Pagination

## Usage Examples

### Authentication

```python
from apistate_common.utils import get_current_user, get_current_active_user

# Use in FastAPI endpoints
@app.get("/users/me")
async def get_me(current_user = Depends(get_current_user)):
    return current_user
```

### Password Management

```python
from apistate_common.utils import get_password_hash, verify_password

# Hash a password
hashed = get_password_hash("mypassword")

# Verify a password
is_valid = verify_password("mypassword", hashed)
```

### Database Operations

```python
from apistate_common.utils import DatabaseHandler

# Initialize database connection
db = DatabaseHandler(connection_string)

# Use in repositories
class UserRepository(BaseRepository):
    def __init__(self, db_handler: DatabaseHandler):
        super().__init__(db_handler)
```

## Contributing

When adding new functionality to this package:

1. Ensure the new code is properly documented
2. Add appropriate tests
3. Update this README if necessary
4. Follow the existing code style and patterns

## License

Proprietary - All rights reserved