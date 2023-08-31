from django.conf import settings
import json
import BO.telegramBO.telegram

def schedule_api():
    status, description, data = BO.telegramBO.telegram.TelegramBO().send_messenge_telegram()

    print(status)
    print(description)