"""Consumer module for code consumers use."""

import json

from kafka import KafkaConsumer


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
        print(f"Received message: {message.value}")
