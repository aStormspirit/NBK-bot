from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import emoji


ikb_menu = InlineKeyboardMarkup(row_width=2, 
                                    inline_keyboard=[
                                        [
                                            InlineKeyboardButton(text="Наш ВК!" + emoji.emojize(":star:"), url="https://vk.com/publicnbc"),
                                            InlineKeyboardButton(text="Наш ТГ канал" + emoji.emojize(":star:"), url="https://t.me/newbusinesscomunity")
                                        ],
                                        [
                                            InlineKeyboardButton(text="Реклама", url="tg://user?id=5805044876")
                                        ]
                                    ])

