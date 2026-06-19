import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():

    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):

    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    return O if x_count > o_count else X


def actions(board):

    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}


def result(board, action):

    i, j = action
    if i not in range(3) or j not in range(3) or board[i][j] is not EMPTY:
        raise ValueError("Acao invalida.")
        
    new_board = copy.deepcopy(board)
    new_board[i][j] = player(board)
    return new_board


def winner(board):

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not EMPTY:
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2]
        
    return None


def terminal(board):

    return winner(board) is not None or all(cell is not EMPTY for row in board for cell in row)


def utility(board):

    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    return 0


def minimax(board):
    
    if terminal(board):
        return None

    curr_player = player(board)

    if curr_player == X:
        best_val = -math.inf
        best_action = None
        alpha = -math.inf
        beta = math.inf
        
        for action in actions(board):
            val = min_value(result(board, action), alpha, beta)
            if val > best_val:
                best_val = val
                best_action = action
            alpha = max(alpha, best_val)
        return best_action
        
    else:
        best_val = math.inf
        best_action = None
        alpha = -math.inf
        beta = math.inf
        
        for action in actions(board):
            val = max_value(result(board, action), alpha, beta)
            if val < best_val:
                best_val = val
                best_action = action
            beta = min(beta, best_val)
        return best_action


def max_value(board, alpha, beta):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action), alpha, beta))
        alpha = max(alpha, v)
        if alpha >= beta:
            break
    return v


def min_value(board, alpha, beta):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action), alpha, beta))
        beta = min(beta, v)
        if alpha >= beta:
            break
    return v