from logger import debug
import environs
import logger
# import telebot
#
#
env = environs.Env()
env.read_env()
#
# bot = telebot.TeleBot(env('BOT_TOKEN'))


def say(*msg):
    try:
        for i in msg:
            if env('DEBUG') == 'true':
                debug('say function:')
            if env.int('MODE') == 1:  # Исправить, если можно
                print(i)
            # elif env.int('MODE') == 2:
            #     bot_say(i)

    except AttributeError:
        logger.error("Невозможен вывод", "Возможно, отсутствует или некорректна переменная 'mode' в "
                                         "файле конфигурации")


# def bot_say(i):
#     bot.send_message(user_id, i)

def question_int(msg):
    say(msg)
    a = int(input())
    return a
#
#
#
#
#
#
#
# @bot.message_handler(commands=['start'])
# def bot_start(msg):
#     bot.send_message(msg.chat.id, 'бот запущен')


# bot.polling(none_stop=True)
