"""CLI for running various tasks."""

import click

from src.common import _wait_for_service
from src.consumer import consume as _consume
from src.producer import produce as _produce

HOST = "kafka"
PORT = 9092


@click.group()
def workers():
    pass


@workers.command()
@click.option("-m", "--max-workers", type=int, default=5)
@click.option("-t", "--timeout", type=float, default=10.0)
def produce(max_workers: int, timeout: float) -> None:
    """CLI for generating and pushing data to kafka.

    Args:
        max_workers: number of threads
        timeout: timeout for each worker thread
    """
    _wait_for_service(HOST, PORT)
    _produce(HOST, PORT, max_workers, timeout)


@workers.command()
def consume() -> None:
    """CLI for consuming data from kafka."""
    _wait_for_service(HOST, PORT)
    _consume(HOST, PORT, "transformed")
