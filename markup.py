from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup
def markup_admin():
        markup_admin = ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = [
                KeyboardButton(text="Рассылка"),
                KeyboardButton(text="Изменить приветствие"),
                KeyboardButton(text="Прием заявок"),
                ]
        markup_admin.add(*buttons)
        return markup_admin
def markup():
        markup = InlineKeyboardMarkup()
        buttons = [
                KeyboardButton(text="Включить",callback_data='yes'),
                KeyboardButton(text="Отменить",callback_data='no'),
        ]
        markup.add(*buttons)
        return markup




