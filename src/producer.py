import concurrent.futures
import json
import socket
import time

from kafka import KafkaProducer

from src.generate_data import make_fake_estore_data


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


def send_purchases_to_kafka() -> None:
    """Worker function to push data to kafka."""
    purchases = make_fake_estore_data()

    for purchase in purchases:
        producer.send("purchases", purchase)

    producer.flush()


def produce(max_workers: int = 5, timeout: float = 10.0) -> None:
    """Main function to take advantage of threads and worker function to push data to kafka.

    Args:
        max_workers: number of threads. Defaults to 5.
        timeout: timeout to run. Defaults to 10.0.
    """
    producer = KafkaProducer(bootstrap_servers="kafka:9092", value_serializer=lambda v: json.dumps(v).encode("utf-8"))
    print(f"Running {max_workers} for {timeout} seconds...")
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        while True:
            if time.time() - start_time >= timeout:
                break
            futures = {executor.submit(send_purchases_to_kafka) for _ in range(max_workers)}

            concurrent.futures.wait(futures)
    print("Complete!")
    producer.close()
