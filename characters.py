from time import sleep
from colorama import Fore, Style


class Character:
    def __init__(
        self, name, max_hp, hp, atk, df, df_on, xp, lvl, hability, crit_chance
    ):
        self.name = name
        self.max_hp = float(max_hp)
        self.hp = float(hp)
        self.atk = atk
        self.df = df
        self.df_on = df_on
        self.xp = xp
        self.lvl = lvl
        self.hability = hability
        self.crit_chance = crit_chance

    def attack(self, enemy):
        print("You attack!")
        sleep(2)
        print(f"Your attack did {Fore.RED}{self.atk}{Style.RESET_ALL} damage.")
        enemy.hp -= self.atk

    def use_hability(self):
        print(
            f"{self.name} used {self.hability}. It did {self.atk * 1.5} points of damage!"
        )

    def use_defense(self):
        print(
            f"You defend yourself, you take {round(100 / self.df, 1)}% less damage on the next attack!"
        )
        self.df_on = True


class Villager(Character):
    def __init__(
        self,
        name,
        max_hp=20,
        hp=20,
        atk=5,
        df=2,
        df_on=False,
        xp=0,
        lvl=1,
        hability="Bonk",
        crit_chance=2,
    ):
        super().__init__(
            name, max_hp, hp, atk, df, df_on, xp, lvl, hability, crit_chance
        )


class Assasin(Character):
    def __init__(
        self,
        name,
        max_hp=15,
        hp=15,
        atk=8,
        df=3,
        df_on=False,
        xp=0,
        lvl=1,
        hability="Blade Storm",
        crit_chance=2,
    ):
        super().__init__(
            name, max_hp, hp, atk, df, df_on, xp, lvl, hability, crit_chance
        )


class Mage(Character):
    def __init__(
        self,
        name,
        max_hp=25,
        hp=25,
        atk=6,
        df=4,
        df_on=False,
        xp=0,
        lvl=1,
        hability="Lightning Blizzard",
        crit_chance=2,
    ):
        super().__init__(
            name, max_hp, hp, atk, df, df_on, xp, lvl, hability, crit_chance
        )
