ship_data = {"destroyer": 2, "submarine": 3, "cruiser": 3, "battleship": 4, "carrier": 5}
row_value = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10}


class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = [[0] * self.cols for _ in range(self.rows)]

    def __eq__(self, other):
        if (self.rows != other.rows) or (self.cols != other.cols):
            return False

        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] != other.board[row][col]:
                    return False
        return True

    def __contains__(self, item):
        for row in range(self.rows):
            for col in range(self.cols):
                if item.board[row][col] == 1 and self.board[row][col] != 1:
                    return False
        return True

    def __str__(self):
        board_string = " "
        column_letter = "A"
        for x in range(self.cols):
            board_string += " " + chr(ord(column_letter) + x)

        for row in range(self.rows):
            board_string += "\n" + str(row+1)
            for col in range(self.cols):
                if self.board[row][col] == 1:
                    board_string += " X"
                elif self.board[row][col] == 2:
                    board_string += " !"
                else:
                    board_string += " O"
        return board_string + "\n"

    def __add__(self, other):
        board_string = " "
        column_letter = "A"
        for x in range(self.cols):
            board_string += " " + chr(ord(column_letter) + x)
        board_string += "        "
        for x in range(other.cols):
            board_string += " " + chr(ord(column_letter) + x)

        for row in range(self.rows):
            board_string += "\n" + str(row+1)
            for col in range(self.cols):
                if self.board[row][col] == 1:
                    board_string += " X"
                elif self.board[row][col] == 2:
                    board_string += " !"
                else:
                    board_string += " O"

            board_string += "       " + str(row + 1)
            for col in range(other.cols):
                if other.board[row][col] == 1:
                    board_string += " X"
                elif other.board[row][col] == 2:
                    board_string += " !"
                else:
                    board_string += " O"
        return board_string + "\n"

    def can_edit_board(self, ship_name, orientation, start_row, start_col):
        ship_length = 0
        try:
            ship_length = ship_data[ship_name]
        except KeyError:
            return False

        if orientation != "v" and orientation != "h":
            return False

        if orientation == "v":
            if (start_row + ship_length > self.rows + 1) or (start_col > self.cols):
                return False
        else:
            if (start_row > self.rows) or (start_col + ship_length > self.cols + 1):
                return False
        return True

    def edit_board(self, ship_name, orientation, start_row, start_col, value):
        ship_length = ship_data[ship_name]

        if orientation == "v":
            for x in range(ship_length):
                self.board[x + start_row - 1][start_col - 1] = value
        else:
            for x in range(ship_length):
                self.board[start_row - 1][x + start_col - 1] = value

    def edit_element(self, row, col, value):
        self.board[row - 1][col - 1] = value
