class ResourceManager:
    def __init__(self):
        self.mana_regen_interval = 0
        self._mana_regen_timer = 0
        self._max_mana = 0
        self._max_hp = 0

        self.mana_is_full = True
        self.hp_is_full = True

    def set_max_mana(self, m: int) -> None:
        self._max_mana = m
        self.cur_mana = self._max_mana

    def set_mana_regen_values(self, regen_interval) -> None:
        self.mana_regen_interval = regen_interval

    def get_cur_mana(self) -> int:
        return self.cur_mana

    def regen_mana(self) -> None:
        if self.cur_mana >= self._max_mana:
            self.mana_is_full = True
            return
        else:
            self.mana_is_full = False

        self._mana_regen_timer += 1
        if self._mana_regen_timer == self.mana_regen_interval:
            self.cur_mana += 1
            self._mana_regen_timer = 0
