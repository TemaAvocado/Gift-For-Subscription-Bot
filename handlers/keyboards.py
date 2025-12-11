from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from config import channels

gift_markup = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🧸 Получить мишку"), KeyboardButton(text="🩷 Получить сердце")]
    ],
    resize_keyboard=True
)

def build_channels_markup():
    inline_keyboard = []
    
    for channel_name, channel_url in channels.items():
        inline_keyboard.append(
            [InlineKeyboardButton(
                text=channel_name, 
                url=channel_url
            )]
        )
    
    inline_keyboard.append(
        [InlineKeyboardButton(
            text="✅ Проверить подписку", 
            callback_data="check_subscription"
        )]
    )
    
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)\
    
channels_murkup = build_channels_markup()