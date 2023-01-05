"""
Tic Tac Toe Player
"""

import math

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
                if element == "X":
                    empty_spots.append((i, j))

    return empty_spots


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Get the row and column of the action
    row = action[0]
    col = action[1]
    # If the player is "O", place an "O" at the action location on the board.
    board[row][col] = player(board)
    return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Check to see if someone has won horizontally
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != EMPTY:
            return True
    
    # Check to see if someone has won vertically
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != EMPTY:
            return True
    
    # Check to see if someone has won diagonally 
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return True
    
    # Check for draw
    for row in board:
        if EMPTY in row:
            return True
    
    # If nobody has won and if there isn't a draw, then the game isn't over
    return False



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
    raise NotImplementedError
