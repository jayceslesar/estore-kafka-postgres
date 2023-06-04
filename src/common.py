"""Common utilities needed across the codebase."""

import socket
import time


def _wait_for_service(host: str, port: int, interval: int = 5) -> None:
    """Poll the kafka service.

    Args:
        host: kafka host
        port: kafka port
        interval: check interval. Defaults to 5.
    """
    print("Waiting for Kafka to start...")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        try:
            result = sock.connect_ex((host, port))
            if result == 0:
                print(f"Kafka service is up!")
                return
            else:
                print(f"Kafka service is not up yet, sleeping for {interval} seconds...")
                time.sleep(interval)
        except socket.error as e:
            time.sleep(interval)
    sock.close()
