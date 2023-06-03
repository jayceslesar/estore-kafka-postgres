# Kafka Playground
simulates sending e-store purchase data generated using [Faker](https://faker.readthedocs.io/en/master/) and a [Simon model](https://en.wikipedia.org/wiki/Simon_model)


## Pipeline
1. Data is generated using the `produce` entrypoint which sends data to Kafka
2. A consumer picks that data up from the `purchases` topic in Kafka
3. The consumer ensures the data is in a clean format and pushes to postgres
4. Stats are exposed on the data via the [ibis-framework](https://ibis-project.org/) library in a dashboard in Dash (in progress)

## Goals
1. Practice tools I am not as proficient as I would like to be such as setting up databases/containers/apps
2. Show off


## TODO
- [] Add consumer
- [] Functionality for consumer of cleaning data and pushing to postgres
- [] Retention policies to Kafka as to not store data forever
- [] Expose ibis and a simple Dash app against the postgres database
- [] Make the producer more continuous with a cron
