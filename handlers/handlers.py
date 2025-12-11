from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.methods import send_gift

from handlers.keyboards import *
from database.database_handlers import *
from utils.check_subscribe import check_all_subscriptions
from config import bot

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    telegram_id = message.from_user.id
    user_data = await get_user(telegram_id)

    if user_data is None:
        await add_user(
            telegram_id=telegram_id,
            username=message.from_user.username,
            first_name=message.from_user.first_name,
        )
        subscribe_status = False
    else:
        subscribe_status = user_data.get('subscribe_status', False)

    if subscribe_status:
        await message.answer("Выберите действие:", reply_markup=gift_markup)
    else:
        await message.answer(
            "Для получения подарка необходимо подписаться на следующие каналы:",
            reply_markup=channels_murkup,
        )



@router.message(F.text == "🧸 Получить мишку")
async def give_gift(message: Message):
    telegram_id = message.from_user.id
    chat_id = message.chat.id
    user_data = await get_user(telegram_id)
    gift_status = user_data.get('gift_status')

    if gift_status:
        await message.answer("☺️ Вы уже получили подарок!")
    else:
        await bot.send_gift(
            gift_id="5170233102089322756",
            user_id=telegram_id,
            chat_id=chat_id,
            text="Что бы тоже получить подарок, перейди в бота и подпишись на канал!",
        )
        await update_get_gift_status(telegram_id=telegram_id, get_gift=True)


@router.message(F.text == "🩷 Получить сердце")
async def give_gift(message: Message):
    telegram_id = message.from_user.id
    chat_id = message.chat.id
    user_data = await get_user(telegram_id)
    gift_status = user_data.get('gift_status')

    if gift_status:
        await message.answer("☺️ Вы уже получили подарок!")
    else:
        await bot.send_gift(
            gift_id="5170145012310081615",
            user_id=telegram_id,
            chat_id=chat_id,
            text="Что бы тоже получить подарок, перейди в бота и подпишись на канал!",
        )
        await update_get_gift_status(telegram_id=telegram_id, get_gift=True)



@router.callback_query(F.data == "check_subscription")
async def check_subs_func(call: CallbackQuery):
    await call.answer("Запускаю проверку подписок на каналы")

    user_id = call.from_user.id

    is_subscribed = await check_all_subscriptions(user_id)

    if not is_subscribed:
        await call.message.answer(
            f"❌ Вы не подписались на все каналы!", reply_markup=channels_murkup
        )
        return

    await update_subscribe_status(telegram_id=user_id, subscribe_status=True)
    await call.message.answer(
        "✅ Спасибо за подпискy на все каналы! Теперь вы можете выбрать подарок!",
        reply_markup=gift_markup,
    )
