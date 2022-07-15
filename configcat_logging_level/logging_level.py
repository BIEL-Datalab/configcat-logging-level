import logging

default_logging_level_map = {}
default_logging_level_map_has_been_set = False


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

    global default_logging_level_map_has_been_set
    default_logging_level_map_has_been_set = True
    print("Default logging level map has been set")
