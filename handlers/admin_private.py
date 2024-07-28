### ФАЙЛ РАБОТЫ АДМИНА С БОТОМ

from aiogram import F, Router, types
from aiogram.filters import Command

from filters.chat_types import ChatTypeFilter, IsAdmin
from keyboards.reply_keyboard import admin_kb


admin_router = Router()
admin_router.message.filter(ChatTypeFilter(['private']), IsAdmin())   # фильтр на роутер для обработки сообщений в личке от админа группы


@admin_router.message(F.text.lower().contains('admin'))   # на команду /admin от  админа группы в личке бот отвечает клавиатурой админа, для остальных пользователей игнор
async def admin_cmd(message: types.Message):
    await message.answer ('Что хочешь сделать?',
                          reply_markup=admin_kb)


    
@admin_router.message(F.text == 'Посмотреть')
async def starring_at_product(message: types.Message):
    await message.answer('Вот список товаров') 
    
@admin_router.message(F.text == 'Изменить товар')
async def change_at_product(message: types.Message):
    await message.answer('Вот список товаров') 
    
    
@admin_router.message(F.text == 'Удалить товар')
async def delete_at_product(message: types.Message):
    await message.answer('Выберите товар для удаления') 
    
 