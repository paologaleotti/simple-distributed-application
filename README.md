![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![RabbitMQ](https://img.shields.io/badge/Rabbitmq-FF6600?style=for-the-badge&logo=rabbitmq&logoColor=white) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

# simple-distributed-application

This repo contains an example of a simple but infinitely scalable web service using **Python** and **RabbitMQ**.

![schema](/docs/infra_schema.png)

## Features

- **Infinite scalabilty**: add as many workers as you want and RabbitMQ will spread all the messages across every deployed service
- **Docker/Kubernetes deployment**: each service can be containerized, distributed and deployed anywhere
- **Language independent**: RabbitMQ has client libraries for pretty much any language or framework
