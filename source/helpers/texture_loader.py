from helpers.logging.logger import Logger
import arcade


class TextureLoader:
    def __init__(self):
        Logger.log_object_creation("TextureLoader")

    # Load texture facing left and facing right
    def load_texture_pair(self, filename):
        return [
            arcade.load_texture(filename),
            arcade.load_texture(filename, flipped_horizontally=True)
        ]
