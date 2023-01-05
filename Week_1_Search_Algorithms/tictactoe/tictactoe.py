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
    Returns player (X or O) who has the next turn on a board.
    """
    # If it is the end, return none
    if terminal(board):
        return None
    # If there are more X's, return O, and vise versa
    x_count = 0
    o_count = 0
    for row in board:
        for element in row:
            if element == "X":
                x_count += 1
            elif element == "O":
                o_count += 1
        
    if o_count < x_count:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    empty_spots = []       
    for i, row in enumerate(board):
            for j, element in enumerate(row):
                if element == EMPTY:
                    empty_spots.append((i, j))

    return empty_spots


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # If action is not a valid action for the board, raise an exception.
    if action[0] not in [0,1,2] or action[1] not in [0,1,2]:
        raise ValueError

    # Creating a deep copy so that I don't modify the real board during minimax
    deep_copy_board = copy.deepcopy(board)
    # Get the row and column of the action
    row = action[0]
    col = action[1]
    # If the player is "O", place an "O" at the action location on the board.
    deep_copy_board[row][col] = player(deep_copy_board)
    return deep_copy_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check to see if someone has won horizontally
    for row in board:
        if (row[0] == row[1] == row[2] == X):
            return X
        elif (row[0] == row[1] == row[2] == O):
            return O
    # Check to see if someone has won vertically
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == X:
            return X
        elif board[0][col] == board[1][col] == board[2][col] == O:
            return O
    
    # Check to see if someone has won diagonally 
    if board[0][0] == board[1][1] == board[2][2] == X:
        return X
    elif board[0][2] == board[1][1] == board[2][0] == X:
        return X
    elif board[0][0] == board[1][1] == board[2][2] == O:
        return O
    elif board[0][2] == board[1][1] == board[2][0] == O:
        return O

    # If no winner, return none
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # If utility != 0, the game has been won
    if utility(board) != 0:
        return True

    # Check for initial board
    if board == initial_state():
        return False

    # If utility is zero, but there is an empty spot, not terminal
    for row in board:
        if EMPTY in row:
            return False

    # Otherwise, full board -> terminal
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise. 
    """
    # Get the next player, and if the game has been won, the winner was the last player
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0
        


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # If the game is over, do nothing
    if terminal(board):
        return None

    # If player X is choosing, maximize utility
    elif player(board) == X:
        # Set the initial best value to negative infinity (or some very negative number)
        best_val = -math.inf
        best_move = None
        # Find the best action using minimax
        for action in actions(board):
            val = min_value(result(board, action))
            if val > best_val:
                best_val = val
                best_move = action
        return best_move
    # If it is O's turn, minimize 
    else:
        best_val = math.inf
        best_move = None
        for action in actions(board):
            val = max_value(result(board, action))
            if val < best_val:
                best_val = val
                best_move = action
        return best_move

def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v

def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v
