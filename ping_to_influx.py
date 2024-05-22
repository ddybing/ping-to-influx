import requests
import time
import os
from  influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import schedule
from tcp_latency import measure_latency


ping_host = os.getenv('PING_URL', 'www.example.com')
influx_token = os.getenv('INFLUXDB_TOKEN', 'your_token_here')
influx_org = os.getenv('INFLUXDB_ORG', 'your_org_here')
influx_bucket = os.getenv('INFLUXDB_BUCKET', 'your_bucket_here')
influx_url = os.getenv('INFLUXDB_URL', 'http://localhost:8086')
interval = os.getenv('INTERVAL', 60)


client = InfluxDBClient(url=influx_url, token=influx_token, org=influx_org)
write_api = client.write_api(write_options=SYNCHRONOUS)

def ping_service():
    latency = measure_latency(host=ping_host)

    # Round latency to one decimal place
    latency = (round(latency[0], 1))

    print("Ping latency: ", latency)
    point = Point("ping_latency").field("latency", latency)
    write_api.write(bucket=influx_bucket, record=point)

# Convert interval to integer
try:
    interval = int(interval)
except ValueError:
    raise ValueError("INTERVAL environment variable must be an integer")

schedule.every(interval).seconds.do(ping_service)

while True:
    schedule.run_pending()
    time.sleep(1)
