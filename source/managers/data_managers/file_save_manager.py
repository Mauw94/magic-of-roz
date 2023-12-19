from pathlib import Path
import os
import json
import uuid
from core.constants import GAME_FOLDER, SAVE_FILE, SAVE_FILE_EXTENSION
from helpers.logging.logger import Logger


def get_documents_path() -> str:
    home_path = Path(os.path.expanduser("~"))
    documents_path = home_path / "Documents"
    documents_path_str = str(documents_path)

    return documents_path_str


def save_new_character_info(char_info: dict) -> None:
    u_id = str(uuid.uuid1())
    game_folder = _make_game_folder_dir_if_not_exists()
    file_path = os.path.join(game_folder, u_id + SAVE_FILE_EXTENSION)

    with open(file_path, "w") as file:
        json.dump(char_info, file, indent=4)


def load_all_saves() -> list:
    game_folder_path = Path(_make_game_folder_dir_if_not_exists())
    files = [f for f in game_folder_path.iterdir() if f.is_file()]
    all_chars = []

    for file in files:
        with open(file, "r") as f:
            char: dict = json.load(f)
            all_chars.append(char)

    return all_chars


def _make_game_folder_dir_if_not_exists() -> str:
    docs_folder = get_documents_path()
    game_path = Path(docs_folder + "/" + GAME_FOLDER)
    game_path.mkdir(parents=True, exist_ok=True)
    Logger.log_info("Game directory successfully created or initialized.")

    return str(game_path)
