from typing import Union

from pyrogram.types import InlineKeyboardButton

import config
from MARKX import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥺 𝘼𝙙𝙙 𝙢𝙚 𝙗𝙖𝙗𝙮 🥺",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="🍀 𝗛𝗲𝗹𝗽 🍀",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="🍀 𝗦𝗲𝘁𝘁𝗶𝗻𝗴𝘀 🍀", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="💖 𝗢𝘄𝗻𝗲𝗿 💖", user_id=OWNER),
            InlineKeyboardButton(
                text="🍀 𝗚𝗿𝗼𝘂𝗽 🍀", url=f"{config.SUPPORT_GROUP}"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥺 𝘼𝙙𝙙 𝙢𝙚 𝙗𝙖𝙗𝙮 🥺",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🍀 𝗛𝗲𝗹𝗽 🍀", callback_data="settings_back_helper"
            ),
            InlineKeyboardButton(text="💖 𝗢𝘄𝗻𝗲𝗿 💖", url=f"https://t.me/OpSangram"),
        ],
        [ 
            InlineKeyboardButton(text="🍀 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 🍀", url=f"{config.SUPPORT_CHANNEL}"),
            InlineKeyboardButton(text="🍀 𝗚𝗿𝗼𝘂𝗽 🍀", url=f"{config.SUPPORT_GROUP}"),
        ],
        [
            InlineKeyboardButton(text="🍀 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 2 🍀", url=f"https://t.me/WCF_officials"),
            InlineKeyboardButton(text="💖 𝗢𝘄𝗻𝗲𝗿 💖", user_id=OWNER)
        ],
     ]
    return buttons



