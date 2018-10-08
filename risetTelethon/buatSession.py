from telethon import TelegramClient, sync
import os
import configparser
from telethon.errors import SessionPasswordNeededError

config = configparser.ConfigParser()
config.read('config.ini')

api_id = config['DATA']['API_ID']
api_hash = config['DATA']['API_HASH']
dataSession = config['DATA']['DATA_SESSION']
idTelegram4Kofirmasi = config['DATA']['ID_TELE4_CONF']
phone_number = config['DATA']['PHONE']

client = TelegramClient(dataSession, api_id, api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone_number)
    me = client.sign_in(phone_number, input('Enter code: '))

client.send_message(idTelegram4Kofirmasi, 'Database Session '+dataSession+' telah dibuat!')
client.disconnect()