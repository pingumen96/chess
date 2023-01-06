from Board import Board
from pieces.King import King
from random import randint


class ChessGame:
    def __init__(self):
        self.board = Board()
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

    def runGame(self, random=False):
        """
        Runs the game
        :return: None
        """
        while not self.isGameOver():
            self.printBoard()
            print("It is " + self.turn + "'s turn")

            if random:
                # get random piece in the board, which means that the piece is not None and the piece's color is the same as the turn
                piece = self.board.getPiece(randint(0, 7), randint(0, 7))

                while piece is None or piece.getColor() != self.turn or len(piece.getMoves(self.board)) == 0:
                    piece = self.board.getPiece(randint(0, 7), randint(0, 7))

                move = piece.getMoves(self.board)[randint(
                    0, len(piece.getMoves(self.board)) - 1)]

                oldPosition = piece.getPosition()

                # print the move
                print(self.turn + " moved " + piece.getSymbol() +
                      " from " + str(oldPosition) + " to " + str(move))

                # move the piece
                self.move(piece.getPosition(), move)
            else:
                # expects input in the form of "x,y"
                start = input("Enter the start position: ")
                start = start.split(",")
                start = (int(start[0]), int(start[1]))

                end = input("Enter the end position: ")
                end = end.split(",")
                end = (int(end[0]), int(end[1]))

                if not self.move(start, end):
                    print("Invalid move")

        self.printBoard()

        if self.isCheckmate():
            print("Checkmate! " + ("White" if self.turn ==
                  "black" else "Black") + " wins!")
        elif self.isDraw():
            print("Draw!")
