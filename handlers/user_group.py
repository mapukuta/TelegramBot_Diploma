### ХЕНДЛЕРЫ ДЛЯ РАБОТЫ БОТА В ГРУППАХ

import re

from aiogram import Bot, Router, types, F  # Импорт классов для объекта Бот, Роутер, модуля types и магического фильтра F
from aiogram.filters import Command


from string import punctuation  # импорт модуля обработки текста для дальнейшей фильтрации сообщений

from filters.chat_types import ChatTypeFilter  # импорт кастомных фильтров из файла
from common.bad_words import bad_words #импорт запретных слов и ссылок из файла


user_group_router = Router()   # создание экземпляра класса Router для линка в файле app.py
user_group_router.message.filter(ChatTypeFilter(['group', 'supergroup'])) #навешиваю фильтр прямо на Router, чтобы проверка срабатывала до момента прохождения по всем хендлерам
# в параметр передаю типы чатов, в которых будет работать фильтр
user_group_router.edited_message.filter(ChatTypeFilter(['group', 'supergroup']))

# Список администраторов группы (взаимодействие с файлами admin_private, chat_types)

@user_group_router.message(Command('admin'))
async def get_admins(message: types.Message, bot: Bot):
    chat_id = message.chat.id    # вытаскиваю из события message chat_id
    admins_list = await bot.get_chat_administrators(chat_id)  #формирую admins_list, используя метод Бота get_chat_administrators,
    # в который передаю id чата
    # бот делает запрос на сервер телеграма и получает список участников
    # print(admins_list)
    
    # если статус - создатель иил админ, то
    # работает генератор списка из id админов и создателей,
   
    admins_list = [
        member.user.id
        for member in admins_list
        if member.status == 'creator' or member.status == 'administrator'
    ]
    bot.my_admins_list = admins_list   # назначаю полученный новый список
    if message.from_user.id in admins_list:
        await message.delete()   # если написал админ - удаляет команду, если обычный юзер - игнор



# Обработка запрещённых слов и ссылок
def clean_text(text:str):
    return text.translate(str.maketrans('', '', punctuation))   # maketrans- если юзер хочет замаскировать запрещённое слово



@user_group_router.edited_message()   # Для отлова редактированных сообщений 
@user_group_router.message()
async def filter_words(message: types.Message):
    if 'http' in message.text:
        await message.answer(f'{message.from_user.first_name}, ССЫЛКИ ЗАПРЕЩЕНЫ!')
        await message.delete()
    elif bad_words.intersection(clean_text(message.text.lower()).split()):   #ищет совпадения в другом множестве
        await message.answer(f'{message.from_user.first_name}, КАКОЙ ТЫ МНЕ {(message.text).upper()} ?! ')
        await message.delete()  # Удаляем сообщение 
    