"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
# import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# Change as desired
NTRIALS = 100  # Number of trials to run
MCMATCH = 1.0  # Score for squares played by the machine player
MCOTHER = 1.0  # Score for squares played by the other player


def sort_dict_by_value(dictionary):
    """
    a helper function, takes in a dictionary, compare all its values and sort from max to min
    :param dictionary:
    :return: tuple (key, value)
    """
    temp = []
    for key, value in dictionary.items():
        temp.append((value, key))

    return sorted(temp, reverse=True)


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


def update_scores_win(board, scores, player):
    """
    update scores when player wins
    :param board:
    :param scores:
    :param player:
    :return: void
    """
    for row_index in range(board.get_dim()):
        for col_index in range(board.get_dim()):
            if board.square(row_index, col_index) == player:  # this square gets MCMATCH
                scores[row_index][col_index] += MCMATCH
            elif board.square(row_index, col_index) == provided.EMPTY:  # gets 0
                scores[row_index][col_index] += 0
            else:
                scores[row_index][col_index] -= MCOTHER


def update_scores_lose(board, scores, player):
    """
    upadte scores when player lose
    :param board:
    :param scores:
    :param player:
    :return: void
    """
    for row_index in range(board.get_dim()):
        for col_index in range(board.get_dim()):
            if board.square(row_index, col_index) == player:  # this square gets -MCMATCH
                scores[row_index][col_index] -= MCMATCH
            elif board.square(row_index, col_index) == provided.EMPTY:  # gets 0
                scores[row_index][col_index] += 0
            else:
                scores[row_index][col_index] += MCOTHER


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
    # machine player is "player"
    if result is None:  # still in progress, do nothing
        return
    elif result == provided.DRAW:  # tie, do nothing
        return

    if result == player:  # machine player wins
        # update scores
        update_scores_win(board, scores, player)
    else:  # machine player loses
        # update scores
        update_scores_lose(board, scores, player)


# def check_row(board, move):
#     """
#     check row
#     :param board:
#     :param move: move[1] is the nex move
#     :return:
#     """
#     row_list = []
#     for col in range(board.get_dim()):
#         if board.square(move[1][0], col) != provided.EMPTY:  # if this square is not empty
#             row_list.append(board.square(move[1][0], col))
#
#     check_dup_in_list(row_list)
#
#     return count > 1


# def check_col(board, move):
#     """
#     check col
#     :param board:
#     :param move: move[1] is the next move
#     :return:
#     """
#     count = 0
#     for row in range(board.get_dim()):
#         if board.square(row, move[1][1]) != provided.EMPTY:  # if this square is not empty
#             count += 1
#
#     return count > 1
#
#
# def check_dia(board, move):
#     """
#     check diag
#     :param board:
#     :param move: move[1] is the next move
#     :return:
#     """
#     critical = False
#
#     # get the diags
#     diag1 = [(idx, idx) for idx in range(board.get_dim())]
#     diag2 = [(idx, board.get_dim() - idx - 1)
#              for idx in range(board.get_dim())]
#
#     # check diag1 first
#     count = 0
#     for pos in diag1:
#         if board.square(pos[0], pos[1]) != provided.EMPTY:  # if this square is not empty
#             count += 1
#
#     if count > 1 and move[1] in diag1:  # this move is critical
#         critical = True
#
#     # check diag2
#     count = 0
#     for pos in diag2:
#         if board.square(pos[0], pos[1]) != provided.EMPTY:  # if this square is not empty
#             count += 1
#
#     if count > 1 and move in diag2:  # this move is critical
#         critical = True
#
#     return critical
#
#
# def check_for_double(board, move):
#     """
#     helper function to check double. call check_row, check_col, and check_dia
#     :param move:
#     :return: bool
#     """
#     return check_row(board, move) or check_col(board, move) or check_dia(board, move)


