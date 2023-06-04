"""Consumer module for code consumers use."""

import json
import uuid

from kafka import KafkaConsumer


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
    pass


def consume(host: str, port: int, write_to: str) -> None:
    """Consumes messages, reformats and writes reformatted to write_to

    Args:
        host: ip/name of kafka instance
        port: port of kafka instance
        write_to: where to write reformatted messages
    """
    consumer = KafkaConsumer(
        "purchases",
        bootstrap_servers=f"{host}:{port}",
        auto_offset_reset="earliest",
        value_deserializer=lambda v: json.loads(v.decode("utf-8")),
    )

    for message in consumer:
        reformatted_message = _reformat_message(message.value)
        _write_message(reformatted_message, write_to)
