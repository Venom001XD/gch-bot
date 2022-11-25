"""
MIT License

Copyright (c) 2022 Arsh

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open('{}/Himawari/{}'.format(os.getcwd(), config),
              'r') as json_file:
        return json.load(json_file)[key]

class Config(object):

    ##dont change
    LOGGER=True
    ALLOW_CHATS=True
    ALLOW_EXCL=False
    TEMP_DOWNLOAD_DIRECTORY="./"
    DEL_CMDS=False
    BAN_STICKER="kans" 
    CERT_PATH=""
    PORT=8443
    WORKERS=8
    LOAD=""
    NO_LOAD="translation"
    MONGO_DB="Himawari"
    WEBHOOK=False
    BOT_API_URL="https://api.telegram.org/bot"

    #you can change these 
    INFOPIC=True #picture while doing /info
    STRICT_GBAN=True
    API_ID=24762688 ##api id from my.telegram.org
    APP_ID=24762688 #same as API_ID
    API_HASH="0940dc2e4b6c7fe162850723b662df82" ##api hash from my.telegram.org
    APP_HASH="0940dc2e4b6c7fe162850723b662df82" #same as API_HASH
    BL_CHATS=[1] #chats to be blacklisted
    MONGO_DB_URL = "mongodb+srv://ssid143:liyaxlambert*143@cluster0.pdabrye.mongodb.net/?retryWrites=true&w=majority" ##mongo database link (necessary)
    DB_URL2="mongodb+srv://Power:powerUltraXBot@cluster0.1q2gvcz.mongodb.net/?retryWrites=true&w=majority" #mongo db (not necessary)
    DB_URL="postgres://ulzydhik:zKIRO9W3Sj2rTtWFw-LJpLcfHz2FRA6n@jelani.db.elephantsql.com/ulzydhik" #postgres sql database link
    REDIS_URL="redis://default:V1PIFnddVQdljAw6OGSZ@containers-us-west-101.railway.app:7447" #redis database url from redislabs.com
    TOKEN="5810699047:AAHBdwpHz9ASP72Wdk2ZRbfCQU4t6leGrgg" #bot token from @BotFather
    DEV_USERS=[1145284986] #developers id
    DRAGONS=[9656] #sudo users id
    DEMONS=[1909] #support user ids
    TIGERS=[1] #commas for multiple ids
    WOLVES=[2112, 1212] #commas for multiple ids 
    DONATION_LINK="https://t.me/Mental_VNM" #u can change with yours
    EVENT_LOGS=-1001791419515  #channel id for gban logs
    JOIN_LOGGER= -1001791419515  #log channel/group id
    OWNER_ID=1145284986 #owner id in integer
    ERROR_LOGS=-1001628946703 #support group id
    BOT_NAME="Gᴄʜ ʙᴏᴛ" #your bot name
    ARQ_API_KEY="XLEPQE-OQEQOU-APAHMM-RGHMQG-ARQ" #ARQ api key from @ARQRobot
    ARQ_API_URL="arq.hamker.dev" #arq link
    SUPPORT_CHAT="vnmbrother" #support group username without @
    OWNER_USERNAME="Mental_VNM" #owner username without @
    UPDATES_CHANNEL="vnmbrother" #Updates/News Channel username without @
    BOT_USERNAME="GameChangersOfficialBot" #bot username without @
    REM_BG_API_KEY="28jwoKAkskaSjsnsksAjnwjUJwj" #not necessary
    GENIUS_API_TOKEN="J968E_20LgxrKjsdN24cqYtD~gNRTbU" # api token from genius.com (not necessary)
    TIME_API_KEY="GPOIC5IBWGWC" #not necessary
    SPAMWATCH_API="4TJ6fBDw3opqHppbjkDIEhqjNPx6OJvBciDJ2hzds4BEgbtj7gchgfinCZIBygH7" #spamwatch api token from @SpamWatchBot
    WALL_API="6950f5ds6a3" #wall api (not necessary)
    BOT_ID = 5518786755

class Production(Config):
    LOGGER=True


class Development(Config):
    LOGGER=True
