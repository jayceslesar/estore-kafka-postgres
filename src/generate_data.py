"""utilities for generating data to push to kafka."""

from datetime import datetime, timezone
from typing import Any

import numpy as np
from faker import Faker

np.random.seed(42)


def simons_model(steps: int, rho: float) -> list[int]:
    """Simple simons model to generate rich get richer data.

    Args:
        steps: number of steps
        rho: probability of new number

    Returns:
        list of numbers generated in order
    """
    population = np.zeros(steps)
    num_groups = 1
    population[0] = 1

    for i in range(steps - 1):
        if np.random.uniform(0, 1) <= rho:
            num_groups += 1
            population[i + 1] = num_groups
        else:
            population[i + 1] = np.random.choice(population[0 : i + 1])

    return list(population.astype(int))


def make_fake_estore_data() -> list[dict[str, Any]]:
    """Generate fake data to be consumed downstream.

    Returns:
        list of purchases at the fake estore
    """
    population = simons_model(1000, 0.1)
    unique, counts = np.unique(population, return_counts=True)
    faker = Faker()
    companies = {company: faker.company() for company in unique}
    purchases_at_company = dict(zip(unique, counts))
    purchases_data = []
    for company_id, num_purchases in purchases_at_company.items():
        purchases_data += [
            {
                "company": companies[company_id],
                "first_name": faker.first_name(),
                "last_name": faker.last_name(),
                "phone_number": faker.phone_number(),
                "address": faker.address(),
                "credit_card": faker.credit_card_full(),
                "date": faker.date_time_between(start_date=datetime(2023, 6, 1), tzinfo=timezone.utc).isoformat(),
                "amount": np.random.uniform(1, 5_000),
            }
            for i in range(num_purchases)
        ]

    return purchases_data
