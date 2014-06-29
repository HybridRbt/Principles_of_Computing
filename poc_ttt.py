__author__ = 'jeredyang'

"""
Monte Carlo Tic-Tac-Toe Player
"""

# class TTTBoard:
# """
# Class to represent a Tic-Tac-Toe board.
# """
#
#
# def __init__(self, dim, reverse = False, board = None):
#     """
#     Initialize the TTTBoard object with the given dimension and
#     whether or not the game should be reversed.
#     """
#
#
# def __str__(self):
#     """
#     Human readable representation of the board.
#     """
#
#
# def get_dim(self):
#     """
#     Return the dimension of the board.
#     """
#
#
# def square(self, row, col):
#     """
#     Return the status (EMPTY, PLAYERX, PLAYERO) of the square at
#     position (row, col).
#     """
#
#
# def get_empty_squares(self):
#     """
#     Return a list of (row, col) tuples for all empty squares
#     """
#
#
# def move(self, row, col, player):
#     """
#     Place player on the board at position (row, col).
#
#     Does nothing if board square is not empty.
#     """
#
#
# def check_win(self):
#     """
#     If someone has won, return player.
#     If game is a draw, return DRAW.
#     If game is in progress, return None.
#     """
#
#
# def clone(self):
#     """
#     Return a copy of the board.
#     """


import random
# import poc_ttt_gui
# import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# Change as desired
NTRIALS = 1  # Number of trials to run
MCMATCH = 1.0  # Score for squares played by the machine player
MCOTHER = 1.0  # Score for squares played by the other player


# Add your functions here.
def play_one_game(board, player):
    """
    play one game until it ends, starts with the given "player", on "board"
    :param board:
    :param player:
    :return:
    """
    playerx_moves = []  # a list of moves with its corresponding scores for playerx
    playero_moves = []  # a list of moves with its corresponding scores for playero

    score_of_moves = {}  # a dictionary recording the scores. use moves as keys

    next_player = player
    while board.check_win() is None:
        # while game is in progress
        # get next player and next move
        next_move = pick_next_move_random(board)

        if next_player == PLAYERX:  # this is for playerx
            # save this move to playerx list
            playerx_moves.append(next_move)
        else:  # this is for playero
            # save this move to playero list
            playero_moves.append(next_move)

        next_player = switch_player(player)  # switch player and repeat

    # game is finished, check the result
    if board.check_win() == PLAYERX:  # playerx has won the game, all playerx moves gets 1


def mc_trial(board, player):
    """
    Takes a current board and the next player to move. The function should play a game starting with the given player
    by making random moves, alternating between players. The function should return when the game is over. The modified
    board [will contain the state of the game, so the function does not return anything.
    """
    number_of_trials = NTRIALS
    while number_of_trials > 0:  # repeat for the desired number of trials
        play_one_game(board, player)  # play one game started by the given player


        number_of_trials -= 1


def mc_update_scores(scores, board, player):
    """
    Takes a grid of scores (a list of lists) with the same dimensions as the Tic-Tac-Toe board, a board from a completed
    game, and which player the machine player is. The function should score the completed board and update the scores
    grid. As the function updates the scores grid directly, it does not return anything,
    """


def get_best_move(board, scores):
    """
    Takes a current board and a grid of scores. The function should find all of the empty squares with the maximum
    score and randomly return one of them as a (row, column) tuple. It is an error to call this function with a board
    that has no empty squares (there is no possible next move), so your function may do whatever it wants in that
    case. The case where the board is full will not be tested.
    """


def mc_move(board, player, trials):
    """
    Takes a current board, which player the machine player is, and the number of trials to run. The function should
    use the Monte Carlo simulation described above to return a move for the machine player in the form of a (row,
    column) tuple. Be sure to use the other functions you have written!
    """


def pick_next_move_random(board):
    """
    randomly pick next move for "player" on current board "board"
    :return: a (row, col) tuple
    """
    # get current available squares
    available_moves = board.get_empty_squares()  # this is a list of (row, col) tuples

    # randomly pick one move from all the available ones
    rand_index = random.randrange(0, len(available_moves))
    next_move = available_moves[rand_index]

    return next_move

def ttt():
    """
    main game logic
    :return: void
    """
    current_board = TTTBoard()  # create a new board
    next_player = PLAYERX # player x will take the first move




# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

# provided.play_game(mc_move, NTRIALS, False)
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
