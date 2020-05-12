import logging
import telegram
from telegram.ext import Updater, CommandHandler, Dispatcher
from config import *
import os
# # from aiogram import Bot, Dispatcher, executor, types, md
# from aiogram import Dispatcher, executor, types, md
# create config.py file in the same directory to store sensitive data (e.g. API bot token)
# from PIL import Image

# Configure logging
logging.basicConfig(level=logging.INFO)
# Initialize bot and dispatcher
bot = telegram.Bot(token='1141274977:AAFNEYbbUCmBbAWI-PXwTOPoHW5dnwUbwIU')
updater = Updater(token='1141274977:AAFNEYbbUCmBbAWI-PXwTOPoHW5dnwUbwIU', use_context=True)

# @telegram.ext.CommandHandler('test', find_file_ids())
def find_file_ids():
    telegram.ext.CommandHandler('test', find_file_ids())
        # bot.sendPhoto(chat_id='276893349', photo="https://i1.wp.com/selomoe.ru/wp-content/uploads/2015/12/chasti-svini.jpg-CJdAAMBAAMCAANtAAMz9gEAARkE", caption="Схема разделки свиняки")
        # # А теперь отправим вслед за файлом его file_id
    bot.sendPhoto(chat_id='276893349', photo="AQADaPn4Il0AAzT2AQAB", reply_to_message_id=msg)
    time.sleep(3)

bot.start_pooling(bot)
# telegram.ext.Updater(bot, 4)


# @bot.message_handler(commands=['start'])
# async def send_welcome(message: types.Message):
#     await message.reply("Этот бот может доставить свежайшую свинину вам домой\nДля подробной информации о продукции введите /info\nДля связи с магазином введите /help")

# @dp.message_handler(commands=['info'])
# def show_pics(commands):
#     img  = Image.open("./data/svin_1.jpg")
#     return img



# @dp.message_handler(commands=['help'])
# async def support_agent(message: type.Message):
#     await messa

# @dp.message_handler()
# async def check_language(message: types.Message):
#     locale = message.from_user.locale
#
#     await message.reply(md.text(
#         md.bold('Info about your language:'),
#         md.text('🔸', md.bold('Code:'), md.code(locale.language)),
#         md.text('🔸', md.bold('Territory:'), md.code(locale.territory or 'Unknown')),
#         md.text('🔸', md.bold('Language name:'), md.code(locale.language_name)),
#         md.text('🔸', md.bold('English language name:'), md.code(locale.english_name)),
#         sep='\n',
    # ))
# @dp.message_handler()
# async def echo(sticker: types.StickerSet):
#     # old style:
#     # await bot.send_message(message.chat.id, message.text)
#
#     await sticker.answer(sticker.sticker)
