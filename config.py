import os

class Config(object):
    LOGGER = True
    PORT = int(os.environ.get("PORT", 8080))
    OWNER_ID = int(os.environ.get("OWNER_ID", "7500587425"))
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    SHORT_URL = os.environ.get("SHORT_URL", "")
    SHORT_API = os.environ.get("SHORT_API", "")
    SHORT_TUT = os.environ.get("SHORT_TUT", "")
