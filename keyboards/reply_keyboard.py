### ФАЙЛ СОЗДАНИЯ КЛАВИАТУР

from aiogram.types import  ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder



# Клавиатура Админа
admin_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Добавить товар'),
            KeyboardButton(text='Изменить товар')
        ],
        [
            KeyboardButton(text='Удалить товар'),
            KeyboardButton(text='Посмотреть')
        ],
        [
            KeyboardButton(text='Назад')
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='Выбери действие'
)


# стартовая Клавиатура
start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Продукция магазина"),
            KeyboardButton(text="Контакты"),
        ],
        {
            KeyboardButton(text="Доставка"),
            KeyboardButton(text="Оплата"),
        }
    ],
    resize_keyboard=True,
    input_field_placeholder='Что Вас интересует?'
)


# Клавиатура Продукция магазина
shop_kb = ReplyKeyboardBuilder()
shop_kb.add (
    KeyboardButton(text='Товары для детей'),
    KeyboardButton(text='Товары для взрослых'),
    KeyboardButton(text='Назад'),
   
)
shop_kb.adjust(2, 1)


# Клавиатура Контакты
contacts_kb = ReplyKeyboardBuilder()
contacts_kb.add (
    KeyboardButton(text='Связаться по телефону'),
    KeyboardButton(text='Написать на электронку'),
    KeyboardButton(text='Назад'),
   
)
contacts_kb.adjust(2, 1)


# Клавиатура Доставка
delivery_kb = ReplyKeyboardBuilder()
delivery_kb.add (
    KeyboardButton(text='Мск / Спб'),
    KeyboardButton(text='РФ'),
    KeyboardButton(text='Назад'),
   
)
delivery_kb.adjust(2, 1)


# Клавиатура Оплата
payment_kb = ReplyKeyboardBuilder()
payment_kb.add (
    KeyboardButton(text='Карта'),
    KeyboardButton(text='Крипта'),
    KeyboardButton(text='Назад'),
   
)
payment_kb.adjust(2, 1)



