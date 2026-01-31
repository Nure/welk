import requests
import time
import random

# Replace with your AWS EC2 Public IP or 'localhost' if running on the server
API_BASE_URL = "http://localhost:8000/api/v1"

endpoints = [
    "/items/",
    "/items/error",
    "/items/?query=devops",
    "/non-existent-page"  # This will generate 404s for your dashboard
]

def run_traffic():
    print(f"Starting Traffic Generator on {API_BASE_URL}...")
    print("Press Ctrl+C to stop.")
    
    while True:
        target = random.choice(endpoints)
        url = f"{API_BASE_URL}{target}"
        
        try:
            start = time.time()
            response = requests.get(url, timeout=5)
            latency = round(time.time() - start, 4)
            
            print(f"Sent GET {target} | Status: {response.status_code} | Latency: {latency}s")
            
        except requests.exceptions.ConnectionError:
            print("Error: Cannot connect to API. Is the Docker container running?")
        except Exception as e:
            print(f"⚠️ Unexpected error: {e}")
        
        # Random sleep between 0.5 to 2 seconds to simulate human behavior
        time.sleep(random.uniform(0.5, 2.0))

if __name__ == "__main__":
    run_traffic()