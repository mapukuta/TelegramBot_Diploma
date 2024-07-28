### ТОЧКА ВХОДА В БОТА

import os        # импорт модуля работы с операционной системой 
import asyncio   # импорт асинхронной библиотеки

from aiogram import Bot, Dispatcher, types   # импорт классов 

# моделируем поведение бота на сервере, когда токен берется из переменных окружения
from dotenv import find_dotenv, load_dotenv   # Для этого из библиотеки dotenv импортирую две функции

load_dotenv(find_dotenv())   # загрузка переменной окружения из файла .env



from handlers.user_private import user_private_router   #импорт роутера из файла общения пользователей
from handlers.user_group import user_group_router   # импорт роутера из файла группового общения
from handlers.admin_private import admin_router



ALLOWED_UPDATES = ['message', 'edited_message']    # обрабатываемые обновления

bot = Bot(token=os.getenv('TOKEN'))   # инициализация бота (токен считывается из переменных окружения)
bot.my_admins_list = []   # пустой список, в который будет добавляться админ группы

dp = Dispatcher()   # диспетчер обрабатывает все сообщения боту от сервера, все обновления

dp.include_router(user_private_router)    # подключаю роутер общения пользователей к диспетчеру
dp.include_router(user_group_router)
dp.include_router(admin_router)




async def main():    # сообщает Питону, что это асинхронная функция
    await bot.delete_webhook(drop_pending_updates=True)   # сброс ожидающих обновлений, прозошедших, пока бот был оффлайн
    # await bot.set_my_commands(commands=private, scope = types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)   # запуск бота в работу (бесконечные запросы серверу Телеграма об обновлениях)

asyncio.run(main())   # запуск через библиотеку