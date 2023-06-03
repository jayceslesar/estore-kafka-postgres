"""CLI for running various tasks."""

import click

from src.producer import _wait_for_service
from src.producer import produce as _produce


@click.command()
@click.option("-m", "--max-workers", type=int, default=5)
@click.option("-t", "--timeout", type=float, default=10.0)
def produce(max_workers: int, timeout: float) -> None:
    """CLI for generating and pushing data to kafka.

    Args:
        max_workers: number of threads
        timeout: timeout for each worker thread
    """
    _wait_for_service("kafka", 9092)
    _produce(max_workers, timeout)


@click.command()
def consume() -> None:
    """CLI for consuming data from kafka."""
    pass
