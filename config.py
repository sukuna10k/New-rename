import os



# Required Variables Config
API_ID = int(os.environ.get("API_ID", "24817837"))
API_HASH = os.environ.get("API_HASH", "acd9f0cc6beb08ce59383cf250052686")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7307692677:AAGK834DvcyPcKf6RXP4-eEjKWxy_PZG2NU")
ADMIN = int(os.environ.get("ADMIN", "7428552084"))


# Premium 4GB Renaming Client Config
STRING_SESSION = os.environ.get("STRING_SESSION", "")


# Log & Force Channel Config
FORCE_SUBS = os.environ.get("FORCE_SUBS", "botzflix")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002376378205"))


# Mongo DB Database Config
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://tgbot:4KzEdxEl4YldwwFR@tg.vr8ef.mongodb.net/?retryWrites=true&w=majority&appName=Tg")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "botzflix")


# Other Variables Config
START_PIC = os.environ.get("START_PIC", "https://envs.sh/i57.jpg")
