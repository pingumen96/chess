import Piece


class Pawn(Piece):
    def __init__(self, color, position):
        Piece.__init__(self, color, position)

        self.doubleMoved = False

    def getDoubleMoved(self):
        return self.doubleMoved

    def setDoubleMoved(self, doubleMoved):
        self.doubleMoved = doubleMoved

    def getMoves(self, board):
        moves = []
        if self.color == "white":
            # check if pawn can move forward
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
            # check if pawn can move forward
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

        # en passant
        if self.color == "white":
            if self.position[0] == 3:
                # left
                if self.position[1] - 1 >= 0:
                    # check if there is a pawn in the left
                    if board[self.position[0]][self.position[1] - 1] != 0 and isinstance(board[self.position[0]][self.position[1] - 1], Pawn) and board[self.position[0]][self.position[1] - 1].getColor() != self.color:
                        # check if the pawn moved 2 spaces
                        if board[self.position[0]][self.position[1] - 1].getDoubleMoved():
                            moves.append(
                                (self.position[0] - 1, self.position[1] - 1))
                # right
                if self.position[1] + 1 < 8:
                    # check if there is a pawn in the right
                    if board[self.position[0]][self.position[1] + 1] != 0 and isinstance(board[self.position[0]][self.position[1] + 1], Pawn) and board[self.position[0]][self.position[1] + 1].getColor() != self.color:
                        # check if the pawn moved 2 spaces
                        if board[self.position[0]][self.position[1] + 1].getDoubleMoved():
                            moves.append(
                                (self.position[0] - 1, self.position[1] + 1))
        else:
            if self.position[0] == 4:
                # left
                if self.position[1] - 1 >= 0:
                    # check if there is a pawn in the left
                    if board[self.position[0]][self.position[1] - 1] != 0 and isinstance(board[self.position[0]][self.position[1] - 1], Pawn) and board[self.position[0]][self.position[1] - 1].getColor() != self.color:
                        # check if the pawn moved 2 spaces
                        if board[self.position[0]][self.position[1] - 1].getDoubleMoved():
                            moves.append(
                                (self.position[0] + 1, self.position[1] - 1))
                # right
                if self.position[1] + 1 < 8:
                    # check if there is a pawn in the right
                    if board[self.position[0]][self.position[1] + 1] != 0 and isinstance(board[self.position[0]][self.position[1] + 1], Pawn) and board[self.position[0]][self.position[1] + 1].getColor() != self.color:
                        # check if the pawn moved 2 spaces
                        if board[self.position[0]][self.position[1] + 1].getDoubleMoved():
                            moves.append(
                                (self.position[0] + 1, self.position[1] + 1))

        return moves

    def getSymbol(self):
        if self.color == "white":
            return "♙"
        else:
            return "♟"
