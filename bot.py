from aiogram import types, Bot, executor
from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage


import os

import db

import classes
import markup

bot = Bot(token="")
# Диспетчер
dp = Dispatcher(bot,storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.chat.id != :#user id админа
        await message.answer('Вы не админ')
        return
    await message.answer('Добро пожаловать в админ панель',reply_markup=markup.markup_admin())

@dp.message_handler()
async def number(message: types.Message):
    if message.chat.id != :#user id админа
        await message.answer('Вы не админ')
        return
    if message.text == 'Рассылка':
        await message.answer('Напишите текст')
        await classes.Mailing.message.set()
    elif message.text == 'Изменить приветствие':
        await message.answer('Напишите текст')
        await classes.change.message.set()
    elif message.text == 'Прием заявок':
        await message.answer('Прием заявок:',reply_markup=markup.markup())
    else:
        await message.answer('Я не понял Вас!')

@dp.message_handler(content_types=types.ContentType.PHOTO,state=classes.Mailing.message)
async def process_name(message: types.Message, state: FSMContext):
    photo = message.photo[-1]
    name = 'photo_mailing.jpg'
    await photo.download(destination=name)
    await state.update_data(message=message.caption)
    text = await state.get_data()
    with open(name, 'rb') as phot:
        photo_data = phot.read()
    for user in db.users():
        await bot.send_photo(user[0],photo=photo_data,caption=text['message'])
    os.remove(name)
    await message.answer('Рассылка сделана')
    await state.finish()

@dp.message_handler(content_types=types.ContentType.PHOTO,state=classes.change.message)
async def process_name(message: types.Message, state: FSMContext):
    photo = message.photo[-1]
    name = 'change.jpg'
    try:
        os.remove(name)
    except:
        pass
    await photo.download(destination=name)
    await state.update_data(message=message.caption)
    text = await state.get_data()
    await message.answer('Приветствие изменено')
    db.change(text['message'])
    await state.finish()

@dp.callback_query_handler(text='yes')
async def next_menu(callback: types.CallbackQuery):
    await callback.message.answer('Вы включили автоприем')
    db.channel_change('yes')

@dp.callback_query_handler(text='no')
async def next_menu(callback: types.CallbackQuery):
    await callback.message.answer('Вы выключили автоприем')
    db.channel_change('no')

@dp.chat_join_request_handler()
async def join_request(update: types.ChatJoinRequest):
    user_id = update.from_user.id
    text = db.mailing()
    if db.add(user_id):
        with open('change.jpg', 'rb') as phot:
            await bot.send_photo(user_id, photo=phot, caption=text)
    if db.channel() == 'no':
        return
    await update.approve()


executor.start_polling(dp,skip_updates=True)
