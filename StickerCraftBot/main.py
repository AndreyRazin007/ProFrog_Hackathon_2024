import logging
from aiogram import Bot, Dispatcher, types
from aiogram import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import configure

# Создаем экземпляр бота и диспетчера
bot = Bot(configure.config["token"])
storage = MemoryStorage()
dispatcher = Dispatcher(bot, storage=storage)

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Команда /start
@dispatcher.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply(f"Привет, {message.from_user.full_name}! " +
                        "Я бот. Добро пожаловать!")

@dispatcher.message_handler(content_types=types.ContentType.PHOTO)
async def handle_photo(message: types.Message):
    photo = message.photo[-1]
    await photo.download()

    await message.answer("Фотография сохранена!")

# Команда /choose_theme
@dispatcher.message_handler(commands=['choose_theme'])
async def choose_theme(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    keyboard.add(types.KeyboardButton(text="Компьютерные технологии"))
    keyboard.add(types.KeyboardButton(text="Эмоции и выражения"))
    keyboard.add(types.KeyboardButton(text="Смешные ситуации"))
    keyboard.add(types.KeyboardButton(text="Фразы и мемы"))

    await message.reply("Выберите тему для стикерпака:", reply_markup=keyboard)

@dispatcher.message_handler(content_types=types.ContentType.PHOTO)
async def send_photo(message: types.Message):
    await message.reply(message.photo[-1].file_id)

# Команда /photo
@dispatcher.message_handler(commands=['photo'])
async def send_photo(message: types.Message):
    chat_id = message.from_user.id

    photo_bytes = types.InputFile(path_or_bytesio='sticker_themes_1/image_1.png')
    await dispatcher.bot.send_photo(chat_id=chat_id, photo=photo_bytes)

# Команда /album
@dispatcher.message_handler(commands=['album'])
async def send_album(message: types.Message):
    photo_bytes_1 = types.InputFile(path_or_bytesio='sticker_themes_1/image_1.png')
    photo_bytes_2 = types.InputFile(path_or_bytesio='sticker_themes_1/image_2.png')
    photo_bytes_3 = types.InputFile(path_or_bytesio='sticker_themes_1/image_3.png')
    photo_bytes_4 = types.InputFile(path_or_bytesio='sticker_themes_1/image_4.png')
    
    await dispatcher.bot.send_photo(chat_id=message.from_user.id, photo=photo_bytes_1)
    await dispatcher.bot.send_photo(chat_id=message.from_user.id, photo=photo_bytes_2)
    await dispatcher.bot.send_photo(chat_id=message.from_user.id, photo=photo_bytes_3)
    await dispatcher.bot.send_photo(chat_id=message.from_user.id, photo=photo_bytes_4)

# Команда /source_code
@dispatcher.message_handler(commands=['source_code'])
async def source_code(message: types.Message):
    await message.reply("Исходный код доступен по ссылке:\n"
                        "https://github.com/AndreyRazin007/ProFrog_Hackathon_2024")
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Перейти на GitHub", url="https://github.com/AndreyRazin007/ProFrog_Hackathon_2024"))

    await message.reply("Нажмите кнопку, чтобы перейти на GitHub:", reply_markup=keyboard)

# Команда /help
@dispatcher.message_handler(commands=['help'])
async def show_help(message: types.Message):
    help_text = "Список команд:\n" \
                "/start - запустить бот\n" \
                "/choose_theme - выбрать тему для стикерпака\n" \
                "/source_code - вывести ссылку на исходный код\n" \
                "/help - помощь"
    await message.answer(help_text)

if __name__ == '__main__':
    executor.start_polling(dispatcher, skip_updates=True)
