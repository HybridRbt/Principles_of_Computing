"""
Mini-max Tic-Tac-Toe Player
"""

# import poc_ttt_gui
import poc_ttt_provided as provided

# Set timeout, as mini-max can take a long time
#import codeskulptor
# codeskulptor.set_timeout(160)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}

def mm_move(board, player):
    """
    Make a move on the board.

    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """
    # always maximizing.
    # initialize answers
    if board.check_win() != None:
        return SCORES[board.check_win()], (-1, -1)

    empty_square = board.get_empty_squares()

    final = (-1, (-1, -1))
    # else recursively compute scores
    for each_square in empty_square:
        new_board = board.clone()
        new_board.move(each_square[0], each_square[1], player)

        new_player = provided.switch_player(player)
        score = mm_move(new_board, new_player)[0]
        move = (each_square[0], each_square[1])

        if score * SCORES[player] == 1:
            # this move wins, return corresponding score
            return score, move
        elif score * SCORES[player] > final[0]:
            final = (score, move)
        elif final[0] == -1:
            final = (final[0], move)

    return final[0] * SCORES[player], final[1]


def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

#provided.play_game(move_wrapper, 1, False)
# poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)
