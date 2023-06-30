from youtube_search import YoutubeSearch
from aiogram import Dispatcher, Bot, executor, types
from aiogram.dispatcher.filters import Text
from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher(bot)

# Начало
@dp.message_handler(commands='start')
async def hello(message: types.Message):
    start_button = ['Поиск']
    keyboards = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboards.add(*start_button)
    await message.answer("Привет! Это бот поиска видео на youtube", reply_markup=keyboards)


# Поиск 10 видео
@dp.message_handler(Text(equals='Поиск'))
async def search(message: types.Message):
    await bot.send_message(message.chat.id, "Введите запрос:")

@dp.message_handler(content_types='text')
async def resutl(message: types.Message):
    search_yt = YoutubeSearch(message.text, max_results=10).to_dict()
    key = 'id'
    
    banned_word = ['/', ' ', 'porn', 'xxx', ',', '.', '|']
    
    if message.text in banned_word:
        await message.reply('Введите коректное название')
    else:
        for res in search_yt:
            res_link = f'https://www.youtube.com/watch?v={res.get(key)}'
            await bot.send_message(message.chat.id, res_link)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

