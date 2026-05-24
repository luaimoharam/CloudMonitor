import requests

# List of services to check
SERVICES = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.openai.com"
]

def check_uptime(service_list):
    print("--- Starting Uptime Monitor ---")
    
    for url in service_list:
        try:
            # Send a GET request
            response = requests.get(url, timeout=5)
            
            # Check if status code is 200 (OK)
            if response.status_code == 200:
                print(f"[UP] {url} - Status: {response.status_code}")
            else:
                print(f"[WARNING] {url} - Status: {response.status_code}")
                
        except requests.exceptions.RequestException as e:
            # This catches connection errors, DNS issues, etc.
            print(f"[DOWN] {url} - Error: {e}")

    print("--- Check Complete ---")

if __name__ == "__main__":
    check_uptime(SERVICES)