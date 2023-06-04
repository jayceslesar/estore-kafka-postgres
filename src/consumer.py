"""Consumer module for code consumers use."""

import json

from kafka import KafkaConsumer

from src.transform_and_load import _reformat_message, _write_message


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
