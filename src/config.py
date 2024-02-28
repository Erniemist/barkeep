import os
from dotenv import load_dotenv

load_dotenv()

MIN_PLAYERS = int(os.getenv("MIN_PLAYERS", "5"))
