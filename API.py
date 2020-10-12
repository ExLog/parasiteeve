import json
import requests
import os
from config import *

try:
    website_status = True
    api_request = requests.get(
        f"https://minecraftpocket-servers.com/api/?object=servers&element=detail&key={Server_Key_API}")
    api = json.loads(api_request.content)
    server_name = api["name"]
    ip = api["address"]
    port = api["port"]
    rank = api["rank"]
    online_now = api["is_online"]
    last_check = api["last_check"]
except Exception:
    website_status = False
