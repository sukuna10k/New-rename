from datetime import date as date_
import os, re, datetime, random, asyncio, time, humanize
from script import *
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from pyrogram import Client, filters, enums
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup)
from helper.progress import humanbytes
from helper.database import botdata, find_one, total_user
from helper.database import insert, find_one, used_limit, usertype, uploadlimit, addpredata, total_rename, total_size
from pyrogram.file_id import FileId
from helper.database import daily as daily_
from helper.date import check_expi
from config import *

token = BOT_TOKEN
botid = token.split(':')[0]





@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    user_id = message.chat.id
    old = insert(int(user_id))
    
    try:
        id = message.text.split(' ')[1]
    except IndexError:
        id = None

    loading_sticker_message = await message.reply_sticker("CAACAgQAAxkBAAIOW2fB4io50g9FjXU6rzvrtr9ljoZpAAI2DQAC3_MhU7xmT478a5PAHgQ")
    await asyncio.sleep(2)
    await loading_sticker_message.delete()
    
    text = f"""{message.from_user.mention} \n<b>Je suis Yor Kingcey ||forger|| l'épouse de roi kingcey je suis un bot puissant capable de renommé n'importe quel type de fichier, comme je le fait avec mes proies.\n\n\n┣⪼<blockquote>||Remercier mon époux de m'avoir créé||</b></blockquote>"""
    
    button = InlineKeyboardMarkup([
        [InlineKeyboardButton("📢 Updates", url="https://telegram.me/BotZFlix"),
        InlineKeyboardButton("💬 Support", url="https://telegram.me/BotZFlixSupport")],
        [InlineKeyboardButton("🛠️ Aide", callback_data='help'),
        InlineKeyboardButton("❤️‍🩹 About", callback_data='about')],
        [InlineKeyboardButton("♨️ Mis à jour premium ♨️", callback_data='upgarde')]
        ])
    
    await message.reply_photo(
        photo=START_PIC,
        caption=text,
        reply_markup=button,
        quote=True
        )
    return    



