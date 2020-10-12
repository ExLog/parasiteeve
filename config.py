from API import *
# Get variables from .env
token = os.getenv('TOKEN')
prefix = os.getenv('PREFIX')
server = int(os.getenv('GUILD_ID'))
channel_id = int(os.getenv('CHANNEL_ID'))
Server_Key_API = os.getenv('SERVER_KEY_API')
