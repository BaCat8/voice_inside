from logger import debug
import environs
import logger
from os import system
from sys import platform

env = environs.Env()
env.read_env()


def clear():
    if platform == 'linux' or platform == 'linux':
        system('clear')
    elif platform == 'win32':
        system('cls')
    elif platform == "darwin":
        system('cls')


def say(*msg):
    try:
        for i in msg:
            if env('DEBUG') == 'true':
                debug('say function:')
            if env.int('MODE') == 1:
                print(i)
    except AttributeError:
        logger.error("Невозможен вывод", "Возможно, отсутствует или некорректна переменная 'mode' в "
                                         "файле конфигурации")


def question_int(msg):
    say(msg)
    a = int(input())
    return a
