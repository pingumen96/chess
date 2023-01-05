import Board
from pieces.King import King


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

    def isStalemate(self):
        """
        Checks if the current player is in stalemate, i.e. if the king of the current player is not in check and cannot move without being in check
        :return: True if the current player is in stalemate, False otherwise
        """
        for row in self.board.getBoard():
            for piece in row:
                if piece is not None and piece.getColor() == self.turn:
                    if isinstance(piece, King):
                        if piece.isStalemate(self.board):
                            return True
        return False

    def isDraw(self):
        """
        Checks if the game is a draw
        :return: True if the game is a draw, False otherwise
        """
        if self.isStalemate():
            return True
        return False

    def isGameOver(self):
        """
        Checks if the game is over
        :return: True if the game is over, False otherwise
        """
        if self.isCheckmate() or self.isDraw():
            return True
        return False

    def move(self, start, end):
        """
        Moves a piece from start to end
        :param start: The start position
        :param end: The end position
        :return: True if the move was successful, False otherwise
        """
        if self.board.getBoard()[start[0]][start[1]] is not None and self.board.getBoard()[start[0]][start[1]].getColor() == self.turn:
            if end in self.board.getBoard()[start[0]][start[1]].getMoves(self.board):
                self.board.getBoard()[end[0]][end[1]] = self.board.getBoard()[
                    start[0]][start[1]]
                self.board.getBoard()[start[0]][start[1]] = None
                self.board.getBoard()[end[0]][end[1]].setPosition(end)
                self.setTurn("black" if self.turn == "white" else "white")
                return True
        return False

    def runGame(self):
        """
        Runs the game
        :return: None
        """
        while not self.isGameOver():
            self.printBoard()
            print("It is " + self.turn + "'s turn")

            start = input("Enter the start position: ")
            end = input("Enter the end position: ")

            if not self.move((int(start[0]), int(start[1])), (int(end[0]), int(end[1]))):
                print("Invalid move")
