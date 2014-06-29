__author__ = 'jeredyang'

"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
# import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# Change as desired
NTRIALS = 1000  # Number of trials to run
MCMATCH = 1.0  # Score for squares played by the machine player
MCOTHER = 1.0  # Score for squares played by the other player


def get_max_value(dictionary):
    """
    a helper function, takes in a dictionary, compare all its values and find the max, and return it along with its key
    :param dictionary:
    :return: tuple (key, value)
    """
    temp = []
    for key, value in dictionary.items():
        temp.append((value, key))

    return sorted(temp)[-1]


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
    :param: scores: a list of scores
    :param: board
    :param: player: current player
    """
    result = board.check_win()
    scores = list_to_dict(scores)
    # machine player is "player"
    if result is None:  # still in progress, do nothing
        return
    elif result == provided.DRAW:  # tie, do nothing
        return

    if result == player:  # machine player wins
        # update scores
        for row_index in range(board.get_dim()):
            for col_index in range(board.get_dim()):
                if board.square(row_index, col_index) == player:  # this square gets MCMATCH
                    scores[(row_index, col_index)] += MCMATCH
                elif board.square(row_index, col_index) == provided.EMPTY:  # gets 0
                    scores[(row_index, col_index)] += 0
                else:
                    scores[(row_index, col_index)] -= MCOTHER
    else:  # machine player loses
        # update scores
        for row_index in range(board.get_dim()):
            for col_index in range(board.get_dim()):
                if board.square(row_index, col_index) == player:  # this square gets MCMATCH
                    scores[(row_index, col_index)] -= MCMATCH
                elif board.square(row_index, col_index) == provided.EMPTY:  # gets 0
                    scores[(row_index, col_index)] += 0
                else:
                    scores[(row_index, col_index)] += MCOTHER


def list_to_dict(scores):
    """
    convert input score list to score dictionary
    :param scores: a list
    :return: a score dictionary
    """
    score_dict = {}
    for row_index in range(len(scores)):  # first level
        for col_index in range(len(scores[row_index])):  # second level
            score_dict[(row_index, col_index)] = score_dict.get((row_index, col_index), scores[row_index][col_index])

    return score_dict


def get_best_move(board, scores):
    """
    Takes a current board and a grid of scores. The function should find all of the empty squares with the maximum
    score and randomly return one of them as a (row, column) tuple. It is an error to call this function with a board
    that has no empty squares (there is no possible next move), so your function may do whatever it wants in that
    case. The case where the board is full will not be tested.
    :param: board: a board instance
    :param: scores: a list
    """
    scores = list_to_dict(scores)
    available_moves = board.get_empty_squares()
    if len(available_moves) == 0:  # no available moves
        return

    temp_dict = {}
    for each_move in available_moves:
        # form a temp dictionary of available squares
        temp_dict[each_move] = temp_dict.get(each_move, scores[each_move])

    best_move = get_max_value(temp_dict)[1]

    return best_move


def mc_move(board, player, trials):
    """
    Takes a current board, which player the machine player is, and the number of trials to run. The function should
    use the Monte Carlo simulation described above to return a move for the machine player in the form of a (row,
    column) tuple. Be sure to use the other functions you have written!
    """
    number_of_trials = trials
    scores = {}

    # initialize scores dictionary
    for row_index in range(board.get_dim()):
        for col_index in range(board.get_dim()):
            scores[(row_index, col_index)] = scores.get((row_index, col_index), 0)

    while number_of_trials > 0:
        temp_board = board.clone()
        mc_trial(temp_board, player)
        mc_update_scores(scores, temp_board, player)
        number_of_trials -= 1

    next_move = get_best_move(board, scores)
    return next_move


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

# provided.play_game(mc_move, NTRIALS, False)
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)

# print get_best_move(provided.TTTBoard(2, False, [[provided.EMPTY, provided.EMPTY], [provided.EMPTY, provided.EMPTY]]),
#               [[0, 0], [3, 0]])
# expected one tuple from [(1, 0)]
