from apistate_common.models.health_config import HealthCheckConfig
from apistate_common.dtos.health_config import HealthCheckConfigResponseDto, RequestBodyCheckDto
from bson import ObjectId

class HealthCheckConfigMapper:
    @staticmethod
    def to_dto(config: HealthCheckConfig) -> HealthCheckConfigResponseDto:
        """Convert a HealthCheckConfig model to a DTO.
        
        Args:
            config: The HealthCheckConfig model to convert
            
        Returns:
            HealthCheckConfigResponseDto: The converted DTO
        """
        return HealthCheckConfigResponseDto(
            id=str(config.id),
            endpoint_id=str(config.endpoint.id) if config.endpoint else None,
            cron=config.cron,
            status_code=config.status_code,
            body_checks=[
                RequestBodyCheckDto(
                    path=check.path,
                    value=check.value,
                    operator=check.operator
                ) for check in config.body_checks
            ] if config.body_checks else [],
            api_id=str(config.api.id)
        )