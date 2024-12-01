import json
import requests

TIMEOUT = 3  # seconds
BUFFER_SIZE = 4096  # bytes

def hoststatus(hostname: str, api_url: str, api_key: str):
    url = f"{api_url}/objects/hoststatus?apikey={api_key}"

    try:
        response = requests.get(url, timeout=TIMEOUT)
        response.raise_for_status()

        data = response.json()
        for host in data.get("hoststatus", []):
            if host.get("host_name") == hostname:
                return host
    except requests.exceptions.RequestException as e:
        print(f"Error fetching host status: {e}")
        return None
    
    return None











