from info import *
from utils import *
from asyncio import sleep
from pyrogram import Client, filters 

@Client.on_message(filters.group & filters.new_chat_members)
async def new_group(bot, message):
    bot_id = (await bot.get_me()).id
    member = [u.id for u in message.new_chat_members]        
    if bot_id in member:
       await add_group(group_id=message.chat.id, 
                       group_name=message.chat.title,
                       user_name=message.from_user.first_name, 
                       user_id=message.from_user.id, 
                       channels=[],
                       f_sub=False,
                       verified=False)
       m=await message.reply(f"<b>☤ ᴛʜᴀɴᴋ ʏᴏᴜ ꜰᴏʀ ᴀᴅᴅɪɴɢ ᴍᴇ ɪɴ {message.chat.title}\n\n🤖 ᴅᴏɴ’ᴛ ꜰᴏʀɢᴇᴛ ᴛᴏ ᴍᴀᴋᴇ ᴍᴇ ᴀᴅᴍɪɴ 🤖\n\n♻️ ᴘʟᴇᴀꜱᴇ ɢᴇᴛ ᴀᴄᴄᴇꜱꜱ ʙʏ /verify ᴄᴏᴍᴍᴀɴᴅ\n\n🕵️ ɪꜰ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ᴅᴏᴜʙᴛ ʏᴏᴜ ᴄʟᴇᴀʀ ɪᴛ ᴜsɪɴɢ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴs</b>", 

reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🥷  ʜᴇʟᴘ  🥷", url="https://telegram.me/CodeXSupport")],

[InlineKeyboardButton("🧑‍💻  ᴏᴡɴᴇʀ  🧑‍💻", url="https://telegram.me/CodeXBro")]]))
       text=f"#NewGroup\n\nGroup: {message.chat.title}\nGroupID: `{message.chat.id}`\nAddedBy: {message.from_user.mention}\nUserID: `{message.from_user.id}`"
       await bot.send_message(chat_id=LOG_CHANNEL, text=text)
       await sleep(120)
       await m.delete()