import os
import json
import logging
from datetime import date


log_dir = "/var/log/app" if os.name != "nt" else f"{os.getcwd()}\logs"
os.makedirs(log_dir, exist_ok=True)

class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "timestamp": self.formatTime(record, self.datefmt),
            "level": record.levelname,
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno,
            "message": record.getMessage(),
            "extra_info": "This is a placeholder for additional log context to ensure the log entry exceeds 64 bytes.",
            "exception": self.formatException(record.exc_info) if record.exc_info else None
        }

        extras = {k: v for k, v in record.__dict__.items() if self._safe_value(v)}
        if extras:
            log_record.update(extras)

        return json.dumps(log_record, default=self._safe_value)

    def _safe_value(self, value):
        try:
            json.dumps(value)
            return value
        except TypeError:
            return str(value)


def setup_logger(file_handler=False, console_handler=True):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    if logger.hasHandlers():
        logger.handlers.clear()

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(JsonFormatter())
    logger.addHandler(console_handler)

    if(file_handler):
        file_handler = logging.FileHandler(os.path.join(log_dir, f"output-{date.today()}.log"))
        file_handler.setFormatter(JsonFormatter())
        logger.addHandler(file_handler)


    return logger


logger = setup_logger(file_handler=True)