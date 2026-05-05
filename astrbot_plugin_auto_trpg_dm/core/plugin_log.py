from __future__ import annotations

from typing import Any

from astrbot.api import logger


def configure_plugin_logging(*_args: Any, **_kwargs: Any) -> Any:
    logger.info("auto_trpg_dm logger uses AstrBot logger")
    return logger


def get_plugin_logger() -> Any:
    return logger
