from ui import show_stats
from time import sleep

from mechanics import enemy_dodge_chance, check_level, clear_cmd, player_dodge_chance


def start_combat(player, enemy):

    clear_cmd()

    print(f"You found a {enemy.name}!")

    while enemy.hp > 0:
        if player.hp > 0:
            print(f"Your HP: {player.hp:.1f}", end="     ")
            print(f"Enemy HP: {enemy.hp:.1f}")
            player.df_on = False

            # players turn
            choice = int(
                input("What you wanna do? (1. Attack | 2. Defense | 3. Stats): ")
            )
            clear_cmd()

            if choice == 1:
                enemy_dodge = enemy_dodge_chance()
                if enemy_dodge > enemy.dodge:
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

            elif choice == 3:
                clear_cmd()
                show_stats(player)
                sleep(5)
                clear_cmd()
                continue

            else:
                print("Select a valid option!")
                sleep(2)
                clear_cmd()
                continue

            # enemy turn
            if enemy.hp > 0:
                player_dodge = player_dodge_chance()
                if player_dodge > 2:
                    enemy.attack(player)
                    sleep(2)
                    clear_cmd()
                else:
                    print("You dodged the attack!")
                    sleep(2)
                    clear_cmd()

        else:
            print("You have been defeated!")
            break

    if player.hp > 0:
        check_level(player, enemy)
        sleep(3)
        enemy.hp = enemy.max_hp
