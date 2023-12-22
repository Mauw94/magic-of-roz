from helpers.logging.bcolors import bcolors
from datetime import datetime

# import traceback
# import sys
# traceback.print_stack(file=sys.stdout)
# might needs this later


class Logger:
    loggingEnabled = True

    # log warning
    def log_warning(msg) -> None:
        log = f"{Logger.__print_time()} {bcolors.WARNING}WARNING: {msg}"
        print(log, bcolors.ENDC)
        Logger.__log_to_file(log)

    # log info
    def log_info(msg) -> None:
        log = f"{Logger.__print_time()} {bcolors.OKBLUE}INFO: {msg}"
        print(log, bcolors.ENDC)
        Logger.__log_to_file(log)

    def log_debug(msg) -> None:
        log = f"{Logger.__print_time()} {bcolors.UNDERLINE}DEBUG: {msg}"
        print(log, bcolors.ENDC)
        Logger.__log_to_file(log)

    # log error
    def log_error(msg) -> None:
        log = f"{Logger.__print_time()} {bcolors.FAIL}ERROR: {msg}"
        print(log, bcolors.ENDC)
        Logger.__log_to_file(log)

    # log event
    def log_game_event(msg) -> None:
        log = f"{Logger.__print_time()} {bcolors.OKGREEN}EVENT: {msg}"
        print(log, bcolors.ENDC)
        Logger.__log_to_file(log)

    # msg: class/object which will be created
    # creationIn: class/object in which the class/object will be created
    def log_object_creation(msg, creationIn) -> None:
        log = f"{Logger.__print_time()} {bcolors.OKCYAN}OBJECT_CREATION: {msg} IN: {creationIn}"
        print(log, bcolors.ENDC)
        Logger.__log_to_file(log)

    def __print_time() -> str:
        now = datetime.now()
        cur_time = now.strftime("%H:%M:%S")

        return cur_time

    def __log_to_file(msg: str) -> None:
        if Logger.loggingEnabled:
            f = open("logs.txt", "a")
            f.write(msg.replace(" ", "") + "\n")
            f.flush()
            f.close()
