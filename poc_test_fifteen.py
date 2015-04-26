__author__ = 'jeredyang'

import poc_fifteen as pff


def test_lower_invariant():
    p22 = pff.Puzzle(2, 2)
    print p22

    p22.update_puzzle("rdlu")
    print p22

    assert p22.lower_row_invariant(0, 0) == True
    print "Pass"

def run_tests():
    test_lower_invariant()

run_tests()