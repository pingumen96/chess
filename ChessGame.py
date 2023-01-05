import Board
from pieces import King, Queen, Rook, Bishop, Knight, Pawn


class ChessGame:
    def __init__(self):
        self.board = Board.Board()
        self.turn = "white"

    def getBoard(self):
        return self.board

    def getTurn(self):
        return self.turn

    def setTurn(self, turn):
        self.turn = turn

    def printBoard(self):
        self.board.printBoard()

    def isCheck(self):
        """
        Checks if the current player is in check
        :return: True if the current player is in check, False otherwise
        """
        for row in self.board.getBoard():
            for piece in row:
                if piece is not None and piece.getColor() == self.turn:
                    if isinstance(piece, King):
                        if piece.isCheck(self.board):
                            return True
        return False

    def isCheckmate(self):
        """
        Checks if the current player is in checkmate, i.e. if the king of the current player is in check and cannot move without being in check
        :return: True if the current player is in checkmate, False otherwise
        """
        for row in self.board.getBoard():
            for piece in row:
                if piece is not None and piece.getColor() == self.turn:
                    if isinstance(piece, King):
                        if piece.isCheckmate(self.board):
                            return True
        return False
