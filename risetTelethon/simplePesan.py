from telethon import TelegramClient, events
import os
import configparser
import asyncio
from telethon.errors import SessionPasswordNeededError

config = configparser.ConfigParser()
config.read('config.ini')

api_id = config['DATA']['API_ID']
api_hash = config['DATA']['API_HASH']
dataSession = config['DATA']['DATA_SESSION']
idTelegram4Kofirmasi = config['DATA']['ID_TELE4_CONF']
phone_number = config['DATA']['PHONE']

client = TelegramClient(dataSession, api_id, api_hash)

async def main():
    async with client:
        await client.send_message(idTelegram4Kofirmasi, 'tes Koneksi')
        async with client.conversation(idTelegram4Kofirmasi) as conv:
            await conv.send_message('Hi!')
            hello = (await conv.get_response()).raw_text
            
            await conv.send_message('tes Nama:')
            name = (await conv.get_response()).raw_text

            await conv.send_message('halloo {}!'.format(name))

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())