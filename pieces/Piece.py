from abc import ABC, abstractmethod
import copy


class Piece(ABC):
    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.moved = False

    def getColor(self):
        return self.color

    def getPosition(self):
        return self.position

    def setPosition(self, position):
        self.position = position

    def getMoved(self):
        return self.moved

    def setMoved(self, moved):
        self.moved = moved

    def filterMoves(self, board, moves):
        # if there is a check, remove all moves that don't remove the check
        if board.isCheck(self.color):
            returnMoves = []

            # do the move in a copy of the board
            for move in moves:
                copyBoard = copy.deepcopy(board)
                copyBoard.movePiece(self.position, move)
                if not copyBoard.isCheck(self.color):
                    returnMoves.append(move)
            return returnMoves
        else:
            return moves

    @abstractmethod
    def getMoves(self, board, verifyCheck=True):
        """
        :param board: The board the piece is on
        :return: A list of tuples of the possible moves
        """
        pass

    @abstractmethod
    def getSymbol(self):
        """
        :return: The symbol of the piece
        """
        pass

    def __str__(self):
        return self.getSymbol() + " " + self.color + " " + str(self.position)