@Client.on_message((filters.private & (filters.document | filters.audio | filters.video)) | filters.channel & (filters.document | filters.audio | filters.video))
async def send_doc(client, message):
    user_id = message.chat.id
    old = insert(int(user_id))
        
    user_id = message.from_user.id    
    if FORCE_SUBS:
        try:
            await client.get_chat_member(FORCE_SUBS, user_id)
        except UserNotParticipant:
            _newus = find_one(message.from_user.id)
            user = _newus["usertype"]
            await message.reply_text("<b>Salut Toi Je suis princesse Hibara \n\nTu dois rejoindre ma chaîne pour m'utiliser.\n\nVeuillez gentiment rejoindre la chaîne.</b>",
                                     reply_to_message_id=message.id,
                                     reply_markup=InlineKeyboardMarkup([
                                         [InlineKeyboardButton("🔺 Rejoindre 🔺", url=f"https://t.me/{FORCE_SUBS}")]
                                         ]))
            await client.send_message(LOG_CHANNEL, f"<b><u>Un utilisateur a demmaré le bot.</u></b> \n\n<b>User ID :</b> <code>{user_id}</code> \n<b>First Name :</b> {message.from_user.first_name} \n<b>Last Name :</b> {message.from_user.last_name} \n<b>User Name :</b> @{message.from_user.username} \n<b>User Mention :</b> {message.from_user.mention} \n<b>User Link :</b> <a href='tg://openmessage?user_id={user_id}'>Click Here</a> \n<b>User Plan :</b> {user}")
            return
		
    botdata(int(botid))
    bot_data = find_one(int(botid))
    prrename = bot_data['total_rename']
    prsize = bot_data['total_size']
    user_deta = find_one(user_id)
    used_date = user_deta["date"]
    buy_date = user_deta["prexdate"]
    daily = user_deta["daily"]
    user_type = user_deta["usertype"]

    c_time = time.time()

    if user_type == "Free":
        LIMIT = 120
    else:
        LIMIT = 10
    then = used_date + LIMIT
    left = round(then - c_time)
    conversion = datetime.timedelta(seconds=left)
    ltime = str(conversion)
    if left > 0:
        await message.reply_text(f"<b>Désolé, je ne suis pas seulement pour toi. \n\nLe contrôle de saturation est actif, donc veuillez attendre. {ltime} </b>", reply_to_message_id=message.id)
    else:
        # Forward a single message
        media = await client.get_messages(message.chat.id, message.id)
        file = media.document or media.video or media.audio
        dcid = FileId.decode(file.file_id).dc_id
        filename = file.file_name
        file_id = file.file_id
        value = 2147483648
        used_ = find_one(message.from_user.id)
        used = used_["used_limit"]
        limit = used_["uploadlimit"]
        expi = daily - int(time.mktime(time.strptime(str(date_.today()), '%Y-%m-%d')))
        if expi != 0:
            today = date_.today()
            pattern = '%Y-%m-%d'
            epcho = int(time.mktime(time.strptime(str(today), pattern)))
            daily_(message.from_user.id, epcho)
            used_limit(message.from_user.id, 0)
        remain = limit - used
        if remain < int(file.file_size):
            await message.reply_text(f"100 % de quotidien {humanbytes(limit)} Quota de données épuisé.\n\n<b>Taille de fichier détectée :</b> {humanbytes(file.file_size)}\n<b>Limite quotidienne utilisée :</b> {humanbytes(used)}\n\nIl ne vous reste que <b>{humanbytes(remain)}</b> Restant sur votre compte\n\nSi vous souhaitez renommer un gros fichier, mettez à niveau votre plan", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("💳 Mettre à jour", callback_data="upgrade")]]))
            return
        if value < file.file_size:
            
            if STRING_SESSION:
                if buy_date == None:
                    await message.reply_text(f"Vous ne pouvez pas télécharger un fichier de plus de 2 Go..\n\nVotre plan ne permet pas de télécharger des fichiers de plus de 2 Go.\n\nMettez à niveau votre plan pour renommer des fichiers de plus de 2 Go.", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("💳 Mettre à jour", callback_data="upgrade")]]))
                    return
                pre_check = check_expi(buy_date)
                if pre_check == True:
                    await message.reply_text(f"""__Que veux-tu que je fasse avec ce fichier ?__\n\n**Nom du fichier :** `{filename}`\n**Poids du fichier :** {humanize.naturalsize(file.file_size)}\n**DC ID :** {dcid}""", reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("📝 Renommer", callback_data="rename"), InlineKeyboardButton("✖️ Annuler", callback_data="cancel")]]))
                    total_rename(int(botid), prrename)
                    total_size(int(botid), prsize, file.file_size)
                else:
                    uploadlimit(message.from_user.id, 2147483648)
                    usertype(message.from_user.id, "Free")

                    await message.reply_text(f'Votre plan a expiré le {buy_date}', quote=True)
                    return
            else:
                await message.reply_text("Vous ne pouvez pas télécharger un fichier de plus de 2 Go.\n\nVotre plan ne permet pas de télécharger des fichiers de plus de 2 Go.\n\nMettez à niveau votre plan pour renommer des fichiers de plus de 2 Go.", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("💳 Mettre à jour", callback_data="upgrade")]]))
                return
        else:
            if buy_date:
                pre_check = check_expi(buy_date)
                if pre_check == False:
                    uploadlimit(message.from_user.id, 2147483648)
                    usertype(message.from_user.id, "Free")
            
            filesize = humanize.naturalsize(file.file_size)
            fileid = file.file_id
            total_rename(int(botid), prrename)
            total_size(int(botid), prsize, file.file_size)
            await message.reply_text(f"""__Voulez Vous Renommer ce fichier ?__\n\n**Nom :** `{filename}`\n**Poids :** {filesize}\n**DC ID :** {dcid}""", reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("📝 Oui", callback_data="rename"),
                  InlineKeyboardButton("✖️ Non", callback_data="cancel")]]))
