from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_menu = InlineKeyboardMarkup(row_width=1, 
                                    inline_keyboard=[
                                        [
                                            InlineKeyboardButton(text="Наша группа ВК!", url="https://vk.com/publicnbc")
                                        ],
                                        [
                                            InlineKeyboardButton(text="Реклама", url="tg://user?id=1038663358")
                                        ]
                                    ])

