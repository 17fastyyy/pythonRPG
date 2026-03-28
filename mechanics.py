import random
import os
import subprocess

from colorama import Fore, Style


def enemy_dodge_chance():
    return random.randint(0, 100)


def player_dodge_chance():
    return random.randint(0, 100)


def clear_cmd():
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)


def lvl_up(player):
    print("You have leveled up!")
    player.lvl += 1
    player.xp = 0

    player.max_hp += 5
    player.atk += 3
    player.df += 2
    player.hp = player.max_hp


def check_level(player, enemy):

    player.xp += enemy.xp_drop

    if player.lvl <= 5 and player.xp >= 100:
        lvl_up(player)

    elif player.lvl > 5 and player.lvl <= 10 and player.xp >= 200:
        lvl_up(player)

    elif player.lvl > 10 and player.lvl <= 15 and player.xp >= 400:
        lvl_up(player)

    elif player.lvl > 15 and player.lvl <= 20 and player.xp >= 600:
        lvl_up(player)

    elif player.lvl > 20 and player.xp >= 700:
        lvl_up(player)

    else:
        print(f"You gained {Fore.GREEN}{enemy.xp_drop}{Style.RESET_ALL} xp!")


def crit_atk(entity):
    if entity.crit_chance > random.randint(0, 100):
        return True
