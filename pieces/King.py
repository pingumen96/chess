from pieces.Piece import Piece
from pieces.Rook import Rook
import copy


class King(Piece):
    def __init__(self, color, position):
        Piece.__init__(self, color, position)

    def getMoves(self, board, verifyCheck=True):
        """
        Returns a list of all possible moves for the King, without the moves that would put the King in check.
        """
        moves = []

        # Up
        if self.position[0] + 1 < 8:
            if board.getPiece(self.position[0] + 1, self.position[1]) == None:
                moves.append((self.position[0] + 1, self.position[1]))
            else:
                if board.getPiece(self.position[0] + 1, self.position[1]).getColor() != self.color:
                    moves.append((self.position[0] + 1, self.position[1]))

        # Down
        if self.position[0] - 1 >= 0:
            if board.getPiece(self.position[0] - 1, self.position[1]) == None:
                moves.append((self.position[0] - 1, self.position[1]))
            else:
                if board.getPiece(self.position[0] - 1, self.position[1]).getColor() != self.color:
                    moves.append((self.position[0] - 1, self.position[1]))

        # Right
        if self.position[1] + 1 < 8:
            if board.getPiece(self.position[0], self.position[1] + 1) == None:
                moves.append((self.position[0], self.position[1] + 1))
            else:
                if board.getPiece(self.position[0], self.position[1] + 1).getColor() != self.color:
                    moves.append((self.position[0], self.position[1] + 1))

        # Left
        if self.position[1] - 1 >= 0:
            if board.getPiece(self.position[0], self.position[1] - 1) == None:
                moves.append((self.position[0], self.position[1] - 1))
            else:
                if board.getPiece(self.position[0], self.position[1] - 1).getColor() != self.color:
                    moves.append((self.position[0], self.position[1] - 1))

        # Up-Right
        if self.position[0] + 1 < 8 and self.position[1] + 1 < 8:
            if board.getPiece(self.position[0] + 1, self.position[1] + 1) == None:
                moves.append((self.position[0] + 1, self.position[1] + 1))
            else:
                if board.getPiece(self.position[0] + 1, self.position[1] + 1).getColor() != self.color:
                    moves.append((self.position[0] + 1, self.position[1] + 1))

        # Up-Left
        if self.position[0] + 1 < 8 and self.position[1] - 1 >= 0:
            if board.getPiece(self.position[0] + 1, self.position[1] - 1) == None:
                moves.append((self.position[0] + 1, self.position[1] - 1))
            else:
                if board.getPiece(self.position[0] + 1, self.position[1] - 1).getColor() != self.color:
                    moves.append((self.position[0] + 1, self.position[1] - 1))

        # Down-Right
        if self.position[0] - 1 >= 0 and self.position[1] + 1 < 8:
            if board.getPiece(self.position[0] - 1, self.position[1] + 1) == None:
                moves.append((self.position[0] - 1, self.position[1] + 1))
            else:
                if board.getPiece(self.position[0] - 1, self.position[1] + 1).getColor() != self.color:
                    moves.append((self.position[0] - 1, self.position[1] + 1))

        # Down-Left
        if self.position[0] - 1 >= 0 and self.position[1] - 1 >= 0:
            if board.getPiece(self.position[0] - 1, self.position[1] - 1) == None:
                moves.append((self.position[0] - 1, self.position[1] - 1))
            else:
                if board.getPiece(self.position[0] - 1, self.position[1] - 1).getColor() != self.color:
                    moves.append((self.position[0] - 1, self.position[1] - 1))

        # Castling
        if self.color == "white":
            if self.position == (7, 4):
                if board.getPiece(7, 0) and board.getPiece(7, 0).getColor() == "white" and board.getPiece(7, 0).getMoved() == False:
                    if board.getPiece(7, 1) == None and board.getPiece(7, 2) == None and board.getPiece(7, 3) == None:
                        moves.append((7, 2))
                if board.getPiece(7, 7) and board.getPiece(7, 7).getColor() == "white" and board.getPiece(7, 7).getMoved() == False:
                    if board.getPiece(7, 5) == None and board.getPiece(7, 6) == None:
                        moves.append((7, 6))
        else:
            if self.position == (0, 4):
                if board.getPiece(0, 0) and board.getPiece(0, 0).getColor() == "black" and board.getPiece(0, 0).getMoved() == False:
                    if board.getPiece(0, 1) == None and board.getPiece(0, 2) == None and board.getPiece(0, 3) == None:
                        moves.append((0, 2))
                if board.getPiece(0, 7) and board.getPiece(0, 7).getColor() == "black" and board.getPiece(0, 7).getMoved() == False:
                    if board.getPiece(0, 5) == None and board.getPiece(0, 6) == None:
                        moves.append((0, 6))

        # remove moves that put the king in check
        returnMoves = []

        # for each move, make a copy of the board and move the piece to the new position
        # if the king is not in check, add the move to the list of valid moves
        if verifyCheck:
            for move in moves:
                boardCopy = copy.deepcopy(board)
                print("debug " + str(self.position) + "  " +
                      str(boardCopy.getPiece(self.position[0], self.position[1])))
                boardCopy.movePiece(self.position, move)
                if not boardCopy.getPiece(move[0], move[1]).isCheck(boardCopy):
                    returnMoves.append(move)

        return returnMoves

    def isCheck(self, board):
        """
        Checks if the king is in check
        :param board: The board
        :return: True if the king is in check, False otherwise
        """
        if self.color == "white":
            for i in range(8):
                for j in range(8):
                    piece = board.getPiece(i, j)
                    if piece and piece.getColor() == "black":
                        moves = None
                        # if the piece is instanceof King, make a different call to getMoves
                        if isinstance(piece, King):
                            moves = piece.getMoves(board, False)
                        else:
                            moves = piece.getMoves(board)
                        if (self.position[0], self.position[1]) in moves:
                            return True
        else:
            for i in range(8):
                for j in range(8):
                    piece = board.getPiece(i, j)
                    if piece and piece.getColor() == "white":
                        moves = None
                        # if the piece is instanceof King, make a different call to getMoves
                        if isinstance(piece, King):
                            moves = piece.getMoves(board, False)
                        else:
                            moves = piece.getMoves(board)
                        if (self.position[0], self.position[1]) in moves:
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
                    if board.getPiece(i, j) != None:
                        if board.getPiece(i, j).getColor() == self.color:
                            if board.getPiece(i, j).getMoves(board) != []:
                                return False

            return True
        return False

    def isStalemate(self, board):
        """
        Checks if the king is in stalemate
        :param board: The board
        :return: True if the king is in stalemate, False otherwise
        """
        if not self.isCheck(board):
            # check if any of the pieces can move
            for i in range(8):
                for j in range(8):
                    if board.getPiece(i, j) != None:
                        if board.getPiece(i, j).getColor() == self.color:
                            if board.getPiece(i, j).getMoves(board) != []:
                                return False

            return True

        return False

    def getSymbol(self):
        if self.color == "white":
            return "♔"
        else:
            return "♚"
