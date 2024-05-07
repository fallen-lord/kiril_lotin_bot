
import json

import consts
from tgbot import send_message
import tgbot


def get_message(event,):
    if event is not None:
        body = event['body']
        if isinstance(body, str):
            body = json.loads(body)
        last_message = body
    else:
        res = tgbot.get_updates()
        # print(utils.dict_to_pretty_str(res["result"]))
        last_message = res["result"][-1]
    if not last_message:
        return
    last_message = (
        last_message.get("message")
        or last_message.get("callback_query")
        or last_message.get("edited_message")
        or last_message.get("edited_callback_query")
        )
    return last_message


def greeting(message, user):
    text = "Onlinedu.zu botiga xush kelibsiz!"
    send_message(message, text)
    text = """Bu bot orqali Siz O'qituchilarni:
    Taxrirlashingiz,
    Ro'yhatdan o'kazishingiz,
    Parollarini tiklashingiz
    va ENG ASOSIYSI
    ularga SERTIFIKAT olib
    berishingiz mumkin!
    Buning uchun shunchaki
    """
    send_message(text, message)
    send_example(message)
    text = "Ro'yhatdanO'tsh, ParolTiklash haqida batafsil ma'lumot olish uchun /help ni bosing"
    send_message(message, text)

    if len(user['updated']) > 1:
        return

    user_message = message['chat']
    user['first_name'] = user_message['first_name']
    if user_message.get("last_name"):
        user['last_name'] = user_message["last_name"]
    if user_message.get("username"):
        user['user_name'] = user_message["username"]

    now = utils.get_time_at_uzb_timezone()
    now = now.strftime(consts.FORMAT_TIME)
    user['updated'].append(
        ['clicked_start', now]
    )

    # print(user)
    models.save_user(user)


def send_example(message):

    send_message("Birinchi satrda telefon raqam\nIkkinchi satrda esa parolni jo'nating!", message)
    send_message(message, "999999999\n12345678")
    send_message(message, "Yuqoridagi namuna singari bo'lsin!")


def help_hendler(message):
    send_message("Agar botda xatolik uchragan bo'lsa adminga murojat qiling:\n https://t.me/onlinedu_admin_bot",
                 message)

def send_empty_pocket(message):
    send_message(
                    message,
                    ("Ushbu buyruqni amalga oshirish uchun hisobingizda yetarli mablag' mavjud emas!\n "
                     + "Balansingiz haqidagi malumotni olish uchun /profile ni bosing."))


def send_profile_data(message, user):
    text_message = ""
    text_message += f"Ism: {user['first_name']}\n"
    user_status_name = utils.user_status_name(user)
    text_message += f"Status: {user_status_name}\n"

    text_message += f"Balansingiz: {user['balance']} ming so'm\n"
    text_message += "\nHozirda Sizga belgilangan narxlar!\n\n"
    text_message += f"Bitta Sertifikat narxi: {user['price_single_certificate']} ming so'm.\n\n"
    text_message += f"Bitta Taxrirlash, ParolTiklash yoki Ro'yhatdanO'tsh narxi: {user['price_reset_password']} ming so'm.\n\n"
    text_message += "Narxlarni o'zgartirmoqchi yoki ular haqida batafsil ma'lumot olish uchun /prices ni bosing."

    send_message(message, text_message)


def send_prices_data(message, user):
    text_message = """
Sertifikat narxlari siz qilgan to'lov miqdoriga qarab belgilanadi.
Agar siz qilgan to'lov:

    100 ming so'mdan kamroq bo'lsa 1 ta sertifikat narhi 60 ming so'mga teng bo'ladi
    
    200 ming so'mdan kamroq bo'lsa 1 ta sertifikat narhi 50 ming so'mga teng bo'ladi

    200 ming so'mga teng bo'lsa 1 ta sertifikat narhi 40 ming so'mga teng bo'ladi 

    300 ming so'mga teng bo'lsa 1 ta sertifikat narhi 30 ming so'mga teng bo'ladi 

Misol uchun agar 70 ming so'm to'lov qilinsa 1 ta sertifikatga botdagi hisobingizdan 60 ming so'm yechib olinadi!

Agar 110 ming so'm to'lov qilsangiz 1 ta sertifikatga botdagi hisobingizdan 50 ming so'm yechib olinadi!

1 ta Taxrirlash, Ro'yhatdanO'tish yoki ParolTiklash narhi 10 ming so'm
"""
    send_message(text_message, message)
