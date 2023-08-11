from datetime import datetime
import os
import logging
from typing import Literal
import traceback
from time import time
from typing import Any, Callable, Optional


class Log:
    log_folder = ""
    instance = None

    def __new__(cls, *args: Any, **kwargs: Any) -> "Log":
        if isinstance(cls.instance, Log):
            return cls.instance
        else:
            rv = super().__new__(cls)
            cls.instance = rv
            return rv

    def __init__(self) -> None:
        self.filename = f'{self.log_folder}{os.sep}log_file_{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}.log'
        logging.basicConfig(
            filename=self.filename,
            filemode="w",
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            level=logging.DEBUG,
        )

    def log(self, msg: str, level: Literal["info", "debug", "error"] = "info") -> None:
        if level == "info":
            logging.info(msg)
        elif level == "debug":
            logging.debug(msg)
        elif level == "error":
            logging.error(msg)


logger = Log()


def log_process_progress(process_name: Optional[str] = None) -> Callable[[Any], Any]:
    ow = process_name is None

    def log_decorator(func: Callable[[Any], Any]) -> Callable[[Any], Any]:
        if ow:
            process_name = func.__name__

        def wrapper(*args: Any, **kwargs: Any) -> Any:
            logger.log(f"Starting process: {process_name}.", "info")
            try:
                t = time()
                rv = func(*args, **kwargs)
                t = time() - t
            except Exception as e:
                arguments = "\n".join([str(a) for a in [*args, *kwargs.items()]])
                logger.log(f"Error occurred in: {process_name}", "error")
                logger.log(f"Arguments used:\n{arguments}", "error")
                logger.log(f"Traceback: {traceback.format_exc()}", "error")
                logger.log(f"Error code: {str(e)}", "error")
            else:
                logger.log(
                    f"Process finished: {process_name}, took {t} seconds.", "info"
                )
                return rv

        return wrapper

    return log_decorator
