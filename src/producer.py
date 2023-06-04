"""Producer module for code producers use."""

import json
import time
from concurrent.futures import ThreadPoolExecutor, wait

from kafka import KafkaProducer

from src.generate_data import make_fake_estore_data


def send_purchases_to_kafka(producer: KafkaProducer) -> None:
    """Worker function to push data to kafka.

        Args:
            producer: producer instance
    """
    try:
        purchase_data = make_fake_estore_data()
        for purchase in purchase_data:
            producer.send("purchases", purchase)
            producer.flush()
    except Exception as e:
        print(f"An error occurred: {e}")


def produce(host: str, port: int, max_workers: int = 5, timeout: float = 10.0) -> None:
    """Main function to take advantage of threads and worker function to push data to kafka.

    Args:
        host: ip/name of kafka instance
        port: port of kafka instance
        max_workers: number of threads. Defaults to 5.
        timeout: timeout to run. Defaults to 10.0.
    """
    producer = KafkaProducer(
        bootstrap_servers=f"{host}:{port}", value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )
    print(f"Running {max_workers} for {timeout} seconds...")
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        while True:
            if time.time() - start_time >= timeout:
                break
            futures = {executor.submit(send_purchases_to_kafka, (producer)) for _ in range(max_workers)}
            wait(futures)

    print("Complete!")
    producer.close()
