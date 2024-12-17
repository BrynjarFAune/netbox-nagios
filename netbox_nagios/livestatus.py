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
                host["services"] = servicestatus(hostname, api_url, api_key)
                return host
    except requests.exceptions.RequestException as e:
        print(f"Error fetching host status: {e}")
        return None
    
    return None


def servicestatus(hostname: str, api_url: str, api_key: str):
    url = f"{api_url}/objects/servicestatus?apikey={api_key}"

    try:
        response = requests.get(url, timeout=TIMEOUT)
        response.raise_for_status()

        services = []
        data = response.json()
        for service in data.get("servicestatus", []):
            if service.get("host_name") == hostname:
                services.append(service)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching service status: {e}")
        return None
    
    return services
