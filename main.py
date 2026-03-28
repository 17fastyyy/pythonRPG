from mechanics import clear_cmd
from time import sleep

from characters import Assasin, Mage, Villager
from enemies import Slime
from combat import start_combat


classes = {
    1: Villager,
    2: Assasin,
    3: Mage,
}

if __name__ == "__main__":
    while True:
        print("Welcome to Pia's Dungeon.")
        role = int(
            input("Please select your class (1. Villager, 2. Assasin, 3. Mage): ")
        )

        print()

        print(f"You've selected the class {classes[role].__name__}.")
        sleep(2)
        print()

        name: str = input("Select a name: ")

        print()

        input(f"Welcome {name}, are you prepared to start? (y/y): ")

        player = classes[role](name)

        slime = Slime()

        sleep(2)
        clear_cmd()
        start_combat(player, slime)
        start_combat(player, slime)
        start_combat(player, slime)

        # player.show_stats()

        break
