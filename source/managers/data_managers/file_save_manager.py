from pathlib import Path
import os
import json
from core.constants import GAME_FOLDER, SAVE_FILE, SAVE_FILE_EXTENSION
from helpers.logging.logger import Logger


def get_documents_path() -> str:
    home_path = Path(os.path.expanduser("~"))
    documents_path = home_path / "Documents"
    documents_path_str = str(documents_path)

    return documents_path_str


def save_new_character_info(char_info: dict) -> None:
    Logger.log_info("Saving..")
    game_folder = _make_game_folder_dir_if_not_exists()
    file_path = os.path.join(game_folder, char_info["u_id"] + SAVE_FILE_EXTENSION)

    with open(file_path, "w") as file:
        json.dump(char_info, file, indent=4)
        file.flush()
        file.close()


def load_all_saves() -> list:
    Logger.log_info("Loading all save files.")
    game_folder_path = Path(_make_game_folder_dir_if_not_exists())
    file_paths = [f for f in game_folder_path.iterdir() if f.is_file()]
    all_chars = []

    for path in file_paths:
        with open(path, "r") as file:
            char: dict = json.load(file)
            all_chars.append(char)
            file.close()

    Logger.log_info("Save files successfully loaded")

    return all_chars


def save_character(u_id: str, char_info: dict) -> None:
    Logger.log_game_event("Saving character info")
    game_folder = _make_game_folder_dir_if_not_exists()
    file_path = os.path.join(game_folder, u_id + SAVE_FILE_EXTENSION)

    with open(file_path, "w") as file:
        json.dump(char_info, file, indent=4)
        file.flush()
        file.close()


def load_character_save(u_id: str) -> dict:
    Logger.log_game_event("Loading character info")
    game_folder = _make_game_folder_dir_if_not_exists()
    file_path = os.path.join(game_folder, u_id + SAVE_FILE_EXTENSION)
    char_info: dict = {}
    with open(file_path, "r") as file:
        char_info = json.load(file)
        file.close()

    return char_info


def _make_game_folder_dir_if_not_exists() -> str:
    docs_folder = get_documents_path()
    game_path = Path(docs_folder + "/" + GAME_FOLDER)
    game_path.mkdir(parents=True, exist_ok=True)

    return str(game_path)
