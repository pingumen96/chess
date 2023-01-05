from pieces.Piece import Piece


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
                # check if pawn can move 1 space forward
                if board.getPiece(self.position[0] - 1, self.position[1]) == None:
                    moves.append((self.position[0] - 1, self.position[1]))
                if self.position[1] - 1 >= 0:
                    if board.getPiece(self.position[0] - 1, self.position[1] - 1) != None and board.getPiece(self.position[0] - 1, self.position[1] - 1).getColor() != self.color:
                        moves.append(
                            (self.position[0] - 1, self.position[1] - 1))
                if self.position[1] + 1 < 8:
                    if board.getPiece(self.position[0] - 1, self.position[1] + 1) != None and board.getPiece(self.position[0] - 1, self.position[1] + 1).getColor() != self.color:
                        moves.append(
                            (self.position[0] - 1, self.position[1] + 1))
            # check if pawn can move 2 spaces forward
            if self.position[0] - 2 >= 0:
                if board.getPiece(self.position[0] - 2, self.position[1]) == None and board.getPiece(self.position[0] - 1, self.position[1]) == None:
                    moves.append((self.position[0] - 2, self.position[1]))
            # check if pawn can en passant
            if self.position[0] == 4:
                # left
                if self.position[1] - 1 >= 0:
                    # check if there is a pawn in the left
                    if board.getPiece(self.position[0], self.position[1] - 1) != None and isinstance(board.getPiece(self.position[0], self.position[1] - 1), Pawn) and board.getPiece(self.position[0], self.position[1] - 1).getColor() != self.color:
                        # check if the pawn moved 2 spaces
                        if board.getPiece(self.position[0], self.position[1] - 1).getDoubleMoved():
                            moves.append(
                                (self.position[0] - 1, self.position[1] - 1))
                # right
                if self.position[1] + 1 < 8:
                    # check if there is a pawn in the right
                    if board.getPiece(self.position[0], self.position[1] + 1) != None and isinstance(board.getPiece(self.position[0], self.position[1] + 1), Pawn) and board.getPiece(self.position[0], self.position[1] + 1).getColor() != self.color:
                        # check if the pawn moved 2 spaces
                        if board.getPiece(self.position[0], self.position[1] + 1).getDoubleMoved():
                            moves.append(
                                (self.position[0] - 1, self.position[1] + 1))
        else:
            # check if pawn can move forward
            if self.position[0] + 1 < 8:
                if board.getPiece(self.position[0] + 1, self.position[1]) == None:
                    moves.append((self.position[0] + 1, self.position[1]))
                if self.position[1] - 1 >= 0:
                    if board.getPiece(self.position[0] + 1, self.position[1] - 1) != None and board.getPiece(self.position[0] + 1, self.position[1] - 1).getColor() != self.color:
                        moves.append(
                            (self.position[0] + 1, self.position[1] - 1))
                if self.position[1] + 1 < 8:
                    if board.getPiece(self.position[0] + 1, self.position[1] + 1) != None and board.getPiece(self.position[0] + 1, self.position[1] + 1).getColor() != self.color:
                        moves.append(
                            (self.position[0] + 1, self.position[1] + 1))
            # check if pawn can move 2 spaces forward
            if self.position[0] + 2 < 8:
                if board.getPiece(self.position[0] + 2, self.position[1]) == None and board.getPiece(self.position[0] + 1, self.position[1]) == None:
                    moves.append((self.position[0] + 2, self.position[1]))
            # check if pawn can en passant
            if self.position[0] == 3:
                # left
                if self.position[1] - 1 >= 0:
                    # check if there is a pawn in the left
                    if board.getPiece(self.position[0], self.position[1] - 1) != None and isinstance(board.getPiece(self.position[0], self.position[1] - 1), Pawn) and board.getPiece(self.position[0], self.position[1] - 1).getColor() != self.color:
                        # check if the pawn moved 2 spaces
                        if board.getPiece(self.position[0], self.position[1] - 1).getDoubleMoved():
                            moves.append(
                                (self.position[0] + 1, self.position[1] - 1))
                # right
                if self.position[1] + 1 < 8:
                    # check if there is a pawn in the right
                    if board.getPiece(self.position[0], self.position[1] + 1) != None and isinstance(board.getPiece(self.position[0], self.position[1] + 1), Pawn) and board.getPiece(self.position[0], self.position[1] + 1).getColor() != self.color:
                        # check if the pawn moved 2 spaces
                        if board.getPiece(self.position[0], self.position[1] + 1).getDoubleMoved():
                            moves.append(
                                (self.position[0] + 1, self.position[1] + 1))

        return moves

    def getSymbol(self):
        if self.color == "white":
            return "♙"
        else:
            return "♟"
