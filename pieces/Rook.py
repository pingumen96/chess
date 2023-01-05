from pieces.Piece import Piece


class Rook(Piece):
    def __init__(self, color, position):
        Piece.__init__(self, color, position)

    def getMoves(self, board):
        moves = []

        # check all the squares in the same row
        for i in range(1, 8):
            # check if the square is on the board
            if self.position[0] + i < 8:
                # check if the square is empty
                if board.getPiece(self.position[0] + i, self.position[1]) == None:
                    moves.append((self.position[0] + i, self.position[1]))
                else:
                    # check if the piece on the square is the same color
                    if board.getPiece(self.position[0] + i, self.position[1]).getColor() != self.color:
                        moves.append((self.position[0] + i, self.position[1]))
                    break
            else:
                break

        # check all the squares in the same row
        for i in range(1, 8):
            # check if the square is on the board
            if self.position[0] - i >= 0:
                # check if the square is empty
                if board.getPiece(self.position[0] - i, self.position[1]) == None:
                    moves.append((self.position[0] - i, self.position[1]))
                else:
                    # check if the piece on the square is the same color
                    if board.getPiece(self.position[0] - i, self.position[1]).getColor() != self.color:
                        moves.append((self.position[0] - i, self.position[1]))
                    break
            else:
                break

        # check all the squares in the same column
        for i in range(1, 8):
            # check if the square is on the board
            if self.position[1] + i < 8:
                # check if the square is empty
                if board.getPiece(self.position[0], self.position[1] + i) == None:
                    moves.append((self.position[0], self.position[1] + i))
                else:
                    # check if the piece on the square is the same color
                    if board.getPiece(self.position[0], self.position[1] + i).getColor() != self.color:
                        moves.append((self.position[0], self.position[1] + i))
                    break
            else:
                break

        # check all the squares in the same column
        for i in range(1, 8):
            # check if the square is on the board
            if self.position[1] - i >= 0:
                # check if the square is empty
                if board.getPiece(self.position[0], self.position[1] - i) == None:
                    moves.append((self.position[0], self.position[1] - i))
                else:
                    # check if the piece on the square is the same color
                    if board.getPiece(self.position[0], self.position[1] - i).getColor() != self.color:
                        moves.append((self.position[0], self.position[1] - i))
                    break
            else:
                break

        return moves

    def getSymbol(self):
        if self.color == 'white':
            return '♖'
        else:
            return '♜'
