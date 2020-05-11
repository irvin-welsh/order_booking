import logging
from aiogram import Bot, Dispatcher, executor, types, md
from config import *  # create config.py file in the same directory to store sensitive data (e.g. API bot token)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def check_language(message: types.Message):
    locale = message.from_user.locale

    await message.reply(md.text(
        md.bold('Info about your language:'),
        md.text('🔸', md.bold('Code:'), md.code(locale.language)),
        md.text('🔸', md.bold('Territory:'), md.code(locale.territory or 'Unknown')),
        md.text('🔸', md.bold('Language name:'), md.code(locale.language_name)),
        md.text('🔸', md.bold('English language name:'), md.code(locale.english_name)),
        sep='\n',
    ))
# @dp.message_handler()
# async def echo(sticker: types.StickerSet):
#     # old style:
#     # await bot.send_message(message.chat.id, message.text)
#
#     await sticker.answer(sticker.sticker)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
