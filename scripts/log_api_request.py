import requests
import json
from datetime import datetime
import os

url = "https://dummyjson.com/todos"

response = requests.get(url)
data = response.json()

output = {
    "time": str(datetime.now()),
    "data": data
}

output_path = "/home/may-thin-kyi/cron-job/api.json"
os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(output_path, "w") as f:
    f.write(json.dumps(output) + "\n")

print("Data saved successfully")