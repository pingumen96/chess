import Piece


class Knight(Piece):
    def __init__(self, color, position):
        Piece.__init__(self, color, position)

    def getMoves(self, board):
        moves = []

        # Up 2
        if self.position[0] + 2 < 8:
            if self.position[1] + 1 < 8:
                if board[self.position[0] + 2][self.position[1] + 1] == 0:
                    moves.append((self.position[0] + 2, self.position[1] + 1))
                else:
                    if board[self.position[0] + 2][self.position[1] + 1].getColor() != self.color:
                        moves.append(
                            (self.position[0] + 2, self.position[1] + 1))
            if self.position[1] - 1 >= 0:
                if board[self.position[0] + 2][self.position[1] - 1] == 0:
                    moves.append((self.position[0] + 2, self.position[1] - 1))
                else:
                    if board[self.position[0] + 2][self.position[1] - 1].getColor() != self.color:
                        moves.append(
                            (self.position[0] + 2, self.position[1] - 1))

        # Down 2
        if self.position[0] - 2 >= 0:
            if self.position[1] + 1 < 8:
                if board[self.position[0] - 2][self.position[1] + 1] == 0:
                    moves.append((self.position[0] - 2, self.position[1] + 1))
                else:
                    if board[self.position[0] - 2][self.position[1] + 1].getColor() != self.color:
                        moves.append(
                            (self.position[0] - 2, self.position[1] + 1))
            if self.position[1] - 1 >= 0:
                if board[self.position[0] - 2][self.position[1] - 1] == 0:
                    moves.append((self.position[0] - 2, self.position[1] - 1))
                else:
                    if board[self.position[0] - 2][self.position[1] - 1].getColor() != self.color:
                        moves.append(
                            (self.position[0] - 2, self.position[1] - 1))

        # Right 2
        if self.position[1] + 2 < 8:
            if self.position[0] + 1 < 8:
                if board[self.position[0] + 1][self.position[1] + 2] == 0:
                    moves.append((self.position[0] + 1, self.position[1] + 2))
                else:
                    if board[self.position[0] + 1][self.position[1] + 2].getColor() != self.color:
                        moves.append(
                            (self.position[0] + 1, self.position[1] + 2))
            if self.position[0] - 1 >= 0:
                if board[self.position[0] - 1][self.position[1] + 2] == 0:
                    moves.append((self.position[0] - 1, self.position[1] + 2))
                else:
                    if board[self.position[0] - 1][self.position[1] + 2].getColor() != self.color:
                        moves.append(
                            (self.position[0] - 1, self.position[1] + 2))

        # Left 2
        if self.position[1] - 2 >= 0:
            if self.position[0] + 1 < 8:
                if board[self.position[0] + 1][self.position[1] - 2] == 0:
                    moves.append((self.position[0] + 1, self.position[1] - 2))
                else:
                    if board[self.position[0] + 1][self.position[1] - 2].getColor() != self.color:
                        moves.append(
                            (self.position[0] + 1, self.position[1] - 2))
            if self.position[0] - 1 >= 0:
                if board[self.position[0] - 1][self.position[1] - 2] == 0:
                    moves.append((self.position[0] - 1, self.position[1] - 2))
                else:
                    if board[self.position[0] - 1][self.position[1] - 2].getColor() != self.color:
                        moves.append(
                            (self.position[0] - 1, self.position[1] - 2))

        return moves

    def getSymbol(self):
        if self.color == "white":
            return "♘"
        else:
            return "♞"
