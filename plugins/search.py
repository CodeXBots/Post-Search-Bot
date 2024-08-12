import asyncio
from info import *
from utils import *
from time import time 
from plugins.generate import database
from pyrogram import Client, filters 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message 

async def send_message_in_chunks(client, chat_id, text):
    max_length = 4096
    for i in range(0, len(text), max_length):
        msg = await client.send_message(chat_id=chat_id, text=text[i:i+max_length])
        asyncio.create_task(delete_after_delay(msg, 1800))

async def delete_after_delay(message: Message, delay):
    await asyncio.sleep(delay)
    try:
        await message.delete()
    except:
        pass

@Client.on_message(filters.text & filters.group & filters.incoming & ~filters.command(["verify", "connect", "id"]))
async def search(bot, message):
    Rahul = database.find_one({"chat_id": ADMIN})
    if Rahul == None:
        return await message.reply("**Contact Admin Then Say To Login In Bot.**")
    User = Client("post_search", session_string=Rahul['session'], api_hash=API_HASH, api_id=API_ID)
    await User.connect()
    f_sub = await force_sub(bot, message)
    if f_sub==False:
       return     
    channels = (await get_group(message.chat.id))["channels"]
    if bool(channels)==False:
       return     
    if message.text.startswith("/"):
       return    
    query   = message.text 
    head    = "<b>⇩  ʜᴇʀᴇ ɪꜱ ʏᴏᴜʀ ʀᴇꜱᴜʟᴛꜱ  ⇩</b>\n\n"
    results = ""
    try:
       for channel in channels:
           async for msg in User.search_messages(chat_id=channel, query=query):
               name = (msg.text or msg.caption).split("\n")[0]
               if name in results:
                  continue 
               results += f"<b>🎬 {name}\n {msg.link} </b>\n\n"                                                      
       if bool(results)==False:
          movies = await search_imdb(query)
          buttons = []
          for movie in movies: 
              buttons.append([InlineKeyboardButton(movie['title'], callback_data=f"recheck_{movie['id']}")])
          msg = await message.reply("𝗜 𝗰𝗼𝘂𝗹𝗱𝗻'𝘁 𝗳𝗶𝗻𝗱 𝗮𝗻𝘆𝘁𝗵𝗶𝗻𝗴 𝗿𝗲𝗹𝗮𝘁𝗲𝗱 𝘁𝗼 𝘁𝗵𝗮𝘁.\n𝗗𝗶𝗱 𝘆𝗼𝘂 𝗺𝗲𝗮𝗻 𝗮𝗻𝘆 𝗼𝗻𝗲 𝗼𝗳 𝘁𝗵𝗲𝘀𝗲 ??", 
                                          reply_markup=InlineKeyboardMarkup(buttons))
       else:
          await send_message_in_chunks(bot, message.chat.id, head+results)
    except:
       pass

@Client.on_callback_query(filters.regex(r"^recheck"))
async def recheck(bot, update):
    Rahul = database.find_one({"chat_id": ADMIN})
    User = Client("post_search", session_string=Rahul['session'], api_hash=API_HASH, api_id=API_ID)
    if Rahul == None:
        return await update.message.edit("**Contact Admin Then Say To Login In Bot.**")
    await User.connect()
    clicked = update.from_user.id
    try:      
       typed = update.message.reply_to_message.from_user.id
    except:
       return await update.message.delete(2)       
    if clicked != typed:
       return await update.answer("ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ꜰᴏʀ ʏᴏᴜ", show_alert=True)

    m=await update.message.edit("<b>ꜱᴇᴀʀᴄʜɪɴɢ ᴘʟᴇᴀꜱᴇ ᴡᴀɪᴛ ♻️</b>")
    id      = update.data.split("_")[-1]
    query   = await search_imdb(id)
    channels = (await get_group(update.message.chat.id))["channels"]
    head    = "<b>ɪ ʜᴀᴠᴇ ꜱᴇᴀʀᴄʜᴇᴅ ᴍᴏᴠɪᴇ ᴡɪᴛʜ ʏᴏᴜʀ ᴡʀᴏɴɢ ꜱᴘᴇʟʟɪɴɢ...\nʙᴜᴛ ᴛᴀᴋᴇ ᴄᴀʀᴇ ɴᴇxᴛ ᴛɪᴍᴇ 😋</b>\n\n"
    results = ""
    try:
       for channel in channels:
           async for msg in User.search_messages(chat_id=channel, query=query):
               name = (msg.text or msg.caption).split("\n")[0]
               if name in results:
                  continue 
               results += f"<b>🎬 {name}\n {msg.link} </b>\n\n"
       if bool(results)==False:          
          return await update.message.edit("<b>⚠️ ɴᴏ ʀᴇꜱᴜʟᴛꜱ ꜰᴏᴜɴᴅ !!\nᴘʟᴇᴀꜱᴇ ʀᴇǫᴜᴇꜱᴛ ᴛᴏ ɢʀᴏᴜᴘ ᴀᴅᴍɪɴ 👇🏻</b>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🧑‍✈️  ʀᴇǫᴜᴇꜱᴛ ᴛᴏ ᴀᴅᴍɪɴ  🧑‍✈️", callback_data=f"request_{id}")]]))
       await send_message_in_chunks(bot, update.message.chat.id, head+results)
    except Exception as e:
       await update.message.edit(f"ᴇʀʀᴏʀ - `{e}`")

@Client.on_callback_query(filters.regex(r"^request"))
async def request(bot, update):
    clicked = update.from_user.id
    try:      
       typed = update.message.reply_to_message.from_user.id
    except:
       return await update.message.delete()       
    if clicked != typed:
       return await update.answer("ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ꜰᴏʀ ʏᴏᴜ", show_alert=True)

    admin = (await get_group(update.message.chat.id))["user_id"]
    id    = update.data.split("_")[1]
    name  = await search_imdb(id)
    url   = "https://www.imdb.com/title/tt"+id
    text  = f"#Request\n\nɴᴀᴍᴇ - {name}\nɪᴍᴅʙ - {url}"
    await bot.send_message(chat_id=admin, text=text, disable_web_page_preview=True)
    await update.answer("ʀᴇǫᴜᴇꜱᴛ ꜱᴇɴᴅ ᴛᴏ ᴀᴅᴍɪɴ  ✅", show_alert=True)
    await update.message.delete(60)
