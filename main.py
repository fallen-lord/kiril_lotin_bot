
if __name__ == '__main__':
    from dotenv import load_dotenv
    load_dotenv()

import consts
from requests.exceptions import ConnectionError
import json
import base_lambda
from base_lambda import get_message
from tgbot import send_message, send_error_message
import tgbot
from kiril_lotin import translate


def main(event=None, context=None):

    try:

        message = get_message(event)
        if message.get("message_id") is None:
            return

        text = message.get("text")
        if text is None:
            return

        user_id = message['chat']['id']
        for i in translate(text):
            send_message(user_id, i)

        # message = get_message(event)

        # if message is None:
        #     message_id = callback_query['id']
        #     user_id = callback_query['from']['id']
        # else:
        #     message_id = str(message['message_id'])
        #     # user_id = str(message['chat']['id'])
        # user = models.get_user(message or user_id)

        # if (user is None 
        #     or ((message_id == user['last_message_id']) and (__name__ != "__main__"))
        #     or (user['accept_message_status'] != "True")):
        #     return
        
        # user['last_message_id'] = message_id
        # models.save_user(user)
        # print(message, "1111111111")


    except ConnectionError:
        send_message("Sayt bilan bog'lanishda xatolik.\nQayta urinib ko'ring!", message['chat']['id'])

    except Exception as e:

        send_message("Nimadur xato ketdi.\nAdminlarimiz bu bilan shug'illanishmoqda.\nBirozdan so'ng qayta urinib ko'ring!",
         message['chat']['id'])
        send_message(str(e), chat_id=consts.BAGS_GROUP)
        send_error_message(consts.BAGS_GROUP)

        if __name__ != "__main__" and type(event['body']) != dict:
            message = json.loads(event['body'])
        send_message(json.dumps(message, indent=2))


def lambda_handler(event=None, context=None):

    main(event, context)

    return {
        'statusCode': 200,
        'body': "Hello from Lambda!"
    }


if __name__ == "__main__":

    lambda_handler()
    # print(len("UC5gXL8j"))
