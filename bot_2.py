import logging
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
from config import *
import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

upd=Updater(token=API_TOKEN, use_context=True)
dp=upd.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

def start(bot, update):
  update.message.reply_text(main_menu_message(),
                            reply_markup=main_menu_keyboard())

# def greet_user(`update: Update, context: CallbackContext`):
#     update.message.reply_text('hello')

def main_menu(bot, update):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
                        text=main_menu_message(),
                        reply_markup=main_menu_keyboard())

def first_menu(bot, update):
  query = update.callback_query
  query.answer()
  query.edit_message_text(
                        text=first_menu_message(),
                        reply_markup=first_menu_keyboard())

def second_menu(bot, update):
  query = update.callback_query
  query.answer()
  query.edit_message_text(
                        text=second_menu_message(),
                        reply_markup=second_menu_keyboard())

def first_submenu(bot, update):
  pass

def second_submenu(bot, update):
  pass


def main_menu_keyboard():
    keyboard = [[InlineKeyboardButton("Информация о предлагаемом продукте", callback_data="Отправьте мне 1(один) если про полный комплект\n\n Отправьте 2(два) если про разделку"),
                 InlineKeyboardButton("Оставить заявку на продукт", callback_data='2')],

                [InlineKeyboardButton("Связаться с магазином", callback_data='3')]]
    return InlineKeyboardMarkup(keyboard)

def first_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Submenu 1-1', callback_data='m1_1')],
              [InlineKeyboardButton('Submenu 1-2', callback_data='m1_2')],
              [InlineKeyboardButton('Main menu', callback_data='main')]]
  return InlineKeyboardMarkup(keyboard)

def second_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Submenu 2-1', callback_data='m2_1')],
                [InlineKeyboardButton('Submenu 2-2', callback_data='m2_2')],
                [InlineKeyboardButton('Main menu', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)

def main_menu_message():
  return 'Choose the option in main menu:'

def first_menu_message():
  return 'Choose the submenu in first menu:'

def second_menu_message():
  return 'Choose the submenu in second menu:'

    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
dp.add_handler(CommandHandler('start', start))
dp.add_handler(CallbackQueryHandler(main_menu, pattern='main'))
dp.add_handler(CallbackQueryHandler(first_menu, pattern='m1'))
dp.add_handler(CallbackQueryHandler(second_menu, pattern='m2'))
dp.add_handler(CallbackQueryHandler(first_submenu, pattern='m1_1'))
dp.add_handler(CallbackQueryHandler(second_submenu, pattern='m2_1'))
upd.start_polling()
# Run the bot until the user presses Ctrl-C or the process receives SIGINT,
# SIGTERM or SIGABRT
upd.idle()
