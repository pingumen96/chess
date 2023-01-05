from abc import ABC, abstractmethod


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

    @abstractmethod
    def getMoves(self, board):
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
