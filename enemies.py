class Enemy:
    def __init__(self, name, hp, atk, atk_name, dodge, xp_drop):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.atk_name = atk_name
        self.dodge = dodge
        self.xp_drop = xp_drop

    def attack(self):
        print(f"{self.name} used {self.atk_name}!")


class Slime(Enemy):
    def __init__(
        self, name="Slime", hp=20, atk=2, atk_name="Blob", dodge=5, xp_drop=10
    ):
        super().__init__(name, hp, atk, atk_name, dodge, xp_drop)
