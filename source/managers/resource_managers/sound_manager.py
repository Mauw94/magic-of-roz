import arcade

from helpers.static_data import PREFERRED_SOUND_VOLUME


class SoundManager:
    def __init__(self, with_preferred_volume: bool = False):
        if with_preferred_volume:
            self.set_preferred_sound_volume()
        else:
            self._volume = 1

        self.current_music: arcade.Sound = None

    def set_preferred_sound_volume(self) -> None:
        self._volume = PREFERRED_SOUND_VOLUME

    def set_custom_voume(self, volume: int) -> None:
        self._volume = volume

    def get_volume(self) -> int:
        return self._volume

    def play_sound(self, sound: arcade.Sound):
        arcade.play_sound(sound, volume=self._volume)

    def play_music(self, music: arcade.Sound, looping: bool = False) -> None:
        music.play(volume=self._volume, loop=looping)
        self.current_music = music
