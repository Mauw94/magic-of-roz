import arcade

class TextureLoader:
    def load_texture_pair(self, filename): # Load texture facing left and facing right
        return [
            arcade.load_texture(filename),
            arcade.load_texture(filename, flipped_horizontally=True)
        ]