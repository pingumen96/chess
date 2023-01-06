from pieces.Piece import Piece


class Queen(Piece):
    def __init__(self, color, position):
        Piece.__init__(self, color, position)

    def getMoves(self, board, verifyCheck=True):
        moves = []

        # Up Right
        for i in range(1, 8):
            if self.position[0] + i < 8:
                if board.getPiece(self.position[0] + i, self.position[1]) == None:
                    moves.append((self.position[0] + i, self.position[1]))
                else:
                    if board.getPiece(self.position[0] + i, self.position[1]).getColor() != self.color:
                        moves.append(
                            (self.position[0] + i, self.position[1]))
                    break
            else:
                break

        # Up Left
        for i in range(1, 8):
            if self.position[0] - i >= 0:
                if board.getPiece(self.position[0] - i, self.position[1]) == None:
                    moves.append((self.position[0] - i, self.position[1]))
                else:
                    if board.getPiece(self.position[0] - i, self.position[1]).getColor() != self.color:
                        moves.append(
                            (self.position[0] - i, self.position[1]))
                    break
            else:
                break

        # Right
        for i in range(1, 8):
            if self.position[1] + i < 8:
                if board.getPiece(self.position[0], self.position[1] + i) == None:
                    moves.append((self.position[0], self.position[1] + i))
                else:
                    if board.getPiece(self.position[0], self.position[1] + i).getColor() != self.color:
                        moves.append(
                            (self.position[0], self.position[1] + i))
                    break
            else:
                break

        # Left
        for i in range(1, 8):
            if self.position[1] - i >= 0:
                if board.getPiece(self.position[0], self.position[1] - i) == None:
                    moves.append((self.position[0], self.position[1] - i))
                else:
                    if board.getPiece(self.position[0], self.position[1] - i).getColor() != self.color:
                        moves.append(
                            (self.position[0], self.position[1] - i))
                    break
            else:
                break

        # Down Right
        for i in range(1, 8):
            if self.position[0] + i < 8 and self.position[1] + i < 8:
                if board.getPiece(self.position[0] + i, self.position[1] + i) == None:
                    moves.append(
                        (self.position[0] + i, self.position[1] + i))
                else:
                    if board.getPiece(self.position[0] + i, self.position[1] + i).getColor() != self.color:
                        moves.append(
                            (self.position[0] + i, self.position[1] + i))
                    break
            else:
                break

        # Down Left
        for i in range(1, 8):
            if self.position[0] + i < 8 and self.position[1] - i >= 0:
                if board.getPiece(self.position[0] + i, self.position[1] - i) == None:
                    moves.append(
                        (self.position[0] + i, self.position[1] - i))
                else:
                    if board.getPiece(self.position[0] + i, self.position[1] - i).getColor() != self.color:
                        moves.append(
                            (self.position[0] + i, self.position[1] - i))
                    break
            else:
                break

        # Up Right
        for i in range(1, 8):
            if self.position[0] - i >= 0 and self.position[1] + i < 8:
                if board.getPiece(self.position[0] - i, self.position[1] + i) == None:
                    moves.append(
                        (self.position[0] - i, self.position[1] + i))
                else:
                    if board.getPiece(self.position[0] - i, self.position[1] + i).getColor() != self.color:
                        moves.append(
                            (self.position[0] - i, self.position[1] + i))
                    break
            else:
                break

        # Up Left
        for i in range(1, 8):
            if self.position[0] - i >= 0 and self.position[1] - i >= 0:
                if board.getPiece(self.position[0] - i, self.position[1] - i) == None:
                    moves.append(
                        (self.position[0] - i, self.position[1] - i))
                else:
                    if board.getPiece(self.position[0] - i, self.position[1] - i).getColor() != self.color:
                        moves.append(
                            (self.position[0] - i, self.position[1] - i))
                    break
            else:
                break

        if verifyCheck:
            return self.filterMoves(board, moves)
        else:
            return moves

    def getSymbol(self):
        if self.color == "white":
            return "♕"
        else:
            return "♛"
