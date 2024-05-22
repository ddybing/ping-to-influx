# Ping to InfluxDB

This project measures the latency of a ping to a specified host and writes the latency data to an InfluxDB instance.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Docker
- Python 3.9

### Installing

1. Clone the repository to your local machine.

2. Build the Docker image:

```sh 
docker build -t ping_to_influx .
```

3. Run the Docker container:

```sh
docker run -e INFLUXDB_URL=http://localhost:8086 \
           -e INFLUXDB_TOKEN=your_token \
           -e INFLUXDB_ORG=your_org \
           -e INFLUXDB_BUCKET=your_bucket \
           -e PING_URL=http://example.com \
           -e INTERVAL=60 \
           ping_to_influx
```

Replace the placeholder values (`http://localhost:8086`, `your_token`, `your_org`, `your_bucket`, `http://example.com`, `60`) with your actual values.

## Built With

- [Python 3.9](https://www.python.org/)
- [InfluxDB Python Client](https://github.com/influxdata/influxdb-client-python)
- [tcp-latency](https://pypi.org/project/tcp-latency/)
- [schedule](https://pypi.org/project/schedule/)

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details
