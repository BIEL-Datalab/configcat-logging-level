import logging
from configcat_logging_level import default_logging_level_map


def init_default_logging_level_map():
    loggers = ["root", *logging.root.manager.loggerDict]
    for name in loggers:
        logger = logging.getLogger(name)
        effective_level = logger.getEffectiveLevel()
        default_logging_level_map[name] = {
            **default_logging_level_map.get(name, {}),
            "default_level": effective_level,
        }

        handlers = logger.handlers
        for handler in handlers:
            handler_level = handler.level
            default_logging_level_map[name] = {
                **default_logging_level_map.get(name, {}),
                hash(handler): handler_level,
            }

    print("Default logging level map has been set")


def init():
    init_default_logging_level_map()
    from configcat_logging_level.configcat_client import configcat_client
