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

    def can_edit_check_board(self, ship_name, orientation, start_row, start_col):
        length_of_ship = 0
        try:
            length_of_ship = ship_length[ship_name]
        except KeyError:
            return False

        if orientation != "v" and orientation != "h":
            return False

        if orientation == "v":
            if (start_row + length_of_ship > self.rows + 1) or (start_col > self.cols):
                return False
            else:
                for x in range(length_of_ship):
                    if self.check.get_item(x + start_row, start_col) == 1:
                        return False
        else:
            if (start_row > self.rows) or (start_col + length_of_ship > self.cols + 1):
                return False
            else:
                for x in range(length_of_ship):
                    if self.check.get_item(start_row, x + start_col) == 1:
                        return False
        return True

    def edit_ship(self, ship_name, orientation, start_row, start_col, value):
        if value == 1:
            for x in range(len(ship_names)):
                if ship_name == ship_names[x]:
                    self.ships[x].edit_board(ship_name, orientation, start_row, start_col, value)
                    self.placed_float[x] = True
                    break
        else:
            for x in range(len(ship_names)):
                if ship_name == ship_names[x]:
                    for row in range(1, self.rows+1):
                        for col in range(1, self.cols+1):
                            if self.ships[x].get_item(row, col) == 1:
                                self.check.edit_element(row, col, 0)
                                self.ships[x].edit_element(row, col, 0)
                    self.placed_float[x] = False
