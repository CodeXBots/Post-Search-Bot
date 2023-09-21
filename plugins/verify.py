from info import *
from utils import *
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 

@Client.on_message(filters.group & filters.command("verify"))
async def _verify(bot, message):
    try:
       group     = await get_group(message.chat.id)
       user_id   = group["user_id"] 
       user_name = group["user_name"]
       verified  = group["verified"]
    except:     
       return await bot.leave_chat(message.chat.id)  
    try:       
       user = await bot.get_users(user_id)
    except:
       return await message.reply(f"{user_name},\nꜱᴛᴀʀᴛ ᴍᴇ ɪɴ ᴘᴍ")
    if message.from_user.id != user_id:
       return await message.reply(f"Only {user.mention} can use this command 😁")
    if verified==True:
       return await message.reply("ᴛʜɪꜱ ɢʀᴏᴜᴘ ɪꜱ ᴀʟʀᴇᴀᴅʏ ᴠᴇʀɪꜰɪᴇᴅ!!")
    try:
       link = (await bot.get_chat(message.chat.id)).invite_link     
    except:
       return message.reply("ᴍᴀᴋᴇ ᴍᴇ ᴀᴅᴍɪɴ ᴡɪᴛʜ ᴀʟʟ ᴘᴇʀᴍɪꜱꜱɪᴏɴꜱ")    
           
    text  = f"#NewRequest\n\n"
    text += f"User: {message.from_user.mention}\n"
    text += f"User ID: `{message.from_user.id}`\n"
    text += f"Group: [{message.chat.title}]({link})\n"
    text += f"Group ID: `{message.chat.id}`\n"
   
    await bot.send_message(chat_id=LOG_CHANNEL,
                           text=text,
                           disable_web_page_preview=True,
                           reply_markup=InlineKeyboardMarkup(
                                                 [[InlineKeyboardButton("✅ ᴀᴘᴘʀᴏᴠᴇ", callback_data=f"verify_approve_{message.chat.id}"),
                                                   InlineKeyboardButton("❌ ᴅᴇᴄʟɪɴᴇ", callback_data=f"verify_decline_{message.chat.id}")]]))
    await message.reply("ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ʀᴇǫᴜᴇꜱᴛ ꜱᴇɴᴛ ✅️\nᴡᴇ ᴡɪʟʟ ɴᴏᴛɪꜰʏ ʏᴏᴜ ᴡʜᴇɴ ɪᴛ ɪꜱ ᴀᴘᴘʀᴏᴠᴇᴅ")



@Client.on_callback_query(filters.regex(r"^verify"))
async def verify_(bot, update):
    id = int(update.data.split("_")[-1])
    group = await get_group(id)
    name  = group["name"]
    user  = group["user_id"]
    if update.data.split("_")[1]=="approve":
       await update_group(id, {"verified":True})
       await bot.send_photo(chat_id=user, photo='https://telegra.ph/file/a706afc296de6da2a40c8.jpg', caption=f"<b>ʏᴏᴜʀ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀ {name} ʜᴀꜱ ʙᴇᴇɴ ᴀᴘᴘʀᴏᴠᴇᴅ ✅</b>", 
       reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🎪  ꜱᴜʙꜱᴄʀɪʙᴇ ᴍʏ ʏᴛ ᴄʜᴀɴɴᴇʟ  🎪", url="https://youtube.com/@NobiDeveloper")]]))
       await update.message.edit(update.message.text.html.replace("#NewRequest", "#Approved"))
    else:
       await delete_group(id)
       await bot.send_message(chat_id=user, text=f"Your verification request for {name} has been declined 😐 Please Contact Admin")
       await update.message.edit(update.message.text.html.replace("#NewRequest", "#Declined")) 