import data.config as config
import logging
import emoji
#from datetime import datetime
#from datetime import timedelta
from keyboard.keyboard import ikb_menu

from filters.filters import IsAdminFilter
from aiogram import Bot, Dispatcher, executor, types

#logs
logging.basicConfig(level=logging.INFO)

# bot init
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)
dp.filters_factory.bind(IsAdminFilter)

#ban commands (admin only)
@dp.message_handler(is_admin=True, commands=['ban'], commands_prefix="!/")
async def cmd_ban(message: types.Message):
    """
    This handler will be called when user answer !ban, and baned him
    """
    if not message.reply_to_message:
        await message.reply('Эта команда должна быть ответом на сообщение')

    await message.bot.delete_message(chat_id=config.GROUP_ID, message_id=message.message_id)
    await message.bot.kick_chat_member(chat_id=config.GROUP_ID, user_id=message.reply_to_message.from_user.id)
    await message.reply_to_message.reply("Пользователь забанен!")

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")

#help command
@dp.message_handler(commands=['help'], commands_prefix="!/")
async def cmd_help(message: types.Message):
    """
    This handler will be called when user answer !help, and baned list all rules groups
    """
    await message.answer(f"""{emoji.emojize(":fire:")*3}<b>Правила чата</b>{emoji.emojize(":fire:")*3}\n
    {emoji.emojize(":tiger:")}Пишите о себе кратко , вид деятельности либо уровень компетенции и в какой сфере
     {emoji.emojize(":hamster:")} Пару сообщений достаточно , многие участники чата успешные бизнесмены и эксперты , ваше сообщение обязательно увидят давайте уважать друг друга 
     {emoji.emojize(":frog:")} Разрешено и приветствуется хорошее настроение и позитивный настрой . 
     {emoji.emojize(":monkey_face:")} Запрещены мат и оскорбления участников чата , скрытая реклама и политические и религиозные обсуждения 
     {emoji.emojize(":pig_nose:")} Реклама только после согласования с администрацией Нбк """, parse_mode='html', reply_markup=ikb_menu)

#echo
@dp.message_handler()
async def filter_message(message: types.Message):
    if "блядь" in message.text:
        await message.delete()

#run longpooling
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


##########


#@dp.message_handler(is_admin=True, commands=['mute'], commands_prefix="!/")
#async def cmd_ban(message: types.Message):
#    if not message.reply_to_message:
#        await message.reply(f'')
#        return
#
#    name1 = message.from_user.get_mention()
#    logging.info('Hello')
#    try:
#        muteint = int(message.text.split()[1])
#        comment = " ".join(message.text.split()[2:])
#    except IndexError:
#        await message.reply('Не хватает аргументов!\nПример:\n`!mute 1 причина`')
#        return
#
#    dt = datetime.now() + timedelta(hours=muteint)
#    timestamp = dt.timestamp()
#    logging.info(dt, timestamp)
#
#    await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_send_messages=False)
#    #await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(False), until_date = timestamp)
#   await message.reply(f' | <b>Пользователь получает мут!</b> {name1}\n | <b>Нарушитель:</b> {message.reply_to_message.from_user.first_name}\n⏰ | <b>Срок наказания:</b> {muteint} Ч\n | <b>Причина:</b> {comment}',  parse_mode='html')

#help command
#@dp.message_handler(commands=['rules'], commands_prefix="!/")
#async def cmd_rules(message: types.Message):
#    await message.answer("Правила чата\n1)Не употреблять нецензурную лексику\n2)Не разжигать вражды\n3)Вести себя культурно")


#удаление сообщения о приветсвии
#@dp.message_handler(content_types=["new_chat_members"])
#async def on_user_join(message: types.Message):
#    await message.delete()
#    await message.answer(f"Добро пожаловать {message.new_chat_members[0].first_name} {message.new_chat_members[0].last_name}!\nРасскажите о себе, как вы нашли эту группу.\nЧтобы избежать конфилктов, ознакомтесь с правилами чата !rules")

