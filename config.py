import os



# Required Variables Config
API_ID = int(os.environ.get("API_ID", "29534418"))
API_HASH = os.environ.get("API_HASH", "5f15dd792990ade40a43ae17413b422f")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7305555008:AAFgmI9RfgNpY8b8KdGR1NoHSdgTVTHVjjM")
ADMIN = int(os.environ.get("ADMIN", "5691486059"))


# Premium 4GB Renaming Client Config
STRING_SESSION = os.environ.get("STRING_SESSION", "")


# Log & Force Channel Config
FORCE_SUBS = os.environ.get("FORCE_SUBS", "-1002322660786")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002322660786"))


# Mongo DB Database Config
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://ks0360683:Ybz9rKOKYilsb38w@cluster0.x6nn0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "ks0360683")


# Other Variables Config
START_PIC = os.environ.get("START_PIC", "https://graph.org/file/ada3f739fed7efdbe7b08.jpg")
