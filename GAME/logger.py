from sys import exit

try:
    from termcolor import colored
    import environs
except ImportError or ModuleNotFoundError:
    print("Fetal error. The necessary packages are missing. Please run the installer")
    exit()

env = environs.Env()
env.read_env()


def debug(msg, comment=""):  # Информация с точки зрения кода
    if env('debug') == 'true':
        print(colored('DEBUG', 'green'), colored(msg, 'green'), comment)


def error(msg, comment=""):  # Критическая ошибки в работе программы
    print(colored('ERROR', 'red'), colored(msg, 'red'), comment)
    exit()


def worning(msg, comment=""):  # Ещё не ошибка, но происходит что-то странное: сервер не ответил
    if env('debug') == 'true':
        print(colored('WORNING', 'yellow'), colored(msg, 'yellow'), comment)


def info(msg, comment=""):  # Информация о разовых ситуациях, например: начали работу
    if env('debug') == 'true':
        print(colored('INFO', 'green'), colored(msg, 'green'), comment)
