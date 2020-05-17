### Imorting necessary handlers and modules from Telegram API_TOKEN
### Config module must be generated by yourself including TOKEN and other configurations for your bot
### working_days_counter is also another file where you add business logic

import logging
from telegram.ext import MessageHandler, CommandHandler, Updater, Filters
from config import *
from working_days_counter import get_working_days
import os
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup

upd=Updater(token=API_TOKEN, use_context=True)
dp=upd.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

# callback function to handle "/start" command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
start_handler = CommandHandler('start', start)

# caption for unhandled input
def random_questions(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Я не понимаю вас. Используйте список моих комманд, для эффективного взаимодействия')
random_questions_handler = MessageHandler(Filters.text, random_questions)

# callback function to handle "/slots" command which returns list of available dates for booking
def get_slots(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=get_working_days())
get_slots_handler=CommandHandler('slots', get_slots)

# calling handlers (commands handlers must go FIRST)
dp.add_handler(start_handler)
dp.add_handler(get_slots_handler)
dp.add_handler(random_questions_handler)

# using pooling method in this case
upd.start_polling()
