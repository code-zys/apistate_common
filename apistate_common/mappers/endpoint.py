from apistate_common.models.endpoint import Endpoint

class EndpointMapper:
    @staticmethod
    def to_dict(endpoint: Endpoint) -> dict:
        """Convert an Endpoint model to a dictionary representation."""
        return {
            "id": str(endpoint.id),
            "path": endpoint.path,
            "method": endpoint.method,
            "api_id": str(endpoint.api.id) if endpoint.api else None,
            "resource_id": endpoint.resource_id,
            "query_params": endpoint.query_params,
            "path_params": endpoint.path_params,
            "body_type": endpoint.body_type,
            "metadata": endpoint.metadata,
            "description": endpoint.description,
            "environment_id": str(endpoint.environment.id) if endpoint.environment else None,
            "created_at": endpoint.created_at if endpoint.created_at else None,
            "updated_at": endpoint.updated_at if endpoint.updated_at else None,
        }

    @staticmethod
    def to_model(data: dict) -> Endpoint:
        """Convert a dictionary to an Endpoint model."""
        return Endpoint(
            path=data.get("path"),
            method=data.get("method"),
            resource_id=data.get("resource_id"),
            query_params=data.get("query_params", []),
            path_params=data.get("path_params", []),
            body_type=data.get("body_type", {}),
            metadata=data.get("metadata", {}),
            description=data.get("description")
        )