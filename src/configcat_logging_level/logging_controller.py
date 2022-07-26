from src.configcat_logging_level.configcat_client import configcat_client
from src.configcat_logging_level.logging_level import (
    init_default_logging_level_map,
    default_logging_level_map,
)
from src.configcat_logging_level.settings import settings


def create():
    init_default_logging_level_map()


def get_value(
    key: str = settings.FEATURE_FLAG_NAME,
    default_value: str = settings.MOCK_LOGGING_LEVEL,
):
    return configcat_client.get_value(key, default_value)


def get_default_logging_level():
    return {"default_logging_level_map": default_logging_level_map}
