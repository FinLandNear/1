# Пишу я такой бота короч
"""
Вот
Вообще описание нужно будет добавить
Вдруг кто код будет читать
"""

import telebot
import answers
import constants
import time
#import txlc


bot = telebot.TeleBot(constants.token)

print(bot.get_me())

a=42
b= "qwerty"
print(type(a), type(b))

def log(message, answer):
    print("\n -----")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1}. (id = {2}) \n Текст : \n {3}".format(message.from_user.first_name,
                                                                   message.from_user.last_name,
                                                                   str(message. from_user.id),
                                                                   message.text))
    print(answer)

@bot.message_handler(commands=['help'])
def handle_start(message):
    bot.send_message(message.chat.id, """Уже почти готово, скоро заработает!!""")

@bot.message_handler(commands=['start'])
def handle_start(message):
    answer = "Send keyboard, answers0"
    log(message, answer)
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row('/start', '/help', '/stop')
    user_markup.row('Организовать', 'Присоединиться')
    user_markup.row('Ответы на вопросы')
    bot.send_message(message.from_user.id, answers.answers0[0], reply_markup=user_markup)

@bot.message_handler(commands=['stop'])
def handle_start(message):
    answer = "Stop keyboard"
    log(message, answer)
    hide_markup = telebot.types.ReplyKeyboardRemove ()
    bot.send_message(message.from_user.id, answers.answers0[1], reply_markup=hide_markup)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "Ответы на вопросы":
        answer = "answers1"
        log(message, answer)
        counter = 0
        max_answers = len(answers.answers1) - 1
        while counter <= max_answers:
            answer = answers.answers1[counter]
            bot.send_message(message.from_user.id, answer)
            time.sleep(3)
            counter = counter + 1
    elif message.text == "Организовать":
        answer = "answers2"
        log(message, answer)
        bot.send_message(message.from_user.id, answers.answers2[0])
        time.sleep(2)
        user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup.row('Да', 'Нет', 'Подробнее')
        bot.send_message(message.from_user.id, answers.answers2[1], reply_markup=user_markup)
    elif message.text == "Да":
            answer = "answers3"
            log(message, answer)
            time.sleep(2)
            bot.send_message(message.from_user.id, answers.answers3[0])
        #вот тут надо бы написать случайное распределение всех воскресений в году, так сказать живая очередь
        #Да и вообще тут будет куча кода, реплик, так еще и их все записывать нужно в какоё-то лог
            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row('1' , '/help', '/stop')
            user_markup.row('/start', '/help', '/stop')
            bot.send_message(message.from_user.id, answers.answers3[1], reply_markup=user_markup)








    elif message.text == "Нет":
            answer = "answers4"
            log(message, answer)
            time.sleep(2)
            bot.send_message(message.from_user.id, answers.answers4[0])
            time.sleep(2)
            hide_markup = telebot.types.ReplyKeyboardRemove()
            bot.send_message(message.from_user.id, answers.answers4[1], reply_markup=hide_markup)

bot.polling(none_stop=True, interval=0)



