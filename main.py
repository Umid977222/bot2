import asyncio
import logging

from aiogram import Bot, Dispatcher, executor, types
from config import token
from aiogram.dispatcher import FSMContext

logging.basicConfig(level=logging.DEBUG)

bot = Bot(token=token, parse_mode="html")
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    buttons = ["Uzb", "Rus", "Eng"]
    keyboard.add(*buttons)
    await message.answer(
        text=f"Xush kelibsz {message.from_user.full_name}",
        reply_markup=keyboard
    )

# @dp.message_handler(commands=["help"])
# async def help_command(message: types.Message):
#     await message.answer(
#         text="Bizning botda hali kamandalar mavjud emas"
#     )


@dp.message_handler(commands="inline")
async def get_button(message: types.Message):
    inl_but = types.InlineKeyboardMarkup(row_width=2)
    inl_but.add(
        types.InlineKeyboardButton(text="1", callback_data="d1"),
        types.InlineKeyboardButton(text="2", callback_data="d2"),
        types.InlineKeyboardButton(text="3", callback_data="d3"),
        types.InlineKeyboardButton(text="4", callback_data="d4"),
    )
    photo2 = open('su-57_large.jpg', 'rb')
    await message.answer_photo(
        photo=photo2,
        reply_markup=inl_but
    )


@dp.message_handler(content_types=types.ContentType.TEXT)
async def choice_lang(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="Contact", request_contact=True),
        types.KeyboardButton(text="Location", request_location=True)
    )
    language = message.text.title()
    if language == "Uzb":
        msg = "Siz o'bek tilini tanladingiz"
    elif language == "Rus":
        msg = "Вы набрали руский язык"
    elif language == "Eng":
        msg = "you selected english"
    await message.answer(
        text=msg,
        reply_markup=types.ReplyKeyboardRemove()
    )
    await message.answer(
        text="tanlang",
        reply_markup=keyboard
    )



@dp.message_handler(commands=['click'])
async def cmd_start(message: types.Message, state: FSMContext):
    async with state.proxy() as proxy:  # proxy = FSMContextProxy(state); await proxy.load()
        proxy.setdefault('counter', 0)
        proxy['counter'] += 1
        return await message.reply(f"Counter: {proxy['counter']}")


@dp.message_handler(commands=["dice"])
async def get_dice(message: types.Message):
    await message.answer_dice(
        emoji="🎲"
    )


@dp.message_handler(commands=["photo"])
async def get_photo1(message: types.Message):
    await message.answer_photo("https://www.airdatanews.com/russia-may-develop-the-super-flanker-fighter-from-2027/")

@dp.message_handler(commands=["video"])
async def get_video(message: types.Message):
    video = open("fa9e27a7534060df383ab54354fcead3_w200.gif", 'rb')
    await message.answer_video(
        video
    )



# @dp.errors_handler(exception='BotBlocked')
# async def handle_error(update: types.Update, exception: Exception):
#     print("Bot blocked")
#     return True
#
#
# @dp.message_handler(commands=["help"])
# async def help_error(message: types.Message):
#     await asyncio.sleep(20)
#     await message.answer(
#         text=f"how can i help you"
#     )

if __name__ == "__main__":
    executor.start_polling(dispatcher=dp)