import logger
import environs
from os import system
from sys import platform
from termcolor import colored

env = environs.Env()
env.read_env()


colors = ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white', 'light_grey', 'dark_grey', 'light_red',
          'light_green', 'light_yellow', 'light_blue', 'light_magenta', 'light_cyan']


def clear():
    if platform == 'linux' or platform == 'linux':
        system('clear')
    elif platform == 'win32':
        system('cls')
    elif platform == "darwin":
        system('cls')


def say(color, *msg):
    try:
        for i in msg:
            if env('DEBUG') == 'true':
                logger.debug('say function:')
            if env.int('MODE') == 1:
                if color in colors:
                    print(colored(i, color))
                else:
                    logger.error("Ошибка вывода")
    except AttributeError:
        logger.error("Невозможен вывод", "Возможно, отсутствует или некорректна переменная 'mode' в "
                                         "файле конфигурации")


def question_int(msg):
    say(msg)
    a = int(input())
    return a
