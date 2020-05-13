import logging
from telegram.ext import *
from config import *
import os

upd=Updater(token=API_TOKEN, use_context=True)
dp=upd.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
start_handler = CommandHandler('start', start)

def random_questions(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Я не понимаю вас. Используйте список моих комманд, для эффективного взаимодействия')
random_questions_handler = MessageHandler(Filters.text, random_questions)

dp.add_handler(start_handler)
dp.add_handler(random_questions_handler)
upd.start_polling()
