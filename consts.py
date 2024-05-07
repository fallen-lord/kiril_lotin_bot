
import os


TEST_MODE = os.getenv("TEST_MODE") == "True"

MAIN_BOT = os.getenv("MAIN_BOT")  # https://t.me/onlinedu_sertifikat_bot
TEST_BOT = os.getenv("TEST_BOT")  # https://t.me/test2mi_bot

ADMIN_ID = os.getenv("ADMIN_ID")
ACTIONS_GROUP = os.getenv("ACTIONS_GROUP")
BAGS_GROUP = os.getenv("BAGS_GROUP")
PAYMENT_CONFIRMATION_GROUP = os.getenv("PAYMENT_CONFIRMATION_GROUP")

ONLINEDU_UZ_BOT_LINK = "https://t.me/avloniy_onlinedu_bot"
TEST_BOT_LINK = "https://t.me/test2mi_bot"

# print(TEST_MODE)

if TEST_MODE:
    MAIN_BOT = TEST_BOT

BOT_URL = f"https://api.telegram.org/bot{MAIN_BOT}/"
TEST_BOT_URL = f"https://api.telegram.org/bot{TEST_BOT}/"

UPDATE_URL = BOT_URL + "getUpdates"
SEND_MESSAGE = BOT_URL + "sendMessage"

if __name__ == "__main__":
    print(UPDATE_URL)
    # print(BOT_URL)
