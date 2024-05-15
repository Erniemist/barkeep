import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN", "")
SERVER_ID = os.getenv("SERVER_ID")
MIN_PLAYERS = int(os.getenv("MIN_PLAYERS", "5"))
AVALON_ENABLED = os.getenv("AVALON_ENABLED", "0") == "1"
