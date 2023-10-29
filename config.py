import os
from os import getenv
from dotenv import load_dotenv
from distutils.util import strtobool


load_dotenv(".env")


API_ID = int(getenv("API_ID", "20913173")) #optional
API_HASH = getenv("API_HASH", "93a1f0cd49026ce5943da64ca7a932d1") #optional
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
DEEP_AI = getenv("DEEP_AI", "d7394561-0528-4714-a1ee-edd7020b48e1")
OWNER_ID = int(getenv("OWNER_ID", "6377369444, 1672843007") or 0)
ADMIN1_ID = list(map(int, getenv("ADMIN1_ID", "1054295664").split()))
ADMIN2_ID = list(map(int, getenv("ADMIN2_ID", "1755047203").split()))
ADMIN3_ID = list(map(int, getenv("ADMIN2_ID", "6377369444").split()))
ADMIN4_ID = list(map(int, getenv("ADMIN2_ID", "1672843007").split()))
ADMIN5_ID = list(map(int, getenv("ADMIN1_ID", "1450470255").split()))


ADMIN1_ID.append(1054295664)
ADMIN2_ID.append(1755047203)
ADMIN3_ID.append(6377369444)
ADMIN4_ID.append(1672843007)
ADMIN5_ID.append(1450470255)

MONGO_URL = getenv("MONGO_URL", "mongodb+srv://Alexa:alexa@cluster0.h0zqfue.mongodb.net/true?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN""6942598619:AAHcO3kp3i05ff7d_lZscNW1_lZtcU8_I4A")
BOT_WORKERS = int(getenv("BOT_WORKERS", "2"))
USER_WORKERS = int(getenv("BOT_WORKERS", "8"))
PM_AUTO_BAN = strtobool(getenv("PM_AUTO_BAN", "True"))
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER", None)
OPENAI_API = getenv("OPENAI_API", "")
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID") or 0)
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "").split()}
GIT_TOKEN = getenv("GIT_TOKEN", "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") #personal access token
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
BRANCH = getenv("BRANCH", "amang") #don't change
REPO_URL = getenv("REPO_URL", "https://github.com/Djangonew/DjangoUbot")
CMD_HNDLR = getenv("CMD_HNDLR", ".")
SUPPORT = int(getenv("SUPPORT", "-1001857062751"))
CHANNEL = int(getenv("CHANNEL", "-1001869711042"))
SESSION1 = getenv("SESSION1", "BQE_HBUAOar-D_qa3Ct-mRcJmddy5Vzz6JNazsRdmdlIDAnBzZ5lvkaFmGz_8Vj8HlghD1Or1WIcFrDNr6Wm0aE3udimzOCsEBUod3Z1rrqjWHfj1nKbAXUj8cW5dZYskPPUjObz0FHqzNCkpUBv0qxPjmy5sbeNtONWO5xa-zg5amYueg9k0sAkS1EiA_HolHm2a6q94XY1F0e18WLKHKWINECCEw8R_IWxc84BpjrIaBQOXc2TUSBGenzey1JXCpu7rUz97n5K19Mpn59TGyHoBUT24pUhUWGGUxVMS1w7VP0TWRPXvumiwEPq_f7WnwLwwtHvO-lJWmoadEeG6LWRgmeC1wAAAAF8Hu9kAA")
SESSION2 = getenv("SESSION2", "")
SESSION3 = getenv("SESSION3", "")
SESSION4 = getenv("SESSION4", "")
SESSION5 = getenv("SESSION5", "")
SESSION6 = getenv("SESSION6", "")
SESSION7 = getenv("SESSION7", "")
SESSION8 = getenv("SESSION8", "")
SESSION9 = getenv("SESSION9", "")
SESSION10 = getenv("SESSION10", "")
SESSION11 = getenv("SESSION11", "")
SESSION12 = getenv("SESSION12", "")
SESSION13 = getenv("SESSION13", "")
SESSION14 = getenv("SESSION14", "")
SESSION15 = getenv("SESSION15", "")
SESSION16 = getenv("SESSION16", "")
SESSION17 = getenv("SESSION17", "")
SESSION18 = getenv("SESSION18", "")
SESSION19 = getenv("SESSION19", "")
SESSION20 = getenv("SESSION20", "")
SESSION21 = getenv("SESSION21", "")
SESSION22 = getenv("SESSION22", "")
SESSION23 = getenv("SESSION23", "")
SESSION24 = getenv("SESSION24", "")
SESSION25 = getenv("SESSION25", "")
SESSION26 = getenv("SESSION26", "")
SESSION27 = getenv("SESSION27", "")
SESSION28 = getenv("SESSION28", "")
SESSION29 = getenv("SESSION29", "")
SESSION30 = getenv("SESSION30", "")
SESSION31 = getenv("SESSION31", "")
SESSION32 = getenv("SESSION32", "")
SESSION33 = getenv("SESSION33", "")
SESSION34 = getenv("SESSION34", "")
SESSION35 = getenv("SESSION35", "")