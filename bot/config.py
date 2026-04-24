# config.py
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

DATABASE_URL = os.getenv("DATABASE_URL")

LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID"))

TOPIC_BUG = int(os.getenv("TOPIC_BUG"))
TOPIC_ERROR = int(os.getenv("TOPIC_ERROR"))
TOPIC_REPORT = int(os.getenv("TOPIC_REPORT"))
TOPIC_OTHER = int(os.getenv("TOPIC_OTHER"))
TOPIC_USERS = int(os.getenv("TOPIC_USERS"))
