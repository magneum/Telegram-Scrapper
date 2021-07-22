from Liters import *


def fonalli_final(input_phone_number, in_dict):
    """ convert the dictionary returned in STEP FOUR
    into Telegram HTML text """
    fonalli = ""
    fonalli += "<i>Phone Number</i>: "
    fonalli += f"<u>{input_phone_number}</u>"
    fonalli += "\n"
    fonalli += "\n"
    fonalli += "<i>App Configuration</i>"
    fonalli += "\n"
    fonalli += "<b>APP ID</b>: "
    fonalli += "<code>{}</code>".format(in_dict["App Configuration"]["app_id"])
    fonalli += "\n"
    fonalli += "<b>API HASH</b>: "
    fonalli += "<code>{}</code>".format(in_dict["App Configuration"]["api_hash"])
    return fonalli


def get_code(ptb_message):
    """ extracts the input message, and returns the
    Telegram Web login code"""
    telegram__web_login_code = None
    incoming_message_text = ptb_message.text
    incoming_message_text_in_lower_case = incoming_message_text.lower()
    if "web login code" in incoming_message_text_in_lower_case:
        parted_message_pts = incoming_message_text.split("\n")
        if len(parted_message_pts) >= 2:
            telegram__web_login_code = parted_message_pts[1]
    elif "\n" in incoming_message_text_in_lower_case:
        HYPEEED.info("did it come inside this 'elif' ?")
    else:
        telegram__web_login_code = incoming_message_text
    return telegram__web_login_code


def foreign_num(ptb_message):
    """ gets the phone number (in international format),
    from the input message"""
    HYPEEED.info(ptb_message)
    my_telegram_ph_no = None
    if ptb_message.text is not None:
        if len(ptb_message.entities) > 0:
            for c_entity in ptb_message.entities:
                if c_entity.type == "phone_number":
                    my_telegram_ph_no = ptb_message.text[
                        c_entity.offset:c_entity.length
                    ]
        else:
            my_telegram_ph_no = ptb_message.text
    elif ptb_message.contact is not None:
        # https://archive.is/X4gsK
        if ptb_message.contact.phone_number != "":
            my_telegram_ph_no = ptb_message.contact.phone_number
    return my_telegram_ph_no



