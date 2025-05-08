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
            "created_at": endpoint.created_at.isoformat() if endpoint.created_at else None,
            "updated_at": endpoint.updated_at.isoformat() if endpoint.updated_at else None,
            "deleted": endpoint.deleted
        }

    @staticmethod
    def to_model(data: dict) -> Endpoint:
        """Convert a dictionary to an Endpoint model."""
        return Endpoint(
            path=data.get("path"),
            method=data.get("method"),
            api_id=data.get("api_id"),
            resource_id=data.get("resource_id")
        )