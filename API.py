import json
import requests
from API_KEY import SERVER_API_KEY
try:
    website_status = True
    # Change your SERVER_API_KEY to your own Server Key.
    api_request = requests.get(f"https://minecraftpocket-servers.com/api/?object=servers&element=detail&key={SERVER_API_KEY}")
    api = json.loads(api_request.content)
    server_name = api["name"]
    ip = api["address"]
    port = api["port"]
    rank = api["rank"]
    online_now = api["is_online"]
    last_check = api["last_check"]
except Exception:
    website_status = False