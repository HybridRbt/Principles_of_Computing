"""
Mini-max Tic-Tac-Toe Player
"""

# import poc_ttt_gui
import poc_ttt_provided as provided

# Set timeout, as mini-max can take a long time
#import codeskulptor
#codeskulptor.set_timeout(60)

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
    score = provided.PLAYERX
    move = (-1, -1)
    new_board = board.clone()

    empty_square = new_board.get_empty_squares()
    if len(empty_square) == 1:
        # only one choice, make this move
        new_board.move(empty_square[0][0], empty_square[0][1], player)
        move = (empty_square[0][0], empty_square[0][1])
        # check if this move wins
        if new_board.check_win() != None:
            # check only when the game is finished
            if new_board.check_win() == provided.DRAW:
                # this move draws, return draw
                score = provided.DRAW
            elif new_board.check_win() == player:
                # this move wins, return corresponding score
                score = SCORES[player]
            elif new_board.check_win() != player:
                score = SCORES[player]
            return score, move

    # else recursively compute scores
    for each_square in empty_square:
        new_board.move(each_square[0], each_square[1], player)
        move = (each_square[0], each_square[1])
        if mm_move(new_board, provided.switch_player(player))[0] == SCORES[player]:
            # this move wins, return corresponding score
            score = SCORES[player]
            return score, move
        else:
            if mm_move(new_board, provided.switch_player(player))[0] == SCORES[provided.DRAW]:
                # this move draws, return draw
                score = provided.DRAW
            else:
                score = SCORES[player]
            return score, move



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
