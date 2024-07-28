### ФАЙЛ С КАСТОМНЫМИ ФИЛЬТРАМИ ДЛЯ ВЫБОРА ЧАТА И ДЛЯ ПРОВЕРКИ ПОЛНОМОЧИЙ АДМИНА

from typing import Any
from aiogram import types, Bot
from aiogram.filters import Filter

class ChatTypeFilter(Filter):   # создаю класс на основе базового класса Filter
    def __init__(self, chat_types: list[str]) -> None:
        self.chat_types = chat_types  # в параметр chat_types при обращении к фильтру
        # передаю список из типов чатов,в которых будет работать тот или иной роутер
        
    async def __call__(self, message: types.Message) -> bool:    # переопределяю метод __call__
        return message.chat.type in self.chat_types    # aiogram сам передаёт объект message (сообщение, которое отправил пользователь)
    
    
    
class IsAdmin(Filter):
    def __init__(self) -> None:
        pass    # заглушка
    
    async def __call__(self, message: types.Message, bot: Bot) -> bool:    # принимает сообщение, прокидываю объект Бота
        return message.from_user.id in bot.my_admins_list   # вначале получает id юзера, который пишет боту
    # и сравнивает, является ли допустимым к вазимодействию с ботом id
    # Поэтому нужен список админов группы, чтобы сравнивать с ними и разрешать им взаимодействие