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

    def get_me(self):
        url = f"https://api.telegram.org/bot{self._token}/getMe"
        response = requests.get(url)

        if response.status_code == 200:
            salida = json.loads(response.text)
            return salida
        return None
    
    def get_updates(self):
        url = f"https://api.telegram.org/bot{self._token}/getUpdates"
        print(url)
        response = requests.get(url)

        if response.status_code == 200:
            salida = json.loads(response.text)
            return salida
        return None