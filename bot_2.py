import logging
from telegram.ext import MessageHandler, CommandHandler, Updater, Filters
from config import *
from working_days_counter import get_working_days
import os
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup

upd=Updater(token=API_TOKEN, use_context=True)
dp=upd.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
start_handler = CommandHandler('start', start)

def random_questions(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Я не понимаю вас. Используйте список моих комманд, для эффективного взаимодействия')
random_questions_handler = MessageHandler(Filters.text, random_questions)

def get_slots(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=get_working_days())
get_slots_handler=CommandHandler('slots', get_slots)

dp.add_handler(start_handler)
dp.add_handler(get_slots_handler)
dp.add_handler(random_questions_handler)
upd.start_polling()
