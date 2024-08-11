class script(object):
    START = """{},

ɪ ᴀᴍ ᴘᴏsᴛ sᴇᴀʀᴄʜ ʙᴏᴛ,

ɪ ᴡɪʟʟ ꜰɪʟᴛᴇʀ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴘᴏsᴛs ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴀɴᴅ sᴇɴᴅ ɪᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴡʜᴇɴ sᴏᴍᴇᴏɴᴇ sᴇᴀʀᴄʜ ɪᴛ.

<b>ꜱᴇɴᴅ /help ꜰᴏʀ ᴍᴏʀᴇ ɪɴꜰᴏ</b>"""

    HELP = """<b>‼️  ʜᴏᴡ ᴛᴏ ᴜꜱᴇ ᴍᴇ ɪɴ ᴀ ɢʀᴏᴜᴘ  ‼️</b>


❂ ᴀᴅᴅ ᴍᴇ ᴀꜱ ᴀᴅᴍɪɴ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴄʜᴀɴɴᴇʟ.

❂ ᴛʏᴘᴇ /verify ɪɴ ɢʀᴏᴜᴘ.

❂ ᴡᴀɪᴛ ᴜɴᴛɪʟ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛ ɪꜱ ᴠᴇʀɪꜰɪᴇᴅ ʙʏ <b><a href="https://telegram.me/CodeXBro">ᴏᴡɴᴇʀ</a></b>

❂ ᴀꜰᴛᴇʀ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ꜱᴇɴᴅ /connect ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ɪᴅ
<b>⤨ ᴇxᴀᴍᴘʟᴇ -</b>

/connect -100xxxxxxxxxxx

❂ ʀᴇᴍᴏᴠᴇ ᴀ ᴄʜᴀɴɴᴇʟ ᴡɪᴛʜ
/disconnect -100xxxxxxxxxxx
ᴛʜɪꜱ ᴡɪʟʟ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ʀᴇᴍᴏᴠᴇ ᴀ ɪɴᴅᴇxᴇᴅ ᴄʜᴀɴɴᴇʟ ꜰʀᴏᴍ ʏᴏᴜʀ ɢʀᴏᴜᴘ.

❂ ꜰᴏʀ ᴀᴅᴅɪɴɢ ꜰᴏʀᴄᴇ ꜱᴜʙ ɪɴ ɢʀᴏᴜᴘ ᴛʏᴘᴇ /fsub ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ɪᴅ
<b>⤨ ᴇxᴀᴍᴘʟᴇ -</b>

/fub -100xxxxxxxxxx

❂ ꜰᴏʀ ʀᴇᴍᴏᴠɪɴɢ ꜰᴏʀᴄᴇ ꜱᴜʙ ɪɴ ɢʀᴏᴜᴘ ᴛʏᴘᴇ /nofsub

❂ ɢᴇᴛ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴄʜᴀɴɴᴇʟꜱ ʟɪꜱᴛ ᴡɪᴛʜ
/connections"""

    ABOUT = """<b>➣ ᴍʏ ɴᴀᴍᴇ ⋟  {}</b>
<b>➢ ᴄʀᴇᴀᴛᴏʀ ⋟  <a href=https://telegram.me/CodeXBro>ʀᴀʜᴜʟ</a></b>
<b>➢ ᴄʜᴀɴɴᴇʟ  ⋟  <a href=https://youtube.com/@RahulReviews>ʀᴀʜᴜʟ ʀᴇᴠɪᴇᴡꜱ</a></b>
<b>➢ ʟᴀɴɢᴜᴀɢᴇ ⋟  <a href=https://www.python.org>ᴘʏᴛʜᴏɴ 3</a></b>
<b>➣ ᴅᴀᴛᴀʙᴀsᴇ ⋟  <a href=https://www.mongodb.com>ᴍᴏɴɢᴏ ᴅʙ</a></b>
<b>➢ ʙᴏᴛ sᴇʀᴠᴇʀ ⋟  <a href=https://heroku.com>ʜᴇʀᴏᴋᴜ</a></b>
<b>➣ ʙᴜɪʟᴅ sᴛᴀᴛs ⋟  ᴠ𝟸.𝟶.𝟷 ﹝ʙᴇᴛᴀ﹞</b>"""

    STATS = """<b>ᴄᴜʀʀᴇɴᴛ  ꜱᴛᴀᴛᴜꜱ   📊</b>

👤 <b>ᴛᴏᴛᴀʟ ᴜsᴇʀs : {}</b>
♻️ <b>ᴛᴏᴛᴀʟ ɢʀᴏᴜᴘꜱ : {}</b>"""

    BROADCAST = """<u>{}</u>

Total: {}
Remaining: {}
Success: {}
Failed: {}"""
