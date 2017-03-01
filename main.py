# Пишу я такой бота короч
"""
Вот
Вообще описание нужно будет добавить
Вдруг кто код будет читать
"""

import telebot
import constants

bot = telebot.TeleBot(constants.token)

print(bot.get_me())

a=42
b= "qwerty"
print(type(a), type(b))

def log(message, answer):
    print("\n -----")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1}. (id = {2}) \n Текст - {3}".format(message.from_user.first_name,
                                                                   message.from_user.last_name,
                                                                   str(message. from_user.id),
                                                                   message.text))
    print(answer)

@bot.message_handler(commands=['help'])
def handle_start(message):
    bot.send_message(message.chat.id, """Уже почти готово, скоро заработает!!""")

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row('/start', '/help', '/stop')
    user_markup.row('Организовать', 'Присоединиться')
    user_markup.row('Ответы на вопросы')
    bot.send_message(message.from_user.id, 'Приветствую, выберите что Вам сейчас интересно', reply_markup=user_markup)

@bot.message_handler(commands=['stop'])
def handle_start(message):
    hide_markup = telebot.types.ReplyKeyboardRemove ()
    bot.send_message(message.from_user.id, '..', reply_markup=hide_markup)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "Ответы на вопросы":
        bot.send_message(message.from_user.id, """\r
        Да - да, смело спрашивайте, о чем угодно!')






bot.polling(none_stop=True, interval=0)



