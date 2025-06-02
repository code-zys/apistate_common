from apistate_common.models.health_config import HealthCheckConfig
from apistate_common.dtos.health_config import HealthCheckConfigResponseDto, RequestBodyCheckDto
from bson import ObjectId

class HealthCheckConfigMapper:
    @staticmethod
    def to_dto(config: HealthCheckConfig) -> HealthCheckConfigResponseDto:
        endpoint = None
        if config.endpoint:
            if isinstance(config.endpoint, ObjectId):
                endpoint = str(config.endpoint)
            else:
                endpoint = str(config.endpoint.id)
        return HealthCheckConfigResponseDto(
            id=str(config.id),
            endpoint_id=endpoint,
            cron=config.cron,
            api_id=str(config.api.id),
            created_at=config.created_at,
            path_params_data=config.path_params_data,
            query_params_data=config.query_params_data
        )