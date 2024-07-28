### ХЕНДЛЕРЫ ДЛЯ РАБОТЫ БОТА В ЛИЧКЕ С ПОЛЬЗОВАТЕЛЯМИ

from aiogram import F, types, Router
from aiogram.filters import Command, CommandStart, or_f

from filters.chat_types import ChatTypeFilter    # импорт кастомных фильтров из файла
from keyboards.reply_keyboard import start_kb, shop_kb, delivery_kb, contacts_kb, payment_kb, admin_kb    # импорт клавиатур из файла


user_private_router = Router()  # создание экземпляра класса Router для линка в файле app.py
user_private_router.message.filter(ChatTypeFilter('private'))   #навешиваю фильтр прямо на Router, чтобы проверка срабатывала до момента прохождения по всем хендлерам
# в параметр передаю тип чатов, в которых будет работать фильтр

@user_private_router.message(or_f(CommandStart(), F.text.lower().contains ('назад')))    # тип события, которое приходит к боту - message
async def start_cmd(message: types.Message):   # в этот хендлер попадает вся  информация, он будет реагировать на любые сообщения
    await message.answer('Привет, я тут главный',
                         reply_markup=start_kb
                         )
    
    
    
@user_private_router.message(F.text.lower().contains ('магаз'))    # тип события, которое приходит к боту - message
async def shop_cmd(message: types.Message):   # в этот хендлер попадает вся  информация, он будет реагировать на любые сообщения
    await message.answer('Магазин:', 
                         reply_markup=shop_kb.as_markup(
                             resize_keyboard=True,
                             input_field_placeholder='Что Вас интересует?'  
                         ))
    
    
@user_private_router.message(F.text.lower().contains ('контакт'))    # тип события, которое приходит к боту - message
async def contacts_cmd(message: types.Message):   # в этот хендлер попадает вся  информация, он будет реагировать на любые сообщения
    await message.answer('Контакты:', 
                         reply_markup=contacts_kb.as_markup(
                             resize_keyboard=True,
                             input_field_placeholder='Что Вас интересует?'  
                         ))
    
    
@user_private_router.message(F.text.lower().contains ('доставк'))    # тип события, которое приходит к боту - message
async def delivery_cmd(message: types.Message):   # в этот хендлер попадает вся  информация, он будет реагировать на любые сообщения
    await message.answer('Варианты доставки:', 
                         reply_markup=delivery_kb.as_markup(
                             resize_keyboard=True,
                             input_field_placeholder='Что Вас интересует?'  
                             ))
    
    
@user_private_router.message(F.text.lower().contains ('оплат'))    # тип события, которое приходит к боту - message
async def payment_cmd(message: types.Message):   # в этот хендлер попадает вся  информация, он будет реагировать на любые сообщения
    await message.answer('Способы оплаты:', 
                         reply_markup=payment_kb.as_markup(
                             resize_keyboard=True,
                             input_field_placeholder='Что Вас интересует?'  
                         ))
