import random

import requests

from BO.integration.integration import IntegrationBO
from DBA.integrationDBA.integrationDBA import IntegrationDBA
from DBA.telegramDBA.telegramDBA import TelegramDBA


class TelegramBO(IntegrationBO, IntegrationDBA, TelegramDBA):
    def send_messenge_telegram(self, category=None):
        descricao = ''
        try:
            token = self.get_token(module='telegram', name='telegram_path')
            path = self.get_path(module='telegram', name='telegram_path')
            url = f"{path}bot{token}/sendMessage"
            message = random.choice(self.get_list_message_group(category=category))
            chat_id = self.get_list_chat()
            params = {
                'text': message,
            }
            for chat in chat_id:
                params['chat_id'] = chat
            # Envie a solicitação POST para a API do Telegram
                response = requests.post(url, data=params)

            # Verifique a resposta da API
                if response.status_code == 200:
                    descricao = "Mensagem enviada com sucesso!"
                else:
                    descricao = "Ocorreu um erro ao enviar a mensagem:" + response.text
            return True, descricao, None
        except ValueError:
            return False, "Request Error", None

    def send_messenge_welcome_telegram(self, category=None, data=None):
        descricao = ''
        try:
            if data['chat']:
                pass
            if data['message']:
                token = self.get_token(module='telegram', name='telegram_path')
                path = self.get_path(module='telegram', name='telegram_path')
                url = f"{path}bot{token}/sendMessage"
                message = random.choice(self.get_list_message_group(category=category))
                chat_id = [data['message']['chat'].get('id')]
                params = {
                    'text': message + ' ' + data['message']['new_chat_participant'].get('first_name'),
                }
                for chat in chat_id:
                    params['chat_id'] = chat
                    # Envie a solicitação POST para a API do Telegram
                    response = requests.post(url, data=params)

                    # Verifique a resposta da API
                    if response.status_code == 200:
                        descricao = "Mensagem enviada com sucesso!"
                    else:
                        descricao = "Ocorreu um erro ao enviar a mensagem:" + response.text
            return True, descricao, None
        except ValueError:
            return False, "Request Error", None