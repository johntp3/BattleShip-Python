from Board import *


class Player:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.play = Board(self.rows, self.cols)
        self.check = Board(self.rows, self.cols)
        self.guess = Board(self.rows, self.cols)
        self.destroyer = Board(self.rows, self.cols)
        self.submarine = Board(self.rows, self.cols)
        self.cruiser = Board(self.rows, self.cols)
        self.battleship = Board(self.rows, self.cols)
        self.carrier = Board(self.rows, self.cols)

    def set_guess(self, row, col):
        self.guess = Board(self.rows, self.cols)
        self.guess.edit_element(row, col, 1)


''' Proof of concept
player1 = Player(3, 4)
player1.check.edit_element(1, 1, 1)
player1.check.edit_element(1, 2, 1)
player1.check.edit_element(1, 3, 1)

while player1.check not in player1.play:
    print(player1.play + player1.check)
    guess_string = input("Enter row and column of your guess Player 2 (<row> <col>): ")
    guess_row = int(guess_string[0])
    guess_col = int(guess_string[len(guess_string)-1])
    player1.set_guess(guess_row, guess_col)
    if player1.guess in player1.check:
        print("Hit!")
        player1.play.edit_element(guess_row, guess_col, 1)
    else:
        print("Miss!")
        player1.play.edit_element(guess_row, guess_col, 2)
'''