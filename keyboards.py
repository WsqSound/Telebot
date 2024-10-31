from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='Услуги'), KeyboardButton(text='Портфолио')],
        [KeyboardButton(text='Прайс-лист'), KeyboardButton(text='Условия выполнения работ')],
        [KeyboardButton(text='Написать мне в telegram')],
        [KeyboardButton(text='Написать мне в vk')],
], 
    resize_keyboard=True,
    input_field_placeholder='Выберите пункт меню...')

# after_main = ReplyKeyboardMarkup(
#     keyboard=[
#         [KeyboardButton(text='Написать мне в telegram')],
#         [KeyboardButton(text='Написать мне в vk')],
#         [KeyboardButton(text='Условия выполнения работ')],

# ], 
# resize_keyboard=True,
#     input_field_placeholder='Напишите автору...')