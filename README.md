# Microservice with Flask and Django REST framework

First aproach to python PRF/flask microservices restAPI
This repository contains two microservices implemented using Flask and Django REST framework that communicate with each other through a message queue.

## Description

The project consists of two microservices:

1. **Flask Microservice (main-backend)**:
    - Implemented in Flask to provide a web API.
    - Communicates with a MySQL database.
    - Publishes and consumes messages on a message queue (RabbitMQ) to synchronize data with the Django microservice.

2. **Django REST Microservice (main-api)**:
    - Implemented in Django REST framework to provide a RESTful API.
    - Consumes messages from the message queue to keep its data updated.

## Environment Setup and Usage

### Environment Setup

- Ensure you have Docker and Docker Compose installed on your system.
- Clone this repository to your local machine.

### Starting the Application

1. Navigate to the project's root directory and run the following command to build and start the Docker containers:

    ```bash
    docker-compose up --build
    ```

2. The microservices will run and be available at the following URLs:

   - Flask Microservice: `http://localhost:8001`
   - Django REST Microservice: `http://localhost:8000`

### Usage

- You can use a tool like [Postman](https://www.postman.com/) to make requests to the APIs provided by both microservices.

### Additional Notes

- Make sure to properly configure the environment files (`.env`) with the necessary credentials for the database and message queue.

## Contribution

If you want to contribute to the development of this project, follow these steps:

1. Fork the repository.
2. Create a branch for your changes: `git checkout -b feature/feature-name`.
3. Make your modifications and document changes if necessary.
4. Commit your changes: `git commit -m 'Add new feature'`.
5. Push your changes to your GitHub repository: `git push origin feature/feature-name`.
6. Open a pull request in this repository.

## License

This project is distributed under the [MIT License](LICENSE).

