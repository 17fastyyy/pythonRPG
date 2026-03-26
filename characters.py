from time import sleep
from colorama import Fore, Style


class Character:
    def __init__(self, name, max_hp, hp, atk, df, df_on, xp, lvl, hability):
        self.name = name
        self.max_hp = max_hp
        self.hp = hp
        self.atk = atk
        self.df = df
        self.df_on = df_on
        self.xp = xp
        self.lvl = lvl
        self.hability = hability

    def show_stats(self):
        print(
            f"Name: {self.name} \nMax Health: {self.max_hp} \nHealth: {self.hp} \nAttack: {self.atk} \nDefense: {self.df} \nHability: {self.hability}"
        )
        return

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
        print(f"You defended yourself, you take {100 / self.df}% less damage!")
        self.df_on = True


class Villager(Character):
    def __init__(
        self,
        name,
        max_hp=20,
        hp=20,
        atk=2,
        df=2,
        df_on=False,
        xp=0,
        lvl=1,
        hability="Bonk",
    ):
        super().__init__(name, max_hp, hp, atk, df, df_on, xp, lvl, hability)


class Assasin(Character):
    def __init__(
        self,
        name,
        max_hp=15,
        hp=15,
        atk=5,
        df=3,
        df_on=False,
        xp=0,
        lvl=1,
        hability="Blade Storm",
    ):
        super().__init__(name, max_hp, hp, atk, df, df_on, xp, lvl, hability)


class Mage(Character):
    def __init__(
        self,
        name,
        max_hp=25,
        hp=25,
        atk=3,
        df=4,
        df_on=False,
        xp=0,
        lvl=1,
        hability="Lightning Blizzard",
    ):
        super().__init__(name, max_hp, hp, atk, df, df_on, xp, lvl, hability)
