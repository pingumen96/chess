import Piece


class Bishop(Piece):
    def __init__(self, color, position):
        Piece.__init__(self, color, position)

    def getMoves(self, board):
        moves = []
        for i in range(1, 8):
            if self.position[0] + i < 8 and self.position[1] + i < 8:
                if board[self.position[0] + i][self.position[1] + i] == 0:
                    moves.append((self.position[0] + i, self.position[1] + i))
                else:
                    if board[self.position[0] + i][self.position[1] + i].getColor() != self.color:
                        moves.append(
                            (self.position[0] + i, self.position[1] + i))
                    break
            else:
                break
        for i in range(1, 8):
            if self.position[0] + i < 8 and self.position[1] - i >= 0:
                if board[self.position[0] + i][self.position[1] - i] == 0:
                    moves.append((self.position[0] + i, self.position[1] - i))
                else:
                    if board[self.position[0] + i][self.position[1] - i].getColor() != self.color:
                        moves.append(
                            (self.position[0] + i, self.position[1] - i))
                    break
            else:
                break
        for i in range(1, 8):
            if self.position[0] - i >= 0 and self.position[1] + i < 8:
                if board[self.position[0] - i][self.position[1] + i] == 0:
                    moves.append((self.position[0] - i, self.position[1] + i))
                else:
                    if board[self.position[0] - i][self.position[1] + i].getColor() != self.color:
                        moves.append(
                            (self.position[0] - i, self.position[1] + i))
                    break
            else:
                break
        for i in range(1, 8):
            if self.position[0] - i >= 0 and self.position[1] - i >= 0:
                if board[self.position[0] - i][self.position[1] - i] == 0:
                    moves.append((self.position[0] - i, self.position[1] - i))
                else:
                    if board[self.position[0] - i][self.position[1] - i].getColor() != self.color:
                        moves.append(
                            (self.position[0] - i, self.position[1] - i))
                    break
            else:
                break

        return moves

    def getSymbol(self):
        if self.color == 'white':
            return '♗'
        else:
            return '♝'
