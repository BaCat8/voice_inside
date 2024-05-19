from termcolor import colored


def debug(msg, comment=""):
    try:
        print(colored('DEBUG', 'green'), colored(comment, 'green'), msg)
    except ImportError:
        print("Fetal error. The necessary packages are missing. Please run the installer")


def error(msg, comment=""):
    try:
        print(colored('ERROR', 'red'), colored(comment, 'red'), msg)
    except ImportError:
        print("Fetal error. The necessary packages are missing. Please run the installer")


def worning(msg, comment=""):
    try:
        print(colored('WORNING', 'yellow'), colored(comment, 'yellow'), msg)
    except ImportError:
        print("Fetal error. The necessary packages are missing. Please run the installer")


def info(msg, comment=""):
    try:
        print(colored('INFO', 'green'), colored(comment, 'green'), msg)
    except ImportError:
        print("Fetal error. The necessary packages are missing. Please run the installer")
