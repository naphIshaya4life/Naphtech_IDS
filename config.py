"""
Configuration loader for Naphtech IDS
"""

import json
from pathlib import Path


CONFIG_PATH = Path("config/config.json")


def load_config():
    """
    Load configuration from config.json.

    Returns:
        dict: Configuration values.

    Raises:
        FileNotFoundError: If the config file is missing.
        ValueError: If the JSON is invalid.
    """

    try:
        with CONFIG_PATH.open("r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        raise FileNotFoundError(
            f"Configuration file not found: {CONFIG_PATH}"
        )

    except json.JSONDecodeError as error:
        raise ValueError(
            f"Invalid JSON in configuration file: {error}"
        )
