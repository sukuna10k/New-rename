from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply
from pyrogram import Client , filters




@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
    text = """** Plan Gratuit User**
Limite de téléchargement quotidienne : 5 Go.
Prix 0

**🪙 Basic**
Limite de téléchargement quotidienne : 20 Go  
Prix : 1000F $ par mois.

**⚡ Standard**
Limite de téléchargement quotidienne : 50 Go  
Prix : 1500F par mois.

**💎 Pro**
Limite de téléchargement quotidienne : 100 Go  
Prix : 2000F par mois.

Payment Details :-
<b>➜ UPI ID :</b> <code>TechifyBots@UPI</code>

Après le paiement, envoyez des captures d'écran du paiement à l'administrateur @Kingcey."""
    
    keybord = InlineKeyboardMarkup([
        [InlineKeyboardButton("🦋 Admin", url = "https://telegram.me/Kingcey"),
        InlineKeyboardButton("✖️ Annuler", callback_data="cancel")]
        ])
    
    await update.message.edit(text = text,reply_markup = keybord, disable_web_page_preview=True)
    
    

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
    text = """**Free Plan User**
Limite de téléchargement quotidienne : 5 Go.
Prix 0

**🪙 Basic**
Limite de téléchargement quotidienne : 20 Go  
Prix : 1000F $ par mois.

**⚡ Standard**
Limite de téléchargement quotidienne : 50 Go  
Prix : 1500F par mois.

**💎 Pro**
Limite de téléchargement quotidienne : 100 Go  
Prix : 2000F par mois.

Payment Details :-
<b>➜ UPI ID :</b> <code>TechifyBots@UPI</code>

Après le paiement, envoyez des captures d'écran du paiement à l'administrateur @Kingcey"""
    
    keybord = InlineKeyboardMarkup([
        [InlineKeyboardButton("🦋 Admin", url = "https://telegram.me/kingcey"),
        InlineKeyboardButton("✖️ Annuler", callback_data="cancel")]
        ])
    
    await message.reply_text(text=text, reply_markup=keybord, quote=True, disable_web_page_preview=True)
