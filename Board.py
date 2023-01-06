from pieces.Piece import Piece
from pieces.Pawn import Pawn
from pieces.Rook import Rook
from pieces.Knight import Knight
from pieces.Bishop import Bishop
from pieces.Queen import Queen
from pieces.King import King


class Board:
    def __init__(self):
        self.board = [[None]*8 for i in range(8)]
        self.board[0][0] = Rook("black", (0, 0))
        self.board[0][1] = Knight("black", (0, 1))
        self.board[0][2] = Bishop("black", (0, 2))
        self.board[0][3] = Queen("black", (0, 3))
        self.board[0][4] = King("black", (0, 4))
        self.board[0][5] = Bishop("black", (0, 5))
        self.board[0][6] = Knight("black", (0, 6))
        self.board[0][7] = Rook("black", (0, 7))
        for i in range(8):
            self.board[1][i] = Pawn("black", (1, i))
        for i in range(8):
            self.board[6][i] = Pawn("white", (6, i))
        self.board[7][0] = Rook("white", (7, 0))
        self.board[7][1] = Knight("white", (7, 1))
        self.board[7][2] = Bishop("white", (7, 2))
        self.board[7][3] = Queen("white", (7, 3))
        self.board[7][4] = King("white", (7, 4))
        self.board[7][5] = Bishop("white", (7, 5))
        self.board[7][6] = Knight("white", (7, 6))
        self.board[7][7] = Rook("white", (7, 7))

    def getBoard(self):
        return self.board

    def getPiece(self, x, y):
        return self.board[x][y]

    def movePiece(self, start, end):
        if self.getPiece(start[0], start[1]) is not None:
            self.setPiece(end[0], end[1], self.getPiece(start[0], start[1]))
            self.setPiece(start[0], start[1], None)
            return True
        return False

    def isCheck(self, color):
        king = None
        for i in range(8):
            for j in range(8):
                if isinstance(self.getPiece(i, j), King) and self.getPiece(i, j).getColor() == color:
                    king = self.getPiece(i, j)
        for i in range(8):
            for j in range(8):
                if self.getPiece(i, j) is not None and self.getPiece(i, j).getColor() != color:
                    for move in self.getPiece(i, j).getMoves(self):
                        if move == king.getPosition():
                            return True
        return False

    def setPiece(self, x, y, piece):
        self.board[x][y] = piece

    def promotePawn(self, x, y, piece):
        if isinstance(piece, Queen) or isinstance(piece, Rook) or isinstance(piece, Bishop) or isinstance(piece, Knight):
            self.setPiece(x, y, piece)
            return True
        return False

    def printBoard(self):
        # print coordinates
        print("  0 1 2 3 4 5 6 7")
        for i in range(8):
            print(i, end=" ")
            for j in range(8):
                if self.getPiece(i, j) is None:
                    print("·", end=" ")
                else:
                    print(self.getPiece(i, j).getSymbol(), end=" ")
            print()
        print("  0 1 2 3 4 5 6 7")
