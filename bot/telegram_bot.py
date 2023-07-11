import requests
import json

PROPERTIES = './bot/telegram_keys'

class TelegramBot():
    def __init__(self):
        self._token = None
        self._group = None
        self._channel = None

        with open(PROPERTIES, 'r') as file_reader:
            params = json.load(file_reader)
            self._token = params['token']
            self._group = params['group']
            self._channel = params['channel']