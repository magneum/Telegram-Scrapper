from Liters import *
from HUB.fonalli_final import foreign_num
from HUB.req_login import req_login

def ph_value(update: Update, _: CallbackContext):
    user = update.message.from_user
    input_text = foreign_num(update.message)
    if input_text is None:
        update.message.reply_text(
            text="sorry, but the input does not seem to be a valid phone number",
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
    """I see!
now please send the Telegram code that you received from Telegram!

/start at any stage to re-enter your details""",
        parse_mode=ParseMode.HTML
    )
    return INPUT_TG_CODE