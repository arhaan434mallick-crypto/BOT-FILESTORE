import os

LOGGER = True
PORT = int(os.environ.get("PORT", 8080))
OWNER_ID = int(os.environ.get("OWNER_ID", "7500587425"))
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
DATABASE_URL = os.environ.get("DATABASE_URL", "")
DB_URI = os.environ.get("DATABASE_URL", "")
API_ID = int(os.environ.get("API_ID", 2040))
API_HASH = os.environ.get("API_HASH", "b18441a1ff607e106cf4ead0914d7a42")

# The missing variable
SESSION = os.environ.get("SESSION", "Alya_Bot")

# Shortener Vars
SHORT_URL = os.environ.get("SHORT_URL", "")
SHORT_API = os.environ.get("SHORT_API", "")
SHORT_TUT = os.environ.get("SHORT_TUT", "")
