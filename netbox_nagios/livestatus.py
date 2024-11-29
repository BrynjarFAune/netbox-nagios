import json
import requests

TIMEOUT = 3  # seconds
BUFFER_SIZE = 4096  # bytes

def hoststatus(hostname: str, api_url: str, api_key: str):
    headers = {"Authorization": f"Bearer {api_key}"}
    url = f"{api_url}/objects/hoststatus"

    try:
        response = requests.get(url, headers=headers, timeout=TIMEOUT)
        response.raise_for_status()

        data = response.json()
        for host in data.get("hoststatus", []):
            if host.get("host_name") == hostname:
                return host
    except requests.exceptions.RequestException as e:
        print(f"Error fetching host status: {e}")
        return None
    
    return None











