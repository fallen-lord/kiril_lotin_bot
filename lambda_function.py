import json

from requests import post

import consts
from kiril_lotin import translate


ADMIN = consts.ADMIN_ID

def add_id(user_id=None, show_ids=False):
    import sqlite3
    try:
        db = sqlite3.connect("kiril_lotin.db")
        cursor = db.cursor()
        cursor.execute("SELECT user_id FROM user")
        users_id = cursor.fetchall()
        if not show_ids:
            if not (user_id, ) in users_id:
                cursor.execute(f"""
                  INSERT INTO user VALUES(
                      {user_id}
                  )
                  """)
                db.commit()
                # print(f"{user_id} mb ga qo'shildi!!!")

    except Exception as e:
        print(e)

    finally:
        cursor.close()
        db.close()
    if show_ids:
        return len(users_id)


def send_message(chat_id, text):
    """Chatga habar jo'natuvchi funksiya"""

    url = consts.SEND_MESSAGE
    post(url,
        data={'chat_id':chat_id, 'text':text})

def lambda_handler(event=None, context=None):
    message = json.loads(event['body']).get('message')
    response = {
        'statusCode': 200
        "body": "Hello from Lambda!"
    }

    if message is None:
        return response
    text = message.get('text')
    user_id = message['chat']['id']
    if text is None:
        return response
    
    if text == "/start":
        add_id(user_id)
        send_message(user_id, """
Menga habar jo'natishingizdan oldin eslatib o'tmoqchiman:
Agar matningiz kiril yozuvida bo'lsa lotin, 
lotin yozuvida bo'lsa kiril yozuviga o'tkazib beraman!!!""")
        send_message(ADMIN, "Bot foydalanuvchilar soni 1 taga oshdi!")
    elif text == "/admin" and user_id == ADMIN:
        text = f"Bot foydalanuvhilari soni: {add_id(show_ids=True)}"
        send_message(ADMIN, text)
    else:
        for i in translate(text):
            send_message(user_id, i)

    return response
