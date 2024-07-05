# Flask & Redis Dockerized TDM (Test Data Manager) Application

Welcome to the Flask & Redis application! This project demonstrates how to build a simple Flask application that interacts with Redis to manage test data, all managed and run within Docker containers. The project also includes a GitHub Actions workflow for automated testing.

## Table of Contents

- [Getting Started](#getting-started)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Testing](#testing)
- [GitHub Actions](#github-actions)
- [Contributing](#contributing)


## Getting Started

These instructions will help you set up and run the project on your local machine for development and testing purposes.

### Prerequisites

Make sure you have the following installed on your local development machine:

- Docker
- Docker Compose
- Git

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/berkaykirmizioglu/redis-tdm.git
    cd redis-tdm
    ```

2. Build and start the Docker containers:

    ```bash
    docker-compose up --build
    ```

3. The Flask application should now be running at `http://localhost:5000`.

## Configuration

The application configuration is managed via a `config.yaml` file. This file contains settings for connecting to Redis and for configuring the Flask application.

Here is a sample `config.yaml`:

```yaml
redis:
  host: redis
  port: 6379
  db: 0

flask:
  host: 0.0.0.0
  port: 5000
```

## Running The Application
To start the application, simply use Docker Compose:
```bash
docker-compose up --build
```
This will start both the Flask application and the Redis server.

## Testing
A script named test.sh is provided to test the application endpoints. This script uses curl commands to interact with the Flask API.

Here’s how to run the test script:
```bash
chmod +x test.sh
./test.sh
```

The script performs the following actions:
	•	Fills the user pool with 3 users
	•	Lists all unused users
	•	Retrieves and removes an unused user
	•	Lists remaining unused users
	•	Fills the user pool with 50 users
	•	Lists all unused users after filling the pool
	•	Flushes all users from the pool
	•	Lists all unused users after flushing the pool

## GitHub Actions

This project includes a GitHub Actions workflow that runs tests automatically on pull requests and pushes to the `master` branches. You can also trigger the workflow manually.

To manually trigger the workflow:

1. Go to the "Actions" tab in your GitHub repository.
2. Select the "Test Environment" workflow.
3. Click the "Run workflow" button.

The workflow performs the following steps:

- Checks out the code
- Sets up Docker Compose
- Builds and starts the Docker containers
- Waits for the services to be ready
- Runs the `test.sh` script
- Shuts down the Docker Compose services

## Contributing

Contributions are welcome!
