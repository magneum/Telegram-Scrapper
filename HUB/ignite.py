from Liters import *

def start(update: Update, context: CallbackContext):
    args = context.args
    if update.effective_chat.type == "private":
        update.message.reply_photo(
"https://telegra.ph/file/d80887fc658949a5a674c.jpg",
"""—🎀••÷[ HVåþïßð†  ]÷••🎀—

    💻 𝗪𝗵𝗮𝘁 𝗖𝗮𝗻 𝗕𝗼𝘁 𝗗𝗼???
⚔️𝘛𝘦𝘭𝘦𝘨𝘳𝘢𝘮 𝘣𝘰𝘵 𝘵𝘰 𝘤𝘳𝘦𝘢𝘵𝘦 𝘶𝘴𝘦𝘳 𝘈𝘗𝘗 𝘢𝘯𝘥 𝘴𝘦𝘯𝘥 𝘵𝘩𝘦𝘪𝘳 𝘈𝘗𝘐_𝘐𝘋 𝘢𝘯𝘥 𝘈𝘗𝘐_𝘏𝘈𝘚𝘏 


/scrap ᴀᴛ ᴀɴʏ ꜱᴛᴀɢᴇ ᴛᴏ ʀᴇ-ᴇɴᴛᴇʀ ʏᴏᴜʀ ᴅᴇᴛᴀɪʟꜱ

 🦞DΣV MΣПƬIӨП:\n💻 @hypevoidsoul | @hypevoidbot  
""",
    parse_mode=ParseMode.HTML
    )
start_handler = CommandHandler("start", start, run_async=True)
hypeVoid.add_handler(start_handler)