__author__ = 'jeredyang'

import poc_fifteen as pff


def test_lower_invariant():
    p22 = pff.Puzzle(2, 2)
    # example from website
    p44 = pff.Puzzle(4, 4, [[4, 2, 3, 7], [8, 5, 6, 10], [9, 1, 0, 11], [12, 13, 14, 15]])
    print p44

    # p22.update_puzzle("rdlu")
    # print p22

    # assert p22.lower_row_invariant(0, 0) == True
    assert p44.lower_row_invariant(2, 2) == True
    print "Pass"

def test_solve_interior_tile():
    p44 = pff.Puzzle(4, 4, [[4, 13, 1, 3], [5, 10, 2, 7], [8, 12, 6, 11], [9, 0, 14, 15]])
    print p44
    assert p44.lower_row_invariant(3, 1) == True
    p44.solve_interior_tile(3, 1)
    assert p44.lower_row_invariant(3, 0) == True
    print p44
    print "Pass"

def run_tests():
    test_lower_invariant()
    test_solve_interior_tile()


run_tests()