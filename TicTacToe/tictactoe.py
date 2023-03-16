"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    numX=0
    numO=0
    for row in board:
        for cell in row:
            if cell==X:
                numX +=1
            elif cell==O:
                numO +=1

    if numX>numO:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    pos_actions = set()
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == EMPTY:
                pos_actions.add((i, j))
                
    return pos_actions



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action[0]<0 or action[1]<0 or action[0]>2 or action[1]>2 or board[action[0]][action[1]] is not EMPTY:
        raise NameError("This action is not valid")
        
    
    result = copy.deepcopy(board)
    result[action[0]][action[1]] = player(board)
    return result

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # check rows
    for row in board:
       if row[0] == row[1] == row[2] and row[0] != EMPTY:
           return row[0]

   # check columns
    for col in range(3):
       if board[0][col] == board[1][col] == board[2][col] and board[0][col] != EMPTY:
           return board[0][col]

   # check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
       return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
       return board[0][2]

    return None    

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if(winner(board) is not None or len(actions(board))==0 ):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if(winner(board)==X):
        return 1
    elif(winner(board)==O):
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:
            value, move = max_value(board)
            return move
        else:
            value, move = min_value(board)
            return move


def max_value(board):
    if terminal(board):
        return utility(board), None

    v = float('-inf')
    move = None
    for action in actions(board):
        # v = max(v, min_value(result(board, action)))
        new_v, new_action = min_value(result(board, action))
        if new_v > v:
            v = new_v
            move = action
            if v == 1:
                return v, move

    return v, move


def min_value(board):
    if terminal(board):
        return utility(board), None

    v = float('inf')
    move = None
    for action in actions(board):
        # v = max(v, min_value(result(board, action)))
        new_v, new_action = max_value(result(board, action))
        if new_v < v:
            v = new_v
            move = action
            if v == -1:
                return v, move

    return v, move
