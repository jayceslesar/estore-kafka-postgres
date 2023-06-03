# Kafka Playground
simulates sending e-store purchase data generated using [Faker](https://faker.readthedocs.io/en/master/) and a [Simon model](https://en.wikipedia.org/wiki/Simon_model)


## Pipeline
1. Data is generated using the `produce` entrypoint which sends data to Kafka
2. A consumer picks that data up from the `purchases` topic in Kafka (in progress)
3. The consumer ensures the data is in a clean format and pushes to postgres (in progress)
4. Stats are exposed on the data via the [ibis-framework](https://ibis-project.org/) library in a dashboard in Dash (in progress)

## Goals
1. Practice tools I am not as proficient as I would like to be such as setting up databases/containers/apps
2. Show off