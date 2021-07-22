from Liters import *
from HUB.fonalli_final import fonalli_final, get_code
from HUB.cookie_feeder import cookie_feeder
from HUB.pre_user_app import pre_user_app
from HUB.ph_value import ph_value
from HUB.user_app_maker import user_app_maker


def start(update: Update, _: CallbackContext):
    update.message.reply_text(
    """Hi!
/start at any stage to re-enter your details""",
    parse_mode=ParseMode.HTML
    )
    return range(2)

def receiver(update: Update, _: CallbackContext):
    user = update.message.from_user
    current_user_creds = GLOBAL_USERS_DICTIONARY.get(user.id)
    if user.id in GLOBAL_USERS_DICTIONARY:
        del GLOBAL_USERS_DICTIONARY[user.id]
    aes_mesg_i = update.message.reply_text(
    "recieved code. Scarpping web page ...")
    
    provided_code = get_code(update.message)
    if provided_code is None:
        aes_mesg_i.edit_text(
            text="sorry, but the input does not seem to be a valid Telegram Web-Login code",
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
                [
                "android",
                "ios",
                "wp",
                "bb",
                "desktop",
                "web",
                "ubp",
                "other"
                ])
        status_t, response_dv = pre_user_app(cookie_v)
        if status_t:
            fonalli = fonalli_final(
                current_user_creds.get("ph_value"),
                response_dv
            )
            fonalli += "\n"
            fonalli += "\n"
            aes_mesg_i.edit_text(
                text=fonalli,
                parse_mode=ParseMode.HTML
            )
        else:
            HYPEEED.warning("creating APP ID caused error %s", response_dv)
            aes_mesg_i.edit_text(
            "something wrongings. failed to get app id."
            )
    else:
        aes_mesg_i.edit_text(cookie_v)
    return ConversationHandler.END

conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={range(2): [MessageHandler(
                Filters.text | Filters.contact,
                ph_value)],
            INPUT_TG_CODE: [MessageHandler(Filters.text, receiver)]},
        fallbacks=[CommandHandler('start', start)])

hypeVoid.add_handler(conv_handler)