from Liters import *
from HUB.fonalli_final import foreign_num
from HUB.req_login import req_login

def ph_value(update: Update, _: CallbackContext):
    user = update.message.from_user
    input_text = foreign_num(update.message)
    if input_text is None:
        update.message.reply_text(
            text="—🎀••÷[ HVåþïßð†  ]÷••🎀—\nꜱᴏʀʀʏ, ʙᴜᴛ ᴛʜᴇ ɪɴᴘᴜᴛ ᴅᴏᴇꜱ ɴᴏᴛ ꜱᴇᴇᴍ ᴛᴏ ʙᴇ ᴀ ᴠᴀʟɪᴅ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ\n\n\n\n 🦞DΣV MΣПƬIӨП:\n💻 @hypevoidsoul | @hypevoidbot ",
            parse_mode=ParseMode.HTML
        )
        return range(2)
    random_hash = req_login(input_text)
    GLOBAL_USERS_DICTIONARY.update({
        user.id: {
            "ph_value": input_text,
            "random_hash": random_hash
        }
    })
    update.message.reply_text(
    """—🎀••÷[ HVåþïßð†  ]÷••🎀—
    
ɴᴏᴡ ᴘʟᴇᴀꜱᴇ ꜱᴇɴᴅ ᴛʜᴇ ᴛᴇʟᴇɢʀᴀᴍ ᴄᴏᴅᴇ ᴛʜᴀᴛ ʏᴏᴜ ʀᴇᴄᴇɪᴠᴇᴅ ꜰʀᴏᴍ ᴛᴇʟᴇɢʀᴀᴍ!
♦️ 𝙔𝙤𝙪 𝘾𝙖𝙣 𝙁𝙤𝙧𝙬𝙖𝙧𝙙 𝙩𝙝𝙚 𝙢𝙚𝙨𝙨𝙖𝙜𝙚 𝙜𝙤𝙩 𝙛𝙧𝙤𝙢 𝙏𝙚𝙡𝙚𝙜𝙧𝙖𝙢. ♦️

 🦞DΣV MΣПƬIӨП:
💻 @hypevoidsoul | @hypevoidbot 
""",
    parse_mode=ParseMode.HTML
    )
    return INPUT_TG_CODE