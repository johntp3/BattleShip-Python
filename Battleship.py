from Player import *
import random as r

row_value = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10}


def greeting():
    print("----------------------------------BattleShip----------------------------------")
    print("Welcome! In this game you will attempt to sink all of the other player's ship ")
    print("before they do. First, you must decide where to put your ships!\n")


p1 = Player(9, 10)
p2 = Player(9, 10)
players = [p1, p2]
p_order = 0
greeting()

# ship placement
while p_order < 2:
    print("Player #" + str(p_order + 1) + ", it is your turn! Other player, turn around.\n")
    while not players[p_order].finish():
        print(players[p_order].check)
        available_ships = "Available ships: "
        for x in range(5):
            if not players[p_order].placed_float[x]:
                available_ships += "| " + str(ship_names[x]) + " |"
        print(available_ships)
        ship_name = input("Type one of the available ships or \"rm\" to remove a ship: ").lower()
        if ship_name == "rm":
            print("You are in removal mode.")
            removable_ships = "Ships on board: "
            for x in range(5):
                if players[p_order].placed_float[x]:
                    removable_ships += "| " + str(ship_names[x]) + " |"
            print(removable_ships)
            status = input("Type the name of a ship on the board or \"q\" to quit: ").lower()
            if status == "q":
                continue
            try:
                players[p_order].edit_ship(status, "", -1, -1, 0)
                continue
            except KeyError:
                print("This ship does not exist. Enter removal mode to try again.")
                continue

        while True:
            print("You are in placement mode for the ship " + ship_name + ".")
            orientation = input("Pick an orientation or type \"q\" to quit (V for Vert. and H for Horiz.): ").lower()
            if orientation == "q":
                break
            ship_position = input("Type pos. of the top most point (v orientation) or left most point (h orientation)"
                                  + " for the current ship in this format (<row> <column>): ").upper().split()
            try:
                ship_row = int(ship_position[0])
                ship_col = row_value[ship_position[1]]
                if not (1 <= ship_row <= 9):
                    raise IndexError()
            except (ValueError, KeyError, IndexError):
                print("Invalid input for row and column. " +
                      "Use numerals 1-9 for row and letter A-J for column separated by a space.")
                continue
            if players[p_order].can_edit_check_board(ship_name, orientation, ship_row, ship_col):
                players[p_order].check.edit_board(ship_name, orientation, ship_row, ship_col, 1)
                players[p_order].edit_ship(ship_name, orientation, ship_row, ship_col, 1)
                break
            print("Incorrect input(s). Try again!")
    p_order += 1
    for x in range(10):
        print("ANTI-CHEATING SPAM! ANTI_CHEATING SPAM! ANTI-CHEATING SPAM!\n")

# Let the games begin!
p_order = r.randint(0, 1)
while (not p1.play.contains(p1.check)) or (not p1.play.contains(p2.check)):
    print(p1.play + p1.check)
    print(p2.play + p2.check)
    current_player = players[p_order % 2]
    other_player = players[(p_order+1) % 2]
    while True:
        guess = input("Player #" + str((p_order % 2)+1)
                      + ", it is your turn to guess (<row> <column>): ").upper().split()
        try:
            guess_row = int(guess[0])
            guess_col = row_value[guess[1]]
            if not (1 <= guess_row <= 9):
                raise IndexError()
        except (ValueError, KeyError, IndexError):
            print("Incorrect input for row and column. " +
                  "Use numerals 1-9 for row and letter A-J for column separated by a space.")
            continue
        if current_player.play.get_item(guess_row, guess_col) == 0:
            current_player.set_guess(guess_row, guess_col)
            break
        else:
            print("You already guessed here. Try again!")
            continue

    if other_player.check.contains(current_player.guess):
        print("Hit!")
        current_player.play.edit_element(guess_row, guess_col, 1)
        counter = 0
        for ship in other_player.ships:
            if current_player.play.contains(ship) and other_player.placed_float[counter]:
                print("You sunk their " + ship_names[counter])
                other_player.placed_float[counter] = False
            counter += 1
        if current_player.play.contains(other_player.check):
            print("You win Player #" + str((p_order % 2) + 1) + "!!!")
            break
    else:
        print("Miss!")
        current_player.play.edit_element(guess_row, guess_col, 2)
    p_order += 1
