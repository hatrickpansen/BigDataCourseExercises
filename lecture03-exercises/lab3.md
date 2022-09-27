# Exercise 1 - Composing a Kafka cluster

## How is the environment variable `ZOOKEEPER_CLIENT_PORT` related to the advertised docker ports?

Kafka can connect to this by specifying host and port in its `KAFKA_ZOOKEEPER_CONNECT` environment variable.

## What purpose does `KAFKA_ADVERTISED_LISTENERS` have?

Defines the addresses that Kafka listens to, and that potential clients can connect to.

## How can you connect to Kowl in the browser?

lol. `localhost:8080`

# Exercise 2 - Interacting with Kafka using Kowl

## What does the Broker view show you?

Active clients that are connected to kowl

1. What is the default value for `log.retention.hours`?
   1. 7 days
2. What is the default value for `offsets.topic.replication.factor`?
   1. Default is 3. Current is 1.

## What does the Topics view show you?

The name, amount of partitions, replicas, cleanup policy and size of topics.
