from ..models.health_history import HealthCheckHistory
from typing import Dict, Any

class HealthCheckHistoryMapper:
    @staticmethod
    def to_dict(history: HealthCheckHistory) -> Dict[str, Any]:
        """Convert a HealthCheckHistory model to a dictionary."""
        return {
            "id": str(history.id),
            "config_id": str(history.config.id) if history.config else None,
            "timestamp": history.timestamp,
            "req_status": history.req_status,
            "request": history.request,
            "response": history.response,
            "api_status": history.api_status.value if history.api_status else None,
            "api_id": str(history.api.id) if history.api else None,
            "request_duration": history.request_duration,
            "organisation_id": str(history.organisation.id) if history.organisation else None,
            "created_at": history.created_at
        }

    @staticmethod
    def to_model(data: Dict[str, Any]) -> HealthCheckHistory:
        """Convert a dictionary to a HealthCheckHistory model."""
        return HealthCheckHistory(
            config=data.get("config_id"),
            timestamp=data.get("timestamp"),
            req_status=data.get("req_status"),
            request=data.get("request", {}),
            response=data.get("response", {}),
            api_status=data.get("api_status"),
            api=data.get("api_id"),
            request_duration=data.get("request_duration"),
            organisation=data.get("organisation_id")
        )