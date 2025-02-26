from pyrogram import Client, idle
from plugins.cb_data import app as Client2
from config import *
import pyromod
import pyrogram.utils
from flask import Flask
import threading

pyrogram.utils.MIN_CHAT_ID = -999999999999
pyrogram.utils.MIN_CHANNEL_ID = -100999999999999

bot = Client("Renamer", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH, plugins=dict(root='plugins'))

# Création de l'application Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Le bot fonctionne !"

def run_flask():
    app.run(host="0.0.0.0", port=8080)

if STRING_SESSION:
    apps = [Client2, bot]
    for app in apps:
        app.start()
    
    # Lancer Flask dans un thread séparé
    threading.Thread(target=run_flask).start()
    
    idle()

    for app in apps:
        app.stop()
else:
    bot.run()
