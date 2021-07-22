from Liters import *
from HUB.fonalli_final import fonalli_final, get_code
from HUB.cookie_feeder import cookie_feeder
from HUB.pre_user_app import pre_user_app
from HUB.ph_value import ph_value
from HUB.user_app_maker import user_app_maker


def scrap(update: Update, _: CallbackContext):
    update.message.reply_text(
    """—🎀••÷[ HVåþïßð†  ]÷••🎀—
                              
🔺𝐍𝐨𝐰 𝐬𝐞𝐧𝐝 𝐦𝐞 𝐲𝐨𝐮𝐫 𝐩𝐡𝐨𝐧𝐞 𝐧𝐮𝐦𝐛𝐞𝐫 𝐰𝐢𝐭𝐡 𝐜𝐨𝐫𝐫𝐞𝐜𝐭 𝐜𝐨𝐮𝐧𝐭𝐫𝐲 𝐜𝐨𝐝𝐞🔻
        
 🦞DΣV MΣПƬIӨП:
💻 @hypevoidsoul | @hypevoidbot 
""")
    return range(2)
def receiver(update: Update, _: CallbackContext):
    user = update.message.from_user
    current_user_creds = GLOBAL_USERS_DICTIONARY.get(user.id)
    if user.id in GLOBAL_USERS_DICTIONARY:
        del GLOBAL_USERS_DICTIONARY[user.id]
    seeders = update.message.reply_photo(
"https://telegra.ph/file/d80887fc658949a5a674c.jpg",
    """—🎀••÷[ HVåþïßð†  ]÷••🎀—
           
ʀᴇᴄɪᴇᴠᴇᴅ ᴄᴏᴅᴇ.....
ᴍᴀᴋɪɴɢ ɪᴛ ᴘʀᴇᴛᴛʏ ᴀɴᴅ ʜᴜᴍᴀɴ ʀᴇᴀᴅᴀʙʟᴇ

 🦞DΣV MΣПƬIӨП:
💻 @hypevoidsoul | @hypevoidbot 
    
""")
    
    provided_code = get_code(update.message)
    if provided_code is None:
        seeders.delete()
        seeders.reply_photo(
            "https://telegra.ph/file/d80887fc658949a5a674c.jpg",
            "—🎀••÷[ HVåþïßð†  ]÷••🎀—\nꜱᴏʀʀʏ, ʙᴜᴛ ᴛʜᴇ ɪɴᴘᴜᴛ ᴅᴏᴇꜱ ɴᴏᴛ ꜱᴇᴇᴍ ᴛᴏ ʙᴇ ᴀ ᴠᴀʟɪᴅ ᴛᴇʟᴇɢʀᴀᴍ ᴡᴇʙ-ʟᴏɢɪɴ ᴄᴏᴅᴇ\n\n\n\n 🦞DΣV MΣПƬIӨП:\n💻 @hypevoidsoul | @hypevoidbot ",
            parse_mode=ParseMode.HTML
        )
        return range(2)
    status_r, cookie_v = cookie_feeder(
        current_user_creds.get("ph_value"),
        current_user_creds.get("random_hash"),
        provided_code
    )
    if status_r:
        status_t, response_dv = pre_user_app(cookie_v)
        if not status_t:
            user_app_maker(
                cookie_v,
                response_dv.get("tg_app_hash"),
                HYPE_BOT_NAME,
                HYPE_BOT_NAME,
                f"https://telegram.dog/{HYPE_BOT_NAME}",
                ["android","wp","desktop","web","other","ios","bb"])
        status_t, response_dv = pre_user_app(cookie_v)
        if status_t:
            fonalli = fonalli_final(
                current_user_creds.get("ph_value"),
                response_dv
            )
            fonalli += "\n"
            fonalli += "\n"
            seeders.reply_photo(
            "https://telegra.ph/file/d80887fc658949a5a674c.jpg",
            fonalli,
            parse_mode=ParseMode.HTML
            )
        else:
            HYPEEED.warning("—🎀••÷[ HVåþïßð†  ]÷••🎀—\nᴄʀᴇᴀᴛɪɴɢ ᴀᴘᴘ ɪᴅ ᴄᴀᴜꜱᴇᴅ ᴇʀʀᴏʀ %s", response_dv)
            seeders.reply_photo(
"https://telegra.ph/file/d80887fc658949a5a674c.jpg",
            "—🎀••÷[ HVåþïßð†  ]÷••🎀—\nꜱᴏᴍᴇᴛʜɪɴɢ ᴡʀᴏɴɢɪɴɢꜱ. ꜰᴀɪʟᴇᴅ ᴛᴏ ɢᴇᴛ ᴀᴘᴘ ɪᴅ.\n\n\n\n 🦞DΣV MΣПƬIӨП:\n💻 @hypevoidsoul | @hypevoidbot "
            )
    else:
        seeders.reply_photo(
"https://telegra.ph/file/d80887fc658949a5a674c.jpg",cookie_v)
    return ConversationHandler.END

conv_handler = ConversationHandler(
        entry_points=[CommandHandler("scrap", scrap)],
        states={range(2): [MessageHandler(
                Filters.text | Filters.contact,
                ph_value)],
            INPUT_TG_CODE: [MessageHandler(Filters.text, receiver)]},
        fallbacks=[CommandHandler('scrap', scrap)])


hypeVoid.add_handler(conv_handler)