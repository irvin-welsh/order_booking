import logging
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
from config import *
import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

upd=Updater(token=API_TOKEN, use_context=True)
dp=upd.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

def random_questions(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Я не понимаю вас. Используйте список моих комманд, для эффективного взаимодействия')
random_questions_handler = MessageHandler(Filters.text, random_questions)

def start(update, context):
    keyboard = [[InlineKeyboardButton("Информация о предлагаемом продукте", callback_data='1'),
                 InlineKeyboardButton("Оставить заявку на продукт", callback_data='2')],

                [InlineKeyboardButton("Связаться с магазином", callback_data='3')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Выберите пункт меню внизу экрана', reply_markup=reply_markup)


def button(update, context):
    query = update.callback_query
    query.answer()

    query.edit_message_text(text="Вы выбрали: {}".format(query.data))

def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CallbackQueryHandler(button))
    dp.add_handler(random_questions_handler)
    upd.start_polling()
    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    upd.idle()

if __name__ == '__main__':
    main()
