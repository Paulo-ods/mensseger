# import logging
# from telegram.ext import Updater, MessageHandler, Filters
#
# import core.models
#
#
# class WelcomeBot():
#
#     def __init__(self):
#         self.token = core.models.IntegrationKeys.objects.filter(module='telegram').values_list('token', flat=True).first()
#         self.main()
#
#     def welcome_message(self, update=None, context=None):
#         new_member = update.message.new_chat_members[0]
#         chat_id = update.message.chat_id
#         welcome_text = f'Bem-vindo(a), {new_member.first_name}!'
#
#         context.bot.send_message(chat_id=chat_id, text=welcome_text)
#
#     def main(self):
#         updater = Updater(token=self.token, use_context=True)
#         dp = updater.dispatcher
#
#         dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, self.welcome_message()))
#
#         updater.start_polling()
#         updater.idle()
