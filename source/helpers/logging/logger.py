from helpers.logging.log_type import LogType
from helpers.logging.bcolors import bcolors
from datetime import datetime

# TODO use print time method
class Logger:
    def log_warning(msg):
        now = datetime.now()
        cur_time = now.strftime("%H:%M:%S")
        print(f"{cur_time} {bcolors.WARNING}WARNING: {msg}", bcolors.ENDC)

    def log_info(msg):
        now = datetime.now()
        cur_time = now.strftime("%H:%M:%S")
        print(f"{cur_time} {bcolors.OKBLUE}INFO: {msg}", bcolors.ENDC)

    def log_error(msg):
        now = datetime.now()
        cur_time = now.strftime("%H:%M:%S")
        print(f"{cur_time} {bcolors.FAIL}ERROR: {msg}", bcolors.ENDC)

    def log_game_event(msg):
        now = datetime.now()
        cur_time = now.strftime("%H:%M:%S")
        print(f"{cur_time} {bcolors.OKGREEN}EVENT: {msg}", bcolors.ENDC)

    def log(msg, logtype):
        if logtype == LogType.INFO:
            print(f"{bcolors.OKBLUE}INFO: {msg}", bcolors.ENDC)
        elif logtype == LogType.WARNING:
            print(f"{bcolors.WARNING}WARNING: {msg}", bcolors.ENDC)
        elif logtype == LogType.ERROR:
            print(f"{bcolors.FAIL}ERROR: {msg}", bcolors.ENDC)

    def __print_time():
        now = datetime.now()
        cur_time = now.strftime("%H:%M:%S")

        return cur_time
