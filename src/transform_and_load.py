"""Utilities fo transforming and loading into database."""

import json
import os
import uuid


def _reformat_message(message: dict[str, str]) -> dict[str, str]:
    """Reformat a message consumed from kafka by coercing strings + floats into common format.

    Args:
        message: message that was consumed

    Returns:
        reformatted dict of same data but cleaner
    """
    reformatted = {}
    for key, value in message.items():
        if isinstance(value, float):
            value = round(value, 2)
        else:
            value = value.replace("\n", " ")
        reformatted[key] = value

    return reformatted


def _write_message(message: dict[str, str], write_to: str) -> None:
    """Write a reformatted message to disk to be loaded into postgres.

    Args:
        message: reformatted message that was consumed from the topic
        write_to: where to write
    """
    name = uuid.uuid4().hex
    path = os.path.join(write_to, name)
    with open(f"{path}.json", "w") as f:
        json.dumps(message, f)


def _stage(read_path: str, staging_path: str) -> str:
    """Read all the data we can from `read_path`, combine and stage in `staging_path`.

    Args:
        read_path: where to read data from
        staging_path: path to stage to

    Returns:
        path of the staged data
    """
    pass


def _load(staged_data_path: str, host: str, port: int) -> None:
    """Load staged data into the DB

    Args:
        staged_data_path: where the staged data is
        host: host of the DB
        port: port of the DB
    """
    pass


def stage_and_load(read_path: str, staging_path: str, host: str, port: int) -> None:
    """Read batch data from where _write_messages writes to and load into Postgres to reduce strain on the DB.

        Goal is to stage data on some schedule and batch load as well as cleanup.

    Args:
        read_path: data that needs to be staged
        staging_path: the staged data
        host: host of the DB
        port: port of the DB
    """
    staged_data_path = _stage(read_path, staging_path)
    _load(staged_data_path, host, port)
    os.remove(staged_data_path)
