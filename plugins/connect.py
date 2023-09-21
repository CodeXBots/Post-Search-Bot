from info import *
from utils import *
from client import User 
from pyrogram import Client, filters

@Client.on_message(filters.group & filters.command("connect"))
async def connect(bot, message):
    m=await message.reply("<b>ᴄᴏɴɴᴇᴄᴛɪɴɢ...</b>")
    user = await User.get_me()
    try:
       group     = await get_group(message.chat.id)
       user_id   = group["user_id"] 
       user_name = group["user_name"]
       verified  = group["verified"]
       channels  = group["channels"].copy()
    except :
       return await bot.leave_chat(message.chat.id)  
    if message.from_user.id!=user_id:
       return await m.edit(f"Only {user_name} can use this command 😁")
    if bool(verified)==False:
       return await m.edit("ᴛʜɪꜱ ᴄʜᴀᴛ ɪꜱ ɴᴏᴛ ᴠᴇʀɪꜰɪᴇᴅ 🚫\nᴜꜱᴇ /verify")    
    try:
       channel = int(message.command[-1])
       if channel in channels:
          return await message.reply("ᴛʜɪꜱ ᴄʜᴀɴɴᴇʟ ɪꜱ ᴀʟʀᴇᴀᴅʏ ᴄᴏɴɴᴇᴄᴛᴇᴅ")
       channels.append(channel)
    except:
       return await m.edit("ɪɴᴄᴏʀʀᴇᴄᴛ ꜰᴏʀᴍᴀᴛ 🚫\nᴜꜱᴇ `/connect` ᴄʜᴀɴɴᴇʟ ɪᴅ")    
    try:
       chat   = await bot.get_chat(channel)
       group  = await bot.get_chat(message.chat.id)
       c_link = chat.invite_link
       g_link = group.invite_link
       await User.join_chat(c_link)
    except Exception as e:
       if "The user is already a participant" in str(e):
          pass
       else:
          text = f"🚫  ᴇʀʀᴏʀ  -  `{str(e)}`\nᴍᴀᴋᴇ ꜱᴜʀᴇ ᴛʜᴀᴛ ɪ ᴀᴍ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴀᴛ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ɢʀᴏᴜᴘ ᴡɪᴛʜ ᴀʟʟ ᴘᴇʀᴍɪꜱꜱɪᴏɴꜱ ᴀɴᴅ {(user.username or user.mention)} ɪꜱ ɴᴏᴛ ʙᴀɴɴᴇᴅ ᴛʜᴇʀᴇ."
          return await m.edit(text)
    await update_group(message.chat.id, {"channels":channels})
    await m.edit(f"ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴛᴏ\n[{chat.title}]({c_link})", disable_web_page_preview=True)
    text = f"#NewConnection\n\nUser: {message.from_user.mention}\nGroup: [{group.title}]({g_link})\nChannel: [{chat.title}]({c_link})"
    await bot.send_message(chat_id=LOG_CHANNEL, text=text)


@Client.on_message(filters.group & filters.command("disconnect"))
async def disconnect(bot, message):
    m=await message.reply("<b>ᴘʟᴇᴀꜱᴇ  ᴡᴀɪᴛ...</b>")   
    try:
       group     = await get_group(message.chat.id)
       user_id   = group["user_id"] 
       user_name = group["user_name"]
       verified  = group["verified"]
       channels  = group["channels"].copy()
    except :
       return await bot.leave_chat(message.chat.id)  
    if message.from_user.id!=user_id:
       return await m.edit(f"Only {user_name} can use this command 😁")
    if bool(verified)==False:
       return await m.edit("ᴛʜɪꜱ ᴄʜᴀᴛ ɪꜱ ɴᴏᴛ ᴠᴇʀɪꜰɪᴇᴅ 🚫\nᴜꜱᴇ /verify")    
    try:
       channel = int(message.command[-1])
       if channel not in channels:
          return await m.edit("ʏᴏᴜ ᴅɪᴅ ɴᴏᴛ ᴀᴅᴅᴇᴅ ᴛʜɪꜱ ᴄʜᴀɴɴᴇʟ ʏᴇᴛ")
       channels.remove(channel)
    except:
       return await m.edit("ɪɴᴄᴏʀʀᴇᴄᴛ ꜰᴏʀᴍᴀᴛ 🚫\nᴜꜱᴇ `/disconnect` ᴄʜᴀɴɴᴇʟ ɪᴅ")
    try:
       chat   = await bot.get_chat(channel)
       group  = await bot.get_chat(message.chat.id)
       c_link = chat.invite_link
       g_link = group.invite_link
       await User.leave_chat(channel)
    except Exception as e:
       text = f"🚫  ᴇʀʀᴏʀ  -  `{str(e)}`\nᴍᴀᴋᴇ ꜱᴜʀᴇ ᴛʜᴀᴛ ɪ ᴀᴍ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴀᴛ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ɢʀᴏᴜᴘ ᴡɪᴛʜ ᴀʟʟ ᴘᴇʀᴍɪꜱꜱɪᴏɴꜱ ᴀɴᴅ {(user.username or user.mention)} ɪꜱ ɴᴏᴛ ʙᴀɴɴᴇᴅ ᴛʜᴇʀᴇ."
       return await m.edit(text)
    await update_group(message.chat.id, {"channels":channels})
    await m.edit(f"ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴅɪꜱᴄᴏɴɴᴇᴄᴛᴇᴅ ꜰʀᴏᴍ [{chat.title}]({c_link})", disable_web_page_preview=True)
    text = f"#DisConnection\n\nUser: {message.from_user.mention}\nGroup: [{group.title}]({g_link})\nChannel: [{chat.title}]({c_link})"
    await bot.send_message(chat_id=LOG_CHANNEL, text=text)


@Client.on_message(filters.group & filters.command("connections"))
async def connections(bot, message):
    group     = await get_group(message.chat.id)    
    user_id   = group["user_id"]
    user_name = group["user_name"]
    channels  = group["channels"]
    f_sub     = group["f_sub"]
    if message.from_user.id!=user_id:
       return await message.reply(f"Only {user_name} can use this command 😁")
    if bool(channels)==False:
       return await message.reply("ᴛʜɪꜱ ɢʀᴏᴜᴘ ɪꜱ ᴄᴜʀʀᴇɴᴛʟʏ ɴᴏᴛ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴛᴏ ᴀɴʏ ᴄʜᴀɴɴᴇʟꜱ..\nᴄᴏɴɴᴇᴄᴛ ᴏɴᴇ ᴜꜱɪɴɢ /connect")
    text = "ᴛʜɪꜱ ɢʀᴏᴜᴘ ɪꜱ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴡɪᴛʜ - \n\n"
    for channel in channels:
        try:
           chat = await bot.get_chat(channel)
           name = chat.title
           link = chat.invite_link
           text += f"[{name}]({link})\n"
        except Exception as e:
           await message.reply(f"🚫  ᴇʀʀᴏʀ  ɪɴ `{channel}:`\n`{e}`")
    if bool(f_sub):
       try:
          f_chat  = await bot.get_chat(channel)
          f_title = f_chat.title
          f_link  = f_chat.invite_link
          text += f"\nFSub: [{f_title}]({f_link})"
       except Exception as e:
          await message.reply(f"❌ ᴇʀʀᴏʀ  ɪɴ  ꜰꜱᴜʙ  (`{f_sub}`)\n`{e}`")
   
    await message.reply(text=text, disable_web_page_preview=True)
