from typing import Union
from pyrogram.types import InlineKeyboardButton
from config import SUPPORT_CHANNEL, SUPPORT_GROUP
from YukkiMusic import app


def start_pannel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="➕ Add me to Group", url=f"https://t.me/{app.username}?startgroup=true"
            ),
        ],
        [
            InlineKeyboardButton(text="📢 Channel", url="https://t.me/Teamfoxbots"),
            InlineKeyboardButton(text="💬 Support", url="https://t.me/Teamfoxbots"),
        ],
        [
            InlineKeyboardButton(
                text="❓ How to Use", url=f"https://t.me/{app.username}?start=help"
            ),
            InlineKeyboardButton(text="⚙️ Settings", callback_data="settings_helper"),
        ],
        [
            InlineKeyboardButton(text="🌐 Language", callback_data="LG"),
        ],
    ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="➕ Add me to Group", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
            ),
        ],
        [
            InlineKeyboardButton(text="📢 Channel", url="https://t.me/Teamfoxbots"),
            InlineKeyboardButton(text="💬 Support", url="https://t.me/Teamfoxbots"),
        ],
        [
            InlineKeyboardButton(text="❓ How to Use", url=f"https://t.me/{BOT_USERNAME}?start=help"),
            InlineKeyboardButton(text="⚙️ Settings", callback_data="settings_helper"),
        ],
        [
            InlineKeyboardButton(text="🌐 Language", callback_data="LG"),
        ],
    ]
    return buttons


def alive_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="➕ Add me to Group", url=f"https://t.me/{app.username}?startgroup=true"
            ),
        ],
        [
            InlineKeyboardButton(text="📢 Channel", url="https://t.me/Teamfoxbots"),
            InlineKeyboardButton(text="💬 Support", url="https://t.me/Teamfoxbots"),
        ],
    ]
    return buttons
