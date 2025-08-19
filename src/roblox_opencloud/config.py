import os
from dotenv import load_dotenv

load_dotenv()  # Loads .env if present

RBXWIRENET_GROUP_API_KEY = os.getenv("RBXWIRENET_GROUP_API_KEY")
BASE_URL = "https://apis.roblox.com/cloud/v2/"

if not RBXWIRENET_GROUP_API_KEY:
    raise ValueError("RBXWIRENET_GROUP_API_KEY is not set in environment variables.")
