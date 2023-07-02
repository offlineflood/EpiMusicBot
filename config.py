from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://graph.org/file/16805c3220aff0f9b74be.jpg")
START_IMG = getenv("START_IMG", "https://graph.org/file/16805c3220aff0f9b74be.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/justtalkinggrop")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/justtalkinggrop")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6212838686").split()))


FAILED = "https://graph.org/file/52cc2b744f86802aa82ac.jpg"
