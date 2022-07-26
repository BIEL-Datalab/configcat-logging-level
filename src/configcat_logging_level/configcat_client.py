from unittest.mock import create_autospec

from configcatclient import ConfigCatClient, create_client_with_auto_poll
from configcat_logging_level.settings import settings
from configcat_logging_level.logging_level import logging, default_logging_level_map


def configuration_changed_callback():
    LOGGER_LEVEL = settings.FEATURE_FLAG_NAME
    level = configcat_client.get_value(LOGGER_LEVEL, "Default")
    level = level.upper()
    print(f"Logger level changed to {level}")

    if level not in ["DEBUG", "INFO", "WARNING", "ERROR", "WARN"]:
        level = "DEFAULT"

    loggers = ["root", *logging.root.manager.loggerDict]
    if level == "DEFAULT":
        if default_logging_level_map:
            for name in loggers:
                logger = logging.getLogger(name)
                logger_level_map = default_logging_level_map.get(name, {})
                for handler in logger.handlers:
                    handler_key = hash(handler)
                    handler_level = logger_level_map.get(handler_key, "INFO")
                    handler.setLevel(handler_level)
                logger.setLevel(logger_level_map.get("default_level", "INFO"))
            print("Logger level set to DEFAULT successfully")
        else:
            print("Failed to get default_logging_level_map")
    else:
        for name in loggers:
            logger = logging.getLogger(name)
            logger.setLevel(level)

            handlers = logger.handlers
            for handler in handlers:
                handler_level = handler.level
                handler.setLevel(level)
        print(f"Logger level set to {level} successfully")


def get_configcat_client():
    mock = create_autospec(ConfigCatClient)
    mock.get_value.return_value = settings.MOCK_LOGGING_LEVEL

    if settings.CONFIGCAT_SDK is None:
        print("CONFIGCAT_SDK is not set")
        return mock

    elif settings.EXECUTION_ENV in ("k8s", "bastion", "test", "default"):
        configcat_client = create_client_with_auto_poll(
            settings.CONFIGCAT_SDK,
            on_configuration_changed_callback=configuration_changed_callback,
            poll_interval_seconds=settings.CANFIGCAT_POLL_INTERVAL_SECONDS,
        )
        return configcat_client
    else:
        print(
            f"ConfigCatClient is mocked, mock.get_value.return_value is {settings.MOCK_LOGGING_LEVEL}"
        )
        return mock


configcat_client = get_configcat_client()
