import Piece
import Rook
import copy


class King(Piece):
    def __init__(self, color, position):
        Piece.__init__(self, color, position)

    def getMoves(self, board):
        """
        Returns a list of all possible moves for the King, without the moves that would put the King in check.
        """
        moves = []

        # Up
        if self.position[0] + 1 < 8:
            if board[self.position[0] + 1][self.position[1]] == 0:
                moves.append((self.position[0] + 1, self.position[1]))
            else:
                if board[self.position[0] + 1][self.position[1]].getColor() != self.color:
                    moves.append((self.position[0] + 1, self.position[1]))

        # Down
        if self.position[0] - 1 >= 0:
            if board[self.position[0] - 1][self.position[1]] == 0:
                moves.append((self.position[0] - 1, self.position[1]))
            else:
                if board[self.position[0] - 1][self.position[1]].getColor() != self.color:
                    moves.append((self.position[0] - 1, self.position[1]))

        # Right
        if self.position[1] + 1 < 8:
            if board[self.position[0]][self.position[1] + 1] == 0:
                moves.append((self.position[0], self.position[1] + 1))
            else:
                if board[self.position[0]][self.position[1] + 1].getColor() != self.color:
                    moves.append((self.position[0], self.position[1] + 1))

        # Left
        if self.position[1] - 1 >= 0:
            if board[self.position[0]][self.position[1] - 1] == 0:
                moves.append((self.position[0], self.position[1] - 1))
            else:
                if board[self.position[0]][self.position[1] - 1].getColor() != self.color:
                    moves.append((self.position[0], self.position[1] - 1))

        # Up-Right
        if self.position[0] + 1 < 8 and self.position[1] + 1 < 8:
            if board[self.position[0] + 1][self.position[1] + 1] == 0:
                moves.append((self.position[0] + 1, self.position[1] + 1))
            else:
                if board[self.position[0] + 1][self.position[1] + 1].getColor() != self.color:
                    moves.append((self.position[0] + 1, self.position[1] + 1))

        # Up-Left
        if self.position[0] + 1 < 8 and self.position[1] - 1 >= 0:
            if board[self.position[0] + 1][self.position[1] - 1] == 0:
                moves.append((self.position[0] + 1, self.position[1] - 1))
            else:
                if board[self.position[0] + 1][self.position[1] - 1].getColor() != self.color:
                    moves.append((self.position[0] + 1, self.position[1] - 1))

        # Down-Right
        if self.position[0] - 1 >= 0 and self.position[1] + 1 < 8:
            if board[self.position[0] - 1][self.position[1] + 1] == 0:
                moves.append((self.position[0] - 1, self.position[1] + 1))
            else:
                if board[self.position[0] - 1][self.position[1] + 1].getColor() != self.color:
                    moves.append((self.position[0] - 1, self.position[1] + 1))

        # Down-Left
        if self.position[0] - 1 >= 0 and self.position[1] - 1 >= 0:
            if board[self.position[0] - 1][self.position[1] - 1] == 0:
                moves.append((self.position[0] - 1, self.position[1] - 1))
            else:
                if board[self.position[0] - 1][self.position[1] - 1].getColor() != self.color:
                    moves.append((self.position[0] - 1, self.position[1] - 1))

        # Castling
        if self.color == "white":
            if self.position == (7, 4):
                if board[7][7] != 0:
                    if isinstance(board[7][7], Rook.Rook):
                        if board[7][7].getMoved() == False:
                            if board[7][5] == 0 and board[7][6] == 0:
                                moves.append((7, 6))
                if board[7][0] != 0:
                    if isinstance(board[7][0], Rook.Rook):
                        if board[7][0].getMoved() == False:
                            if board[7][1] == 0 and board[7][2] == 0 and board[7][3] == 0:
                                moves.append((7, 2))
        else:
            if self.position == (0, 4):
                if board[0][7] != 0:
                    if isinstance(board[0][7], Rook.Rook):
                        if board[0][7].getMoved() == False:
                            if board[0][5] == 0 and board[0][6] == 0:
                                moves.append((0, 6))
                if board[0][0] != 0:
                    if isinstance(board[0][0], Rook.Rook):
                        if board[0][0].getMoved() == False:
                            if board[0][1] == 0 and board[0][2] == 0 and board[0][3] == 0:
                                moves.append((0, 2))

        # remove moves that put the king in check
        returnMoves = []

        # for each move, make a copy of the board and move the piece to the new position
        # if the king is not in check, add the move to the list of valid moves
        for move in moves:
            boardCopy = copy.deepcopy(board)
            boardCopy[self.position[0]][self.position[1]] = 0
            boardCopy[move[0]][move[1]] = self
            if self.isCheck(boardCopy) == False:
                returnMoves.append(move)

        return returnMoves

    def isCheck(self, board):
        """
        Checks if the king is in check
        :param board: The board
        :return: True if the king is in check, False otherwise
        """
        if self.color == 1:
            for i in range(8):
                for j in range(8):
                    if board[i][j] != 0:
                        if board[i][j].getColor() == 0:
                            if self.position in board[i][j].getMoves(board):
                                return True
        else:
            for i in range(8):
                for j in range(8):
                    if board[i][j] != 0:
                        if board[i][j].getColor() == 1:
                            if self.position in board[i][j].getMoves(board):
                                return True
        return False

    def isCheckmate(self, board):
        """
        Checks if the king is in checkmate
        :param board: The board
        :return: True if the king is in checkmate, False otherwise
        """
        if self.isCheck(board):
            for i in range(8):
                for j in range(8):
                    if board[i][j] != 0:
                        if board[i][j].getColor() == self.color:
                            if board[i][j].getMoves(board) != []:
                                return False
            return True
        return False

    def getSymbol(self):
        if self.color == "white":
            return "♔"
        else:
            return "♚"
