from math import ceil
class Board:
    def __init__(self, board=None):
        self.rows = 6
        self.columns = 7
        if board == None:
            self.board = self.createBoard()
        else:
            self.board = board

    """Create an empty board"""
    def createBoard(self):
        board = []
        for r in range(self.rows):
            row = []
            for c in range(self.columns):
                row.append(None)
            board.append(row)
        return board

    """Copy the current board"""
    def copyBoard(self):
        board = []
        for r in range(self.rows):
            row = []
            for c in range(self.columns):
                row.append(self.board[r][c])
            board.append(row)
        return board

    """Find the row that the place will be put in for the column"""
    def findRow(column):
        row = 0
        while self.board[row][column] != None:
            row += 1
        return row

    """Place the player at the row and column given"""
    def placePiece(self, row, column, player):
        self.board[row][column] = player

    """Prints the current board out"""
    def printBoard(self):
        for r in range(self.rows - 1, -1, -1):
            print("|", end="")
            for c in range(self.columns):
                if self.board[r][c] == None:
                    print(" ", end="|")
                else:
                    print(self.board[r][c].piece, end="|")
            print()

    """Checks if the row and column creates a win in that row"""
    def rowWin(self, row, column, player):
        for c in range(math.ceil(self.columns/2)):
            if c + 4 <= column:
                continue
            count = 0
            for dist in range(4):
                if self.board[row][c + dist] == player:
                    count += 1
            if count == 4:
                return True
        return False

    """Checks if the row and column creates a win in that column"""
    def columnWin(self, row, column, player):
        for r in range(math.ceil(self.rows/2)):
            if r + 4 <= row:
                continue
            count = 0
            for dist in range(4):
                if self.board[row + dist][column] == player:
                    count += 1
            if count == 4:
                return True
        return False

    """Checks if the row and column creates a diagonal win going up"""
    def upDiagonalWin(self, row, column, player):
        for r in range(math.ceil(self.rows/2)):
            if r + 4 <= row:
                continue
            for c in range(math.ceil(self.columns/2)):
                if c + 4 <= column:
                    continue
                count = 0
                for dist in range(4):
                    if self.board[r + dist][c + dist]:
                        count += 1
                if count == 4:
                    return True
        return False


    """Checks if the row and column creates a diagonal win going down"""
    def downDiagonalWin(self, row, column, player):
        for r in range(math.ceil(self.rows/2)):
            if r + 4 <= row:
                continue
            for c in range(math.ceil(self.columns/2)):
                if c + 4 <= column:
                    continue
                count = 0
                for dist in range(4):
                    if self.board[r + dist][c - dist]:
                        count += 1
                if count == 4:
                    return True
        return False

    """Checks for diagonal win"""
    def diagonalWin(self, row, column, player):
        return upDiagonalWin(row, column, player) \
            or downDiagonalWin(row, column, player)

    """Checks to see if there is a row, column, or diagonal win"""
    def win(self, row, column, player):
        if self.rowWin(row, column, player) \
            or self.columnWin(row, column, player) \
            or self.diagonalWin(row, column, player) :
                return True
        return False

    """Checks if the whole board is full and there is no wins"""
    def tie(self):
        for r in range(self.rows):
            for c in range(self.columns):
                if self.board[r][c] == None:
                    return False
        return True
