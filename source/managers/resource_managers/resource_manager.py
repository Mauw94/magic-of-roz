class ResourceManager:
    def __init__(self):
        self.cur_mana = 0
        self.cur_hp = 0

        self._mana_regen_interval = 0
        self._mana_regen_timer = 0
        self._max_mana = 0

        self._hp_regen_interval = 0
        self._hp_regen_timer = 0
        self._max_hp = 0

        self.mana_is_full = True
        self.hp_is_full = True

    def set_max_hp(self, hp: int) -> None:
        self._max_hp = hp
        self.cur_hp = self._max_hp

    def set_hp_regen_values(self, regen_interval) -> None:
        self._hp_regen_interval = regen_interval

    def get_cur_hp(self) -> int:
        return self.cur_hp

    def regen_hp(self) -> None:
        if self.cur_hp >= self._max_hp:
            self.hp_is_full = True
            return
        else:
            self.hp_is_full = False

        self._hp_regen_timer += 1
        if self._hp_regen_timer == self._hp_regen_interval:
            self.cur_hp += 1
            self._hp_regen_timer = 0

    def set_max_mana(self, m: int) -> None:
        self._max_mana = m
        self.cur_mana = self._max_mana

    def set_mana_regen_values(self, regen_interval) -> None:
        self._mana_regen_interval = regen_interval

    def get_cur_mana(self) -> int:
        return self.cur_mana

    def regen_mana(self) -> None:
        if self.cur_mana >= self._max_mana:
            self.mana_is_full = True
            return
        else:
            self.mana_is_full = False

        self._mana_regen_timer += 1
        if self._mana_regen_timer == self._mana_regen_interval:
            self.cur_mana += 1
            self._mana_regen_timer = 0
