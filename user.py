from aiogram.dispatcher import FSMContext

from loader import dp, db
from aiogram import types
from states.user_reg import RegisterState


@dp.message_handler(commands="start")
async def user_start(message: types.Message):
    if await db.get_user_by_id(chat_id=message.chat.id):
        text = "Xushkelibsiz.."
        await message.answer(text=text)
    else:
        text = "Assalomu alaykum ismingizni  kriting"
        await message.answer(text=text)
        await RegisterState.full_name.set()


@dp.message_handler(state=RegisterState.full_name)
async def get_full_name(message: types.Message, state: FSMContext):
    await state.update_data(full_name=message.text, chat_id=message.chat.id)
    text = "Telefon Raqam"
    await message.answer(text=text)
    await RegisterState.phone_number.set()


@dp.message_handler(state=RegisterState.phone_number)
async def get_phone_number(message: types.Message, state: FSMContext):
    await state.update_data(full_name=message.text)
    text = "Telefon Raqam"
    await message.answer(text=text)
    await RegisterState.phone_number.set()


@dp.message_handler(state=RegisterState.location)
async def get_location(message: types.Message, state: FSMContext):
    await state.update_data(location=message.text)

    data = await state.get_data()
    if db.add_user(data):
        text = "muvaffaqiyatli"
    else:
        text = "muvaffaqiyatsz"
    await message.answer(text=text)
    await state.finish()
