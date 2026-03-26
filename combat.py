import problem
from time import sleep

from mechanics import get_dodge_chance, check_level, clear_cmd


def start_combat(player, enemy):

    print(f"You found a {enemy.name}!")

    while enemy.hp > 0:
        if player.hp > 0:
            print(f"Your HP: {player.hp}", end="     ")
            print(f"Enemy HP: {enemy.hp}")

            # players turn
            choice = int(input("What you wanna do? (1. Attack | 2. Defense): "))
            clear_cmd()

            if choice == 1:
                dodge_num = get_dodge_chance()
                if dodge_num > enemy.dodge:
                    player.attack(enemy)
                    sleep(3)
                    clear_cmd()

                else:
                    print("Oops! You missed your attack.")
                    sleep(2)
                    clear_cmd()

            elif choice == 2:
                player.use_defense()
                sleep(2)
                clear_cmd()

            else:
                print("Select a valid option!")
                sleep(2)
                clear_cmd()
                continue

            enemy.attack()
            player.hp -= enemy.atk
            sleep(2)
            clear_cmd()

        else:
            print("You have been defeated!")
            break

    if player.hp > 0:
        check_level(player, enemy)
