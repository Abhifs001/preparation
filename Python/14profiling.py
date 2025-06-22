import time
from contextlib import contextmanager

import requests

@contextmanager
def log_time(task_name):
    start = time.time()
    print(f"Started: {task_name}")
    yield
    end = time.time()
    print(f"Completed: {task_name} in {end - start:.2f}s")

# Usage
with log_time("Fetch stock data"):
    response = requests.get("https://api.example.com/stocks/NSE")
    time.sleep(2)  # simulate API call




#note 
# with log_time("Fetch stock data"):
#     time.sleep(2)  # simulate API call

# This simulates that the Fetch stock data task takes 2 seconds — as if you were calling a real trading API like NSE/BSE or fetching data from Alpha Vantage or Bloomberg.4

# with log_time("Fetch stock price"):
#     response = requests.get("https://api.example.com/stocks/TCS")


