from mechanics import crit_atk
from colorama import Fore, Style
from time import sleep


class Enemy:
    def __init__(self, name, max_hp, hp, atk, atk_name, dodge, crit_chance, xp_drop):
        self.name = name
        self.max_hp = max_hp
        self.hp = hp
        self.atk = atk
        self.atk_name = atk_name
        self.dodge = dodge
        self.crit_chance = crit_chance
        self.xp_drop = xp_drop

    def attack(self, player):
        print(f"{self.name} used {self.atk_name}!")
        sleep(2)
        if player.df_on:
            damage = self.atk / 10 * player.df
            print(
                f"{self.name}'s attack deals {Fore.RED}{round(damage, 1)}{Style.RESET_ALL} damage."
            )
            player.hp -= damage

        elif crit_atk(self):
            print(
                f"{self.name}'s attack is critic! It deals {Fore.RED}{self.atk * 2}{Style.RESET_ALL} damage."
            )
            player.hp -= self.atk * 2

        else:
            print(
                f"{self.name}'s attack deals {Fore.RED}{self.atk}{Style.RESET_ALL} damage."
            )
            player.hp -= self.atk


class Slime(Enemy):
    def __init__(
        self,
        name="Slime",
        max_hp=20,
        hp=20,
        atk=2,
        atk_name="Blob",
        dodge=5,
        crit_chance=1,
        xp_drop=60,
    ):
        super().__init__(name, max_hp, hp, atk, atk_name, dodge, crit_chance, xp_drop)
