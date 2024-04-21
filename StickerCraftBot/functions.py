from configure import dispatcher

from aiogram import types

@dispatcher.message_handler(lambda message: message.text == 'Компьютерные технологии')
async def send_photos_сomputer_technology(message: types.Message):
    chat_id = message.from_user.id    
    photos = [
        'photo_themes/сomputer_technology/image_1.png',
        'photo_themes/сomputer_technology/image_2.png',
        'photo_themes/сomputer_technology/image_3.png',
        'photo_themes/сomputer_technology/image_4.png'
    ]

    for photo in photos:
        photo_bytes = types.InputFile(path_or_bytesio=photo)
        await dispatcher.bot.send_photo(chat_id=chat_id, photo=photo_bytes)

@dispatcher.message_handler(lambda message: message.text == 'Эмоции и выражения')
async def send_photos_emotions_and_expressions(message: types.Message):
    chat_id = message.from_user.id    
    photos = [
        'photo_themes/emotions_and_expressions/image_1.png',
        'photo_themes/emotions_and_expressions/image_2.png',
        'photo_themes/emotions_and_expressions/image_3.png',
        'photo_themes/emotions_and_expressions/image_4.png'
    ]

    for photo in photos:
        photo_bytes = types.InputFile(path_or_bytesio=photo)
        await dispatcher.bot.send_photo(chat_id=chat_id, photo=photo_bytes)

@dispatcher.message_handler(lambda message: message.text == 'Смешные ситуации')
async def send_photos_funny_situations(message: types.Message):
    chat_id = message.from_user.id    
    photos = [
        'photo_themes/funny_situations/image_1.png',
        'photo_themes/funny_situations/image_2.png',
        'photo_themes/funny_situations/image_3.png',
        'photo_themes/funny_situations/image_4.png'
    ]

    for photo in photos:
        photo_bytes = types.InputFile(path_or_bytesio=photo)
        await dispatcher.bot.send_photo(chat_id=chat_id, photo=photo_bytes)

@dispatcher.message_handler(lambda message: message.text == 'Фразы и мемы')
async def send_photos_phrases_and_memes(message: types.Message):
    chat_id = message.from_user.id    
    photos = [
        'photo_themes/phrases_and_memes/image_1.png',
        'photo_themes/phrases_and_memes/image_2.png',
        'photo_themes/phrases_and_memes/image_3.png',
        'photo_themes/phrases_and_memes/image_4.png'
    ]

    for photo in photos:
        photo_bytes = types.InputFile(path_or_bytesio=photo)
        await dispatcher.bot.send_photo(chat_id=chat_id, photo=photo_bytes)
