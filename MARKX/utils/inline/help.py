from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from MARKX import app
from config import SUPPORT_GROUP


def help_pannel(_, START: Union[bool, int] = None):
    first = [
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        )
    ]
    second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data=f"settingsback_helper",
        ),
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="💖 𝗔𝗱𝗺𝗶𝗻 💖",
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text="💖 𝗔𝘂𝘁𝗵 💖",
                    callback_data="help_callback hb2",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="💖 𝗕𝗹𝗮𝗰𝗸𝗹𝗶𝘀𝘁 💖",
                    callback_data="help_callback hb3",
                ),
                InlineKeyboardButton(
                    text="💖 Broadcast 💖",
                    callback_data="help_callback hb4",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="💖 𝗚𝗯𝗮𝗻 💖",
                    callback_data="help_callback hb12",
                ),
                InlineKeyboardButton(
                    text="💖 𝗟𝘆𝗿𝗶𝗰𝘀 💖",
                    callback_data="help_callback hb5",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="💖 𝗽𝗶𝗻𝗴 💖",
                    callback_data="help_callback hb7",
                ),
                InlineKeyboardButton(
                    text="💖 𝗣𝗹𝗮𝘆 💖",
                    callback_data="help_callback hb8",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="💖 𝗣𝗹𝗮𝘆𝗹𝗶𝘀𝘁 💖",
                    callback_data="help_callback hb6",
                ),
                InlineKeyboardButton(
                    text="💖 𝗩𝗶𝗱𝗲𝗼𝗰𝗵𝗮𝘁𝘀💖",
                    callback_data="help_callback hb10",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="💖 𝗦𝘁𝗮𝗿𝘁 💖",
                    callback_data="help_callback hb11",
                ),
                InlineKeyboardButton(
                    text="💖 Sudo 💖",
                    callback_data="help_callback hb9",
                ),
            ],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"settings_back_helper",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"], callback_data=f"close"
                ),
                InlineKeyboardButton(
                    text=" sᴜᴩᴩᴏʀᴛ ", url=f"{SUPPORT_GROUP}"
                ),
            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"],
                url=f"https://t.me/{app.username}?start=help",
            ),
        ],
    ]
    return buttons
