

import sys
import traceback

from requests import get, post

from consts import BOT_URL, UPDATE_URL, SEND_MESSAGE, TEST_MODE, ADMIN_ID, TEST_BOT_URL

# print(BOT_URL)

def send_message(text, chat_id=ADMIN_ID, keyboard=None):

    if not isinstance(text, str):
        text, chat_id = chat_id, text

    if isinstance(chat_id, dict):
        chat_id = chat_id['chat']['id']

    url = SEND_MESSAGE
    params = {
        'chat_id': chat_id,
        "text": text,
    }

    if not keyboard is None:
        params['reply_markup'] = keyboard

    res = send_request(url, params)
    # print(res.text)

def send_contact(phone_number, chat_id="6863016071"):
    url = TEST_BOT_URL + "sendContact"

    params = {
        "chat_id": chat_id, 
        "first_name": "ccontact", 
        "phone_number": "+" + phone_number
    }

    send_request(url, params)

def send_file(chat_id, file_content, file_name=None):

    url = BOT_URL + "sendDocument"

    if isinstance(chat_id, bytes):
        file_content, chat_id = chat_id, file_content

    if isinstance(chat_id, dict):
        chat_id = chat_id['chat']['id']

    params = {
        'chat_id': str(chat_id),
    }
    # print(params)
    if file_name is None:
        file_name = "document"
    file = {'document': (f'{file_name}.pdf', file_content)}

    send_request(url, params, file, as_data_params=True)



def get_updates():
    response = get(UPDATE_URL)

    # send_request(UPDATE_URL, None)


    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to get updates. Status code:", response.status_code)
        print(response.text)


def send_error_message(chat_id=ADMIN_ID):
    exc_type, exc_value, exc_traceback = sys.exc_info()

    # chat_id = consts.BAGS_GROUP

    send_message(str(exc_type), chat_id)
    send_message(str(exc_value), chat_id)

    # Get formatted traceback as a list of strings
    tb_str_list = traceback.format_tb(exc_traceback)

    # Join the list of strings into a single string
    tb_str = '\n'.join(tb_str_list)

    if TEST_MODE:
        print(tb_str)
        print(exc_type)
        print(exc_value)

    send_message(tb_str, chat_id)


def forward_message(message=None, chat_id=None, message_id=None, from_chat_id=None, ):

    if message_id is None:
        message_id = message['message_id']
        from_chat_id = message['chat']['id']

    url = BOT_URL + "forwardMessage"
    params = {
        "chat_id": chat_id,
        "from_chat_id": from_chat_id,
        "message_id": message_id,
    }
    response = send_request(url, params=params)



def set_webhook(server_url=None):
    url = BOT_URL + "setWebhook"
    params = {
        "url": server_url
    }
    send_request(url, params)


def delete_webhook():

    url = BOT_URL + "deleteWebhook"

    response = send_request(url, None)
    print(response)
    print(response.text)

    

def send_request(url, params, files=None, as_data_params=None):

    if (not as_data_params is None) or (not files is None):
        response = post(url, data=params, files=files)
    else:
        response = post(url, json=params, files=files)

    if response.status_code != 200:
        print("Failed to sending: ", url.split("/")[-1])
        print("Status code:", response.status_code)
        print(response.text)
        print(params)
    return response



if __name__ == "__main__" and not TEST_MODE:
    set_webhook(
        "https://ynjraq1b3h.execute-api.ap-northeast-1.amazonaws.com/default/malaka_oshirish_version_2"
    )
    # delete_webhook()


