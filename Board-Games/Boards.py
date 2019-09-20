class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = []
        for y in range(self.height):
            for x in range(self.width):
                self.cells.append((x, y))

    # Makes all instances of Board iterable
    def __iter__(self):
        yield from self.cells


class TicTacToe(Board):
    def __init__(self):
        super(TicTacToe, self).__init__(width=3, height=3)


if __name__ == "__main__":
    board = Board(4, 5)
    print(board.width)
    print(board.height)
    tic_tac_toe_board = TicTacToe()
    print(tic_tac_toe_board.width)
    print(tic_tac_toe_board.height)
    print(tic_tac_toe_board.cells)