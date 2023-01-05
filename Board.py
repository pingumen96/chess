from pieces import Rook, Knight, Bishop, Queen, King, Pawn


class Board:
    def __init__(self):
        self.board = [[None]*8 for i in range(8)]
        self.board[0][0] = Rook(0, 0, "black")
        self.board[0][1] = Knight(0, 1, "black")
        self.board[0][2] = Bishop(0, 2, "black")
        self.board[0][3] = Queen(0, 3, "black")
        self.board[0][4] = King(0, 4, "black")
        self.board[0][5] = Bishop(0, 5, "black")
        self.board[0][6] = Knight(0, 6, "black")
        self.board[0][7] = Rook(0, 7, "black")
        self.board[1][0] = Pawn(1, 0, "black")
        self.board[1][1] = Pawn(1, 1, "black")
        self.board[1][2] = Pawn(1, 2, "black")
        self.board[1][3] = Pawn(1, 3, "black")
        self.board[1][4] = Pawn(1, 4, "black")
        self.board[1][5] = Pawn(1, 5, "black")
        self.board[1][6] = Pawn(1, 6, "black")
        self.board[1][7] = Pawn(1, 7, "black")
        self.board[6][0] = Pawn(6, 0, "white")
        self.board[6][1] = Pawn(6, 1, "white")
        self.board[6][2] = Pawn(6, 2, "white")
        self.board[6][3] = Pawn(6, 3, "white")
        self.board[6][4] = Pawn(6, 4, "white")
        self.board[6][5] = Pawn(6, 5, "white")
        self.board[6][6] = Pawn(6, 6, "white")
        self.board[6][7] = Pawn(6, 7, "white")
        self.board[7][0] = Rook(7, 0, "white")
        self.board[7][1] = Knight(7, 1, "white")
        self.board[7][2] = Bishop(7, 2, "white")
        self.board[7][3] = Queen(7, 3, "white")
        self.board[7][4] = King(7, 4, "white")
        self.board[7][5] = Bishop(7, 5, "white")
        self.board[7][6] = Knight(7, 6, "white")
        self.board[7][7] = Rook(7, 7, "white")

    def getBoard(self):
        return self.board

    def getPiece(self, x, y):
        return self.board[x][y]

    def setPiece(self, x, y, piece):
        self.board[x][y] = piece

    def movePiece(self, x1, y1, x2, y2):
        piece = self.getPiece(x1, y1)

        if piece is None:
            return False

        if (x2, y2) not in piece.getMoves(self):
            return False

        self.setPiece(x2, y2, piece)
        self.setPiece(x1, y1, None)

    def printBoard(self):
        for row in self.board:
            for piece in row:
                if piece is None:
                    print(" ", end=" ")
                else:
                    print(piece, end=" ")
            print()
