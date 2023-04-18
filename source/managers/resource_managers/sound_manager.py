import arcade


class SoundManager:
    def __init__(self):
        self._volume = 1

    def set_preferred_sound_volume(self, v: int) -> None:
        self._volume = v

    def get_volume(self) -> int:
        return self._volume
    
    def play_sound(self, sound: arcade.Sound):
        arcade.play_sound(sound, volume=self._volume)
