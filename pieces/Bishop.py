from pieces.Piece import Piece


class Bishop(Piece):
    def __init__(self, color, position):
        Piece.__init__(self, color, position)

    def getMoves(self, board, verifyCheck=True):
        moves = []

        # up left
        for i in range(1, 8):
            if self.position[0] + i < 8 and self.position[1] + i < 8:
                if board.getPiece(self.position[0] + i, self.position[1] + i) == None:
                    moves.append((self.position[0] + i, self.position[1] + i))
                else:
                    if board.getPiece(self.position[0] + i, self.position[1] + i).getColor() != self.color:
                        moves.append(
                            (self.position[0] + i, self.position[1] + i))
                    break
            else:
                break

        # down right
        for i in range(1, 8):
            if self.position[0] - i >= 0 and self.position[1] - i >= 0:
                if board.getPiece(self.position[0] - i, self.position[1] - i) == None:
                    moves.append((self.position[0] - i, self.position[1] - i))
                else:
                    if board.getPiece(self.position[0] - i, self.position[1] - i).getColor() != self.color:
                        moves.append(
                            (self.position[0] - i, self.position[1] - i))
                    break
            else:
                break

        # up right
        for i in range(1, 8):
            if self.position[0] + i < 8 and self.position[1] - i >= 0:
                if board.getPiece(self.position[0] + i, self.position[1] - i) == None:
                    moves.append((self.position[0] + i, self.position[1] - i))
                else:
                    if board.getPiece(self.position[0] + i, self.position[1] - i).getColor() != self.color:
                        moves.append(
                            (self.position[0] + i, self.position[1] - i))
                    break
            else:
                break

        # down left
        for i in range(1, 8):
            if self.position[0] - i >= 0 and self.position[1] + i < 8:
                if board.getPiece(self.position[0] - i, self.position[1] + i) == None:
                    moves.append((self.position[0] - i, self.position[1] + i))
                else:
                    if board.getPiece(self.position[0] - i, self.position[1] + i).getColor() != self.color:
                        moves.append(
                            (self.position[0] - i, self.position[1] + i))
                    break
            else:
                break

        if verifyCheck:
            return self.filterMoves(board, moves)
        else:
            return moves

    def getSymbol(self):
        if self.color == 'white':
            return '♗'
        else:
            return '♝'
