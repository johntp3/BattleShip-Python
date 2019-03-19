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
    while not players[p_order].finish():
        print("Player #" + str(p_order + 1) + ", it is your turn! Other player, turn around.\n" +
              str(players[p_order].check))
        available_ships = "Available ships: | "
        for x in range(5):
            if not players[p_order].placed_float[x]:
                available_ships += str(ship_names[x]) + " | "
        print(available_ships)

        while True:
            ship_name = input("Type one of the available ships: ")
            orientation = input("Pick an orientation. V for Vertical and H for Horizontal: ")
            ship_position = input("Type ship position in this format (<row> <column>): ")
            ship_row = int(ship_position[0])
            ship_col = int(ship_position[len(ship_position)-1])
            if players[p_order].check.can_edit_board(ship_name, orientation, ship_row, ship_col):
                players[p_order].check.edit_board(ship_name, orientation, ship_row, ship_col, 1)
                players[p_order].edit_ship(ship_name, orientation, ship_row, ship_col)
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
    guess = input("Player #" + str((p_order % 2) + 1) + ", it is your turn to guess (<row> <column>): ")
    guess_row = int(guess[0])
    guess_col = int(guess[len(guess)-1])
    current_player.set_guess(guess_row, guess_col)
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
