__author__ = 'jeredyang'

"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
# import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# Change as desired
NTRIALS = 1  # Number of trials to run
MCMATCH = 1.0  # Score for squares played by the machine player
MCOTHER = 1.0  # Score for squares played by the other player


def mc_trial(board, player):
    """
    Takes a current board and the next player to move. The function should play a game starting with the given player
    by making random moves, alternating between players. The function should return when the game is over. The modified
    board will contain the state of the game, so the function does not return anything.
    """
    next_player = player
    while board.check_win() is None:
        # while game is in progress
        # get next player and next move
        next_move = pick_next_move_random(board)
        board.move(next_move[0], next_move[1], next_player)
        next_player = provided.switch_player(next_player)  # switch player and repeat


def mc_update_scores(scores, board, player):
    """
    Takes a grid of scores (a list of lists) with the same dimensions as the Tic-Tac-Toe board, a board from a completed
    game, and which player the machine player is. The function should score the completed board and update the scores
    grid. As the function updates the scores grid directly, it does not return anything,
    """
    # machine player is "player"
    board.check_win() == player  # machine player wins

    # update scores
    for each_square in board:
        if board.square(each_square[0], each_square[1]) == player:  # this square gets MCMATCH
            scores[]


def get_best_move(board, scores):
    """
    Takes a current board and a grid of scores. The function should find all of the empty squares with the maximum
    score and randomly return one of them as a (row, column) tuple. It is an error to call this function with a board
    that has no empty squares (there is no possible next move), so your function may do whatever it wants in that
    case. The case where the board is full will not be tested.
    """
    available_moves = board.get_empty_squares()
    if len(available_moves) == 0:  # no available moves
        return

    sort_score = []
    for each_move in available_moves:
        sort_score.append((each_move, scores[each_move]))


def mc_move(board, player, trials):
    """
    Takes a current board, which player the machine player is, and the number of trials to run. The function should
    use the Monte Carlo simulation described above to return a move for the machine player in the form of a (row,
    column) tuple. Be sure to use the other functions you have written!
    """
    number_of_trials = trials
    while number_of_trials > 0:
        mc_trial(board, player)

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


# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

provided.play_game(mc_move, NTRIALS, False)
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
