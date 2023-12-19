from pathlib import Path
import os
import json
from core.constants import GAME_FOLDER, SAVE_FILE
from helpers.logging.logger import Logger

def get_documents_path() -> str:
    home_path = Path(os.path.expanduser("~"))
    documents_path = home_path / "Documents"
    documents_path_str = str(documents_path)
    print(f"Path to docs folder: {documents_path_str}")
    
    return documents_path_str
    
def save_character_info(char_info: dict) -> None:
    # TODO: save file name should have unique id per character
    game_folder = _make_game_folder_dir_if_not_exists()
    file_path = os.path.join(game_folder, SAVE_FILE)
    
    with open(file_path, 'w') as file:
        json.dump(char_info, file, indent=4)

def load_character_info() -> dict:
    game_folder = _make_game_folder_dir_if_not_exists()
    file_path = os.path.join(game_folder, SAVE_FILE)
    
    with open(file_path, 'r') as file:
        char_info: dict = json.load(file)
    print(char_info)
    
    return char_info

def _make_game_folder_dir_if_not_exists() -> str:
    docs_folder = get_documents_path()
    game_path = Path(docs_folder + "/" + GAME_FOLDER)
    game_path.mkdir(parents=True, exist_ok=True)
    Logger.log_info("Game directory successfully created or initialized.")
    
    return str(game_path)
    