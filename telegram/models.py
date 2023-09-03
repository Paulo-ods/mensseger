
from django.db import models

import core.models


# Create your models here.


class TelegramChat(core.models.Log):
    cd_chat = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=512)
    type_code = models.CharField(null=True, max_length=255, default='group')
    type_config = models.CharField(null=True, max_length=255, default='TELEGRAM-CHAT')


    class Meta:
        db_table = 'telegram_chat'


class TelegramMessagesCategory(core.models.Log):
    category = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=512, null=True)
    parent_category = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True, related_name='category_parent')

    class Meta:
        db_table = 'telegram_messages_category'


class TelegramMessages(core.models.Log):
    message = models.CharField(max_length=4096, null=True)
    category = models.ForeignKey('TelegramMessagesCategory',  on_delete=models.DO_NOTHING, null=True, related_name='category_message')

    class Meta:
        db_table = 'telegram_messages'
