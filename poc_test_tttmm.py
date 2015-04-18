__author__ = 'JeredYang'

import poc_tttmm as tm

test_board = tm.provided.TTTBoard(3)

def clear_borad(board):
    board = tm.provided.TTTBoard(3)
    return board
#O | X |
#---------
#O | X |
#---------
#  | O | X
def fill_board1():
    test_board.move(0, 0, tm.provided.PLAYERO)
    test_board.move(1, 0, tm.provided.PLAYERO)
    test_board.move(2, 1, tm.provided.PLAYERO)
    test_board.move(0, 1, tm.provided.PLAYERX)
    test_board.move(1, 1, tm.provided.PLAYERX)
    test_board.move(2, 2, tm.provided.PLAYERX)

#O | X |
#---------
#O | X | X
#---------
#  | O | X
def fill_board2():
    test_board.move(0, 0, tm.provided.PLAYERO)
    test_board.move(1, 0, tm.provided.PLAYERO)
    test_board.move(2, 1, tm.provided.PLAYERO)
    test_board.move(0, 1, tm.provided.PLAYERX)
    test_board.move(1, 1, tm.provided.PLAYERX)
    test_board.move(2, 2, tm.provided.PLAYERX)
    test_board.move(1, 2, tm.provided.PLAYERX)

def fill_board4():
    test_board.move(0, 0, tm.provided.PLAYERX)
    test_board.move(1, 0, tm.provided.PLAYERO)
    test_board.move(1, 1, tm.provided.PLAYERO)
    test_board.move(2, 1, tm.provided.PLAYERX)

def fill_board5():
    test_board.move(0, 0, tm.provided.PLAYERX)
    test_board.move(1, 0, tm.provided.PLAYERO)
    test_board.move(1, 1, tm.provided.PLAYERO)
    test_board.move(2, 1, tm.provided.PLAYERX)
    # test_board.move(2, 2, tm.provided.PLAYERX)

def test_tttmm1():
    fill_board1()
    print "Test board after initialization:\n" + str(test_board)

    # 1st for x
    move = tm.mm_move(test_board, tm.provided.PLAYERX)[1]
    test_board.move(move[0], move[1], tm.provided.PLAYERX)
    print "Best move for X:\n" + str(test_board)

    # 1st for o
    move = tm.mm_move(test_board, tm.provided.PLAYERO)[1]
    test_board.move(move[0], move[1], tm.provided.PLAYERO)
    print "Best move for O:\n" + str(test_board)

def test_tttmm2():
    fill_board2()
    print "Test board after initialization:\n" + str(test_board)

    # 1st for o
    move = tm.mm_move(test_board, tm.provided.PLAYERO)[1]
    test_board.move(move[0], move[1], tm.provided.PLAYERO)
    print "Best move for O:\n" + str(test_board)

    # 1st for x
    move = tm.mm_move(test_board, tm.provided.PLAYERX)[1]
    test_board.move(move[0], move[1], tm.provided.PLAYERX)
    print "Best move for X:\n" + str(test_board)

def test_tttmm3():
    test_board = tm.provided.TTTBoard(2)
    print "Test board after initialization:\n" + str(test_board)

    # 1st for o
    score, move = tm.mm_move(test_board, tm.provided.PLAYERO)
    print score
    test_board.move(move[0], move[1], tm.provided.PLAYERO)
    print "Best move for O:\n" + str(test_board)

    # 1st for x
    # move = tm.mm_move(test_board, tm.provided.PLAYERX)[1]
    # test_board.move(move[0], move[1], tm.provided.PLAYERX)
    # print "Best move for X:\n" + str(test_board)

def test_tttmm4():
    fill_board4()
    print "Test board after initialization:\n" + str(test_board)

    # 1st for x
    score, move = tm.mm_move(test_board, tm.provided.PLAYERX)
    print score
    test_board.move(move[0], move[1], tm.provided.PLAYERX)
    print "Best move for x:\n" + str(test_board)

    # 1st for x
    # move = tm.mm_move(test_board, tm.provided.PLAYERX)[1]
    # test_board.move(move[0], move[1], tm.provided.PLAYERX)
    # print "Best move for X:\n" + str(test_board)

def test_tttmm5():
    fill_board5()
    print "Test board after initialization:\n" + str(test_board)

    # 1st for x
    score, move = tm.mm_move(test_board, tm.provided.PLAYERX)
    print score
    test_board.move(move[0], move[1], tm.provided.PLAYERX)
    print "Best move for x:\n" + str(test_board)

def test_tttmm6():
    test_board = tm.provided.TTTBoard(2)
    print "Test board after initialization:\n" + str(test_board)

    # 1st for x
    score, move = tm.mm_move(test_board, tm.provided.PLAYERX)
    print score
    test_board.move(move[0], move[1], tm.provided.PLAYERX)
    print "Best move for x:\n" + str(test_board)

def test_check_win():
    test_board = tm.provided.TTTBoard(2)
    print "Test board after initialization:\n" + str(test_board)

    # 1st for o
    test_board.move(0, 0, tm.provided.PLAYERO)
    test_board.check_win()

    test_board = clear_borad(test_board)

    # 1st for x
    test_board.move(0, 0, tm.provided.PLAYERX)
    test_board.check_win()


#test_tttmm1()
#test_board = clear_borad(test_board)
# test_tttmm5()
# test_tttmm6()
test_board = tm.provided.TTTBoard(3, False, [[tm.provided.PLAYERX, tm.provided.EMPTY, tm.provided.EMPTY],
                                             [tm.provided.PLAYERO, tm.provided.PLAYERO, tm.provided.EMPTY],
                                             [tm.provided.EMPTY, tm.provided.PLAYERX, tm.provided.EMPTY]])
print test_board
result = tm.mm_move(test_board, tm.provided.PLAYERO)
print result