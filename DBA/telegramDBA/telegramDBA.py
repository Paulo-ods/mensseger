import telegram.models


class TelegramDBA:
    def __init__(self):
        pass

    @staticmethod
    def get_list_message_group(category=None):
        messages = list(telegram.models.TelegramMessages.objects.filter(
            status=True, category=category
        ).values_list(
            'message', flat=True
        ))

        return messages

    @staticmethod
    def get_list_chat():
        chat = list(telegram.models.TelegramChat.objects.filter(
            status=True, type_code='group'
        ).values_list(
            'cd_chat', flat=True
        ))

        return chat
