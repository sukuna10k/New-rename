import os



# Required Variables Config
API_ID = int(os.environ.get("API_ID", "24817837"))
API_HASH = os.environ.get("API_HASH", "acd9f0cc6beb08ce59383cf250052686")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8074880690:AAHlE1byWBOcy3LOhg_gbKbZWQ48_t1KEgQ")
ADMIN = int(os.environ.get("ADMIN", "7428552084"))


# Premium 4GB Renaming Client Config
STRING_SESSION = os.environ.get("STRING_SESSION", "BAF6sK0Adox21RgTZ9IYmyO2AWwIMZKq_pyFsT01TYqsTWfCTEAmU5pUfeCHsenPDOW0sLu3_nyp9jMSTYj6tclCJ_M9ZhphXSvUzBpOcRs0KB4Oh9qoT2HGNmX3z9wDJB6JAzt6Ar-kY8wypGA88E3pGyQtQeeW30lMUtysOn97CllaJVJhno3gRsn06YM-sVUXjCQIwSG4b3LexvJeVifWXGIfpzOCf5iR4AFD_qvdyi_U5pwbl2xvRx7T-_ahSSNUg_-i3exoBbM2BQVO9Gk3ByKBfaFkgrTyjURkU-cC-mgCEiZeqyGOluShG0TqxGB6keyfS0AlWPFhA8P01bbGDFLaTwAAAAG6xrWUAA")


# Log & Force Channel Config
FORCE_SUBS = os.environ.get("FORCE_SUBS", "botzflix")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002376378205"))


# Mongo DB Database Config
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://botzflix:zflixteam@botzflix.p19sv.mongodb.net/?retryWrites=true&w=majority&appName=botzflix")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "botzflix")


# Other Variables Config
START_PIC = os.environ.get("START_PIC", "https://envs.sh/tun.jpg")
