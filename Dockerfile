FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . . 


# The URL to the InfluxDB instance
ENV INFLUXDB_URL=http://localhost:8086

# The InfluxDB token
ENV INFLUXDB_TOKEN=your_token

# The InfluxDB Org
ENV INFLUXDB_ORG=your_org

# The InfluxDB bucket
ENV INFLUXDB_BUCKET=your_bucket

# The URL to ping
ENV PING_URL=http://example.com

# Interval in seconds
ENV INTERVAL=60

CMD ["python", "ping_to_influx.py"]