from info import *
from utils import *
from pyrogram import Client, filters 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 

@Client.on_message(filters.command("start") & ~filters.channel)
async def start(bot, message):
    await add_user(message.from_user.id, message.from_user.first_name)
    await message.reply(text=script.START.format(message.from_user.mention),
                        disable_web_page_preview=True,
                        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('⇄  ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ  ⇄', url=f'http://telegram.me/Link_Search_Robot?startgroup=true')
            ],[InlineKeyboardButton("ʜᴇʟᴘ", url="http://telegram.me/BotszSupport"),

InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="misc_help")],[InlineKeyboardButton('❂   ᴏᴜʀ  ᴜᴘᴅᴀᴛᴇꜱ  ᴄʜᴀɴɴᴇʟ   ❂', url=f'http://telegram.me/BotszList')]]))  
@Client.on_message(filters.command("help"))
async def help(bot, message):
    await message.reply(text=script.HELP,
                        disable_web_page_preview=True)

@Client.on_message(filters.command("about"))
async def about(bot, message):
    await message.reply(text=script.ABOUT.format((await bot.get_me()).mention),
                        disable_web_page_preview=True)

@Client.on_message(filters.command("stats") & filters.user(ADMIN))
async def stats(bot, message):
    g_count, g_list = await get_groups()
    u_count, u_list = await get_users()
    await message.reply(script.STATS.format(u_count, g_count))

@Client.on_message(filters.command("id"))
async def id(bot, message):
    text = f"<b>➲  ᴄʜᴀᴛ ɪᴅ:-</b>  `{message.chat.id}`\n"
    if message.from_user:
       text += f"<b>➲  ʏᴏᴜʀ ɪᴅ:-</b> `{message.from_user.id}`\n"
    if message.reply_to_message:
       if message.reply_to_message.from_user:
          text += f"<b>➲  ʀᴇᴘʟɪᴇᴅ ᴜꜱᴇʀ ɪᴅ:-</b> `{message.reply_to_message.from_user.id}`\n"
       if message.reply_to_message.forward_from:
          text += f"<b>➲  ʀᴇᴘʟɪᴇᴅ ᴍᴇꜱꜱᴀɢᴇ ꜰᴏʀᴡᴀʀᴅ ꜰʀᴏᴍ ᴜꜱᴇʀ ɪᴅ:-</b> `{message.reply_to_message.forward_from.id}`\n"
       if message.reply_to_message.forward_from_chat:
          text += f"<b>➲  ʀᴇᴘʟɪᴇᴅ ᴍᴇꜱꜱᴀɢᴇ ꜰᴏʀᴡᴀʀᴅ ꜰʀᴏᴍ ᴄʜᴀᴛ ɪᴅ:-</b> `{message.reply_to_message.forward_from_chat.id}\n`"
    await message.reply(text)

@Client.on_callback_query(filters.regex(r"^misc"))
async def misc(bot, update):
    data = update.data.split("_")[-1]
    if data=="home":
       await update.message.edit(text=script.START.format(update.from_user.mention),
                                 disable_web_page_preview=True,
                                 reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('⇄  ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ  ⇄', url=f'http://telegram.me/Link_Search_Robot?startgroup=true')
            ],[InlineKeyboardButton("ʜᴇʟᴘ", url="http://telegram.me/BotszSupport"),

InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="misc_help")],[InlineKeyboardButton('❂   ᴏᴜʀ  ᴜᴘᴅᴀᴛᴇꜱ  ᴄʜᴀɴɴᴇʟ   ❂', url=f'http://telegram.me/BotszList')]])) 
    elif data=="help":
       await update.message.edit(text=script.HELP, 
                                 disable_web_page_preview=True,
                                 reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('🧑‍💻   ᴄᴏɴᴛᴀᴄᴛ  ᴛᴏ  ᴏᴡɴᴇʀ   🧑‍💻',url='https://telegram.me/NobiDeveloperr')],[InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="misc_home"),InlineKeyboardButton("ɴᴇxᴛ", url="https://telegra.ph/SUPPORT-12-22-2")]])) 


    elif data=="about":
        await update.message.edit(text=script.ABOUT.format((await bot.get_me()).mention), 
                                  disable_web_page_preview=True,
                                  reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="misc_home")]]))
         
@Client.on_message(filters.command("follow"))
async def follow_msg(bot, message):
    btn = [[
        InlineKeyboardButton(text="ᴛᴡɪᴛᴛᴇʀ", url="https://twitter.com/NobiDeveloper"),
        InlineKeyboardButton(text="ɪɴꜱᴛᴀɢʀᴀᴍ", url="https://instagram.com/NobiDeveloper")
        ],[
        InlineKeyboardButton(text="ɢɪᴛʜᴜʙ  ᴀᴄᴄᴏᴜɴᴛ", url="https://github.com/NobiDeveloper")
    ],[
        InlineKeyboardButton(text="ᴏᴜʀ  ᴏꜰꜰɪᴄɪᴀʟ  ᴡᴇʙꜱɪᴛᴇ", url="https://nobideveloper.blogspot.com")
    ],[
        InlineKeyboardButton(text="ꜱᴜʙꜱᴄʀɪʙᴇ  ᴏᴜʀ  ʏᴛ  ᴄʜᴀɴɴᴇʟ", url="https://youtube.com/@NobiDeveloper")
    ],[
        InlineKeyboardButton(text="ʀᴇᴠɩᴇᴡꜱ", url="https://telegram.me/ReviewsGallary"),
        InlineKeyboardButton(text="ᴜᴘᴅᴀᴛᴇꜱ", url="https://telegram.me/NobiDeveloper")
    ]]
    yt = await message.reply_photo(photo='https://telegra.ph/file/b681d379605d3d3a9fa1c.jpg', caption="<b>ᴏᴜʀ  ꜱᴏᴄɪᴀʟ  ᴍᴇᴅɪᴀ  ᴘʟᴀᴛꜰᴏʀᴍꜱ</b>", reply_markup=InlineKeyboardMarkup(btn))
    await asyncio.sleep(500)
    await yt.delete()
    await message.delete()

@Client.on_message(filters.private & filters.text & filters.incoming)
async def pm_text(bot, message):
    content = message.text
    user = message.from_user.first_name
    user_id = message.from_user.id
    if content.startswith("/") or content.startswith("#"): return  # ignore commands and hashtags
    await message.reply_text(
         text="<b>ʜʏ,\n\nɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴍᴏᴠɪᴇs / sᴇʀɪᴇs ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ꜰɪʀsᴛ ʙᴜᴛᴛᴏɴ ᴏʀ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ɪɴ ʙᴏᴛ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ sᴇᴄᴏɴᴅ ʙᴜᴛᴛᴏɴ</b>",   
         reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("📝  ʀᴇǫᴜᴇsᴛ ʜᴇʀᴇ​ ", url=f"https://telegram.me/AllRequestGroups")],[InlineKeyboardButton("🧑‍💻  ʙᴏᴛ ᴏᴡɴᴇʀ ", url=f"https://telegram.me/Nobideveloperr")]]), disable_web_page_preview=True
    )
    await bot.send_message(
        chat_id=LOG_CHANNEL,
        text=f"<b>#𝐌𝐒𝐆\n\nNᴀᴍᴇ : {user}\n\nID : {user_id}\n\nMᴇssᴀɢᴇ : {content}</b>"
    )