def get_best_move(board, scores):
    """
    Takes a current board and a grid of scores. The function should find all of the empty squares with the maximum
    score and randomly return one of them as a (row, column) tuple. It is an error to call this function with a board
    that has no empty squares (there is no possible next move), so your function may do whatever it wants in that
    case. The case where the board is full will not be tested.
    :param: board: a board instance
    :param: scores: a list
    """
    available_moves = board.get_empty_squares()
    if len(available_moves) == 0:  # no available moves
        return

    temp_dict = {}
    for each_move in available_moves:
        # form a temp dictionary of available squares
        temp_dict[each_move] = temp_dict.get(each_move, scores[each_move[0]][each_move[1]])

    # get a list of moves
    move_list = sort_dict_by_value(temp_dict)

    # need to deal w/ equals
    temp_best_move_score = move_list[0][0]

    temp_compare_list = []
    for each_move in move_list:
        if each_move[0] == temp_best_move_score:  # a new competitor
            # add to list
            temp_compare_list.append(each_move)

    ran_index = random.randrange(0, len(temp_compare_list))
    best_move = temp_compare_list[ran_index][1]

    return best_move


# def check_next_move(board, player, next_move):
#     temp_compare_list = []
#     for each_move in move_list:
#         if each_move[0] == temp_best_move_score:  # a new competitor
#             # add to list
#             temp_compare_list.append(each_move)
#
#     for each_move in temp_compare_list:
#         if check_for_double(board, each_move):  # check if there are two squares occupied already, if yes
#             # this move is top priority
#             best_move = each_move[1]
#             break


def mc_move(board, player, trials):
    """
    Takes a current board, which player the machine player is, and the number of trials to run. The function should
    use the Monte Carlo simulation described above to return a move for the machine player in the form of a (row,
    column) tuple. Be sure to use the other functions you have written!
    """
    number_of_trials = trials
    temp_list = [0] * board.get_dim()
    scores = [temp_list] * board.get_dim()

    # this gets complained by OwlTest
    # initialize scores dictionary
    # for row_index in range(board.get_dim()):
    #     temp_list = []d
    #     for col_index in range(board.get_dim()):
    #         temp_list.append(0)
    #     scores.append(temp_list)

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
# [[0, 0], [3, 0]])
# expected one tuple from [(1, 0)]

# print mc_move(provided.TTTBoard(3, False, [[provided.PLAYERX, provided.PLAYERX, provided.PLAYERO],
# [provided.PLAYERO, provided.PLAYERX, provided.PLAYERX],
# [provided.PLAYERO, provided.EMPTY, provided.PLAYERO]]),
# provided.PLAYERX, NTRIALS)
#
# print mc_move(provided.TTTBoard(3, False, [[provided.PLAYERX, provided.PLAYERX, provided.PLAYERO],
#                                            [provided.EMPTY, provided.PLAYERX, provided.PLAYERX],
#                                            [provided.PLAYERO, provided.EMPTY, provided.PLAYERO]]),
#               provided.PLAYERO, NTRIALS)
#
# sc = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# mc_update_scores(sc, provided.TTTBoard(3, False, [[provided.PLAYERX,
#                                                    provided.PLAYERX,
#                                                    provided.PLAYERO],
#                                                   [provided.PLAYERO,
#                                                    provided.PLAYERX,
#                                                    provided.EMPTY],
#                                                   [provided.EMPTY,
#                                                    provided.PLAYERX,
#                                                    provided.PLAYERO]]), 2)
# print sc
# expected [[1.0, 1.0, -1.0], [-1.0, 1.0, 0], [0, 1.0, -1.0]] but
# received [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# print mc_move(provided.TTTBoard(3, False, [[provided.PLAYERX, provided.EMPTY, provided.EMPTY],
#                                            [provided.PLAYERO, provided.PLAYERO, provided.EMPTY],
#                                            [provided.EMPTY, provided.PLAYERX, provided.EMPTY]]),
#               provided.PLAYERX, NTRIALS)