from Board import *

ship_names = ("destroyer", "submarine", "cruiser", "battleship", "carrier")


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
        self.ships = [self.destroyer, self.submarine, self.cruiser, self.battleship, self.carrier]
        self.placed_float = [False, False, False, False, False, True]  # last element used to bypass first check

    def set_guess(self, row, col):
        self.guess = Board(self.rows, self.cols)
        self.guess.edit_element(row, col, 1)

    def finish(self):
        b_initial = self.placed_float[0]
        for b in self.placed_float:
            if b_initial is not b:
                return False
        return True

    def edit_ship(self, ship_name, orientation, start_row, start_col):
        for x in range(len(ship_names)):
            if ship_name == ship_names[x]:
                self.ships[x].edit_board(ship_name, orientation, start_row, start_col, 1)
                self.placed_float[x] = True
                break
