import random
import os
import subprocess

from colorama import Fore, Style


def get_dodge_chance():
    return random.randint(0, 100)


def clear_cmd():
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)


def check_level(player, enemy):

    player.xp += enemy.xp_drop

    if player.xp >= 100:
        print("You have leveled up!")
        player.lvl += 1

        player.hp = player.max_hp
    else:
        print(f"You gained {Fore.GREEN}{enemy.xp_drop}{Style.RESET_ALL} xp!")
