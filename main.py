import chess
import time

# artificial intelligence for chess


def countOnes(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count


def evaluatePosition(board):
    pieceValues = {
        chess.PAWN: 1,
        chess.KNIGHT: 3,
        chess.BISHOP: 3,
        chess.ROOK: 5,
        chess.QUEEN: 9,
        chess.KING: 0
    }

    positionValue = 0

    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece is not None:
            positionValue += pieceValues[piece.piece_type] * \
                (1 if piece.color == chess.WHITE else -1)

    return positionValue


def minimax(board, depth, alpha, beta, maximizingPlayer):
    if depth == 0:
        return evaluatePosition(board)

    if maximizingPlayer:
        maxEval = -9999
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, False)
            board.pop()
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)

            # alpha-beta pruning
            if beta <= alpha:
                break
        return maxEval
    else:
        minEval = 9999
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, True)
            board.pop()
            minEval = min(minEval, eval)
            beta = min(beta, eval)

            # alpha-beta pruning
            if beta <= alpha:
                break
        return minEval


board = chess.Board()

game = "Nf3 Nf6 c4 g6 Nc3 Bg7 d4 O-O Bf4 d5 Qb3 dxc4 Qxc4 c6 e4 Nbd7 Rd1 Nb6 Qc5 Bg4 Bg5 Na4 Qa3 Nxc3 bxc3 Nxe4 Bxe7 Qb6 Bc4 Nxc3 Bc5 Rfe8+ Kf1 Be6 Bxb6 Bxc4+ Kg1 Ne2+ Kf1 Nxd4+ Kg1 Ne2+ Kf1 Nc3+ Kg1 axb6 Qb4 Ra4 Qxb6 Nxd1 h3 Rxa2 Kh2 Nxf2 Re1 Rxe1 Qd8+ Bf8 Nxe1 Bd5 Nf3 Ne4 Qb8 b5 h4 h5 Ne5 Kg7 Kg1 Bc5+ Kf1 Ng3+ Ke1 Bb4+ Kd1 Bb3+ Kc1 Ne2+ Kb1 Nc3+ Kc1 Rc2#"
moves = game.split()

# start timer
timestamp = time.time()

# for each move in game, push it to the board
for move in moves:
    board.push_san(move)
    print(board)

    print("Position value: " + str(evaluatePosition(board)))
    print("Best move: " + str(minimax(board, 3, -9999, 9999, True)))
    print("Is check: " + str(board.is_check()))
    print("Is checkmate: " + str(board.is_checkmate()))

# end timer
print("Time elapsed: " + str(time.time() - timestamp) + " seconds")
