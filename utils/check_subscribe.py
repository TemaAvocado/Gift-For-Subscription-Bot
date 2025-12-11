from aiogram.enums import ChatMemberStatus
from config import bot, channels


async def check_all_subscriptions(telegram_id: int) -> bool:
    if not channels:
        return True
    
    for channel_name, channel_url in channels.items():
        try:
            channel_username = channel_url.split('/')[-1]
            
            member = await bot.get_chat_member(
                chat_id=f"@{channel_username}" if not channel_username.startswith('@') else channel_username,
                user_id=telegram_id
            )
            
            if member.status not in [ChatMemberStatus.MEMBER, 
                                     ChatMemberStatus.CREATOR, 
                                     ChatMemberStatus.ADMINISTRATOR]:
                return False
                
        except Exception as e:
            print(f"Ошибка при проверке подписки на канал {channel_name}: {e}")
            return False
    
    return True