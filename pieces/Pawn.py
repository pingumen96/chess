import Piece


class Pawn(Piece):
    def __init__(self, color, position):
        Piece.__init__(self, color, position)

    def getMoves(self, board):
        moves = []
        if self.color == "white":
            if self.position[0] - 1 >= 0:
                if board[self.position[0] - 1][self.position[1]] == 0:
                    moves.append((self.position[0] - 1, self.position[1]))
                if self.position[1] - 1 >= 0:
                    if board[self.position[0] - 1][self.position[1] - 1] != 0:
                        if board[self.position[0] - 1][self.position[1] - 1].getColor() != self.color:
                            moves.append(
                                (self.position[0] - 1, self.position[1] - 1))
                if self.position[1] + 1 < 8:
                    if board[self.position[0] - 1][self.position[1] + 1] != 0:
                        if board[self.position[0] - 1][self.position[1] + 1].getColor() != self.color:
                            moves.append(
                                (self.position[0] - 1, self.position[1] + 1))
            if self.position[0] == 6:
                if board[self.position[0] - 1][self.position[1]] == 0:
                    if board[self.position[0] - 2][self.position[1]] == 0:
                        moves.append((self.position[0] - 2, self.position[1]))
        else:
            if self.position[0] + 1 < 8:
                if board[self.position[0] + 1][self.position[1]] == 0:
                    moves.append((self.position[0] + 1, self.position[1]))
                if self.position[1] - 1 >= 0:
                    if board[self.position[0] + 1][self.position[1] - 1] != 0:
                        if board[self.position[0] + 1][self.position[1] - 1].getColor() != self.color:
                            moves.append(
                                (self.position[0] + 1, self.position[1] - 1))
                if self.position[1] + 1 < 8:
                    if board[self.position[0] + 1][self.position[1] + 1] != 0:
                        if board[self.position[0] + 1][self.position[1] + 1].getColor() != self.color:
                            moves.append(
                                (self.position[0] + 1, self.position[1] + 1))
            if self.position[0] == 1:
                if board[self.position[0] + 1][self.position[1]] == 0:
                    if board[self.position[0] + 2][self.position[1]] == 0:
                        moves.append((self.position[0] + 2, self.position[1]))
        return moves

    def getSymbol(self):
        if self.color == "white":
            return "♙"
        else:
            return "♟"
