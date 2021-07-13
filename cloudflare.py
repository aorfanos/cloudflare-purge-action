import requests
import json
import os
import sys

CF_API_BASE = "https://api.cloudflare.com/client/v4"

cf_api_key = os.environ.get("CF_API_KEY")
cf_email_addr = os.environ.get("CF_EMAIL_ADDR")
cf_token = os.environ.get("CF_TOKEN")
cf_zone_name = os.environ.get("CF_ZONE_NAME")
cf_purge_urls = os.environ.get("CF_PURGE_URLS")
cf_purge_hosts = os.environ.get("CF_PURGE_HOSTS")
cf_purge_prefixes = os.environ.get("CF_PURGE_PREFIXES")
cf_purge_tags = os.environ.get("CF_PURGE_TAGS")

# use legacy global API key if cf_token input is not defined
if cf_token is None:
    headers_default = {
        "Content-Type": "application/json",
        "X-Auth-Email": f"{cf_email_addr}",
        "X-Auth-Key": f"{cf_api_key}",
    }
else:
    headers_default = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {cf_token}",
    }

if cf_purge_urls is not None:
    data = {
        "files": [f'"{cf_purge_urls}"']
    }
elif cf_purge_hosts is not None:
    data = {
        "hosts": [f'"{cf_purge_hosts}"']
    } 
elif cf_purge_prefixes is not None:
    data = {
        "prefixes": [f'"{cf_purge_prefixes}"']
    }
elif cf_purge_tags is not None:
    data = {
        "tags": [f'"{cf_purge_tags}"']
    }
else:
    data = {
        "purge_everything": True,
    }

def ZoneNameToID(zoneName: str):
    request = requests.get(f"{CF_API_BASE}/zones", headers=headers_default)
    _jsonized_req = request.json()
    _data_block = _jsonized_req["result"]

    for zone in _data_block:
        if zone["name"] == zoneName:
            return zone["id"]
        else:
            return None

def purgeCFCache(zoneID: str):
    request = requests.post(f"{CF_API_BASE}/zones/{zoneID}/purge_cache", headers=headers_default, json=data)
    if request.status_code != 200:
        sys.exit(f"Exited with status code {request.status_code}\nInfo: {request.text}")
    else:
        return print("Cache purged successfully.")

if __name__ == '__main__':
    purgeCFCache(ZoneNameToID(cf_zone_name))
