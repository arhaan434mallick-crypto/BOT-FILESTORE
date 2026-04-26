import os

LOGGER = True
PORT = int(os.environ.get("PORT", 8080))
OWNER_ID = int(os.environ.get("OWNER_ID", "7500587425"))
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
DATABASE_URL = os.environ.get("DATABASE_URL", "")
# Some bots use these names instead:
DB_URI = os.environ.get("DATABASE_URL", "")
API_ID = int(os.environ.get("API_ID", 0))
API_HASH = os.environ.get("API_HASH", "")

# Shortener Vars
SHORT_URL = os.environ.get("SHORT_URL", "")
SHORT_API = os.environ.get("SHORT_API", "")
SHORT_TUT = os.environ.get("SHORT_TUT", "")
