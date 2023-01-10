from helpers.logging.bcolors import bcolors
from datetime import datetime
# import traceback
# import sys
# traceback.print_stack(file=sys.stdout)
# might needs this later


class Logger:
    loggingEnabled = True

    def log_warning(msg):
        log = f"{Logger.__print_time()} {bcolors.WARNING}WARNING: {msg}"
        print(log, bcolors.ENDC)
        Logger.__log_to_file(log)

    def log_info(msg):
        log = f"{Logger.__print_time()} {bcolors.OKBLUE}INFO: {msg}"
        print(log, bcolors.ENDC)
        Logger.__log_to_file(log)

    def log_error(msg):
        log = f"{Logger.__print_time()} {bcolors.FAIL}ERROR: {msg}"
        print(log, bcolors.ENDC)
        Logger.__log_to_file(log)

    def log_game_event(msg):
        log = f"{Logger.__print_time()} {bcolors.OKGREEN}EVENT: {msg}"
        print(log, bcolors.ENDC)
        Logger.__log_to_file(log)

    def log_object_creation(msg, creationIn):
        log = f"{Logger.__print_time()} {bcolors.OKCYAN}OBJECT_CREATION: {msg} IN: {creationIn}"
        print(log, bcolors.ENDC)
        Logger.__log_to_file(log)

    def __print_time():
        now = datetime.now()
        cur_time = now.strftime("%H:%M:%S")

        return cur_time

    def __log_to_file(msg: str):
        if Logger.loggingEnabled:
            f = open("logs.txt", "a")
            f.write(msg.replace(" ", "") + "\n")
            f.flush()
            f.close()
