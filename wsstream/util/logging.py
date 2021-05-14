import logging


def set_log_level(args: dict, logger: logging.Logger) -> None:
    if args["--verbose"]:
        logger.setLevel(level=logging.DEBUG)
    elif args["--silent"]:
        logger.setLevel(level=logging.ERROR)
    else:
        logger.setLevel(level=logging.INFO)
