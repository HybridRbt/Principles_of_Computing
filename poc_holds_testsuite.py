"""
Test suite for gen_all_holds in "Yahtzee"
"""

import poc_simpletest


def run_suite(gen_all_holds):
    """
    Some informal testing code for gen_all_holds
    """

    # create a TestSuite object
    suite = poc_simpletest.TestSuite()

    # test gen_all_holds on various inputs
    hand = tuple([])
    suite.run_test(gen_all_holds(hand), set([()]), "Test #1:")

    hand = tuple([4, 2])
    suite.run_test(gen_all_holds(hand), set([(), (4,), (2,), (4, 2)]), "Test #2:")

    hand = tuple((1, 2, 2))
    suite.run_test(gen_all_holds(hand), set([(), (1,), (2,), (1, 2), (2, 2), (1, 2, 2)]), "Test #3:")

    hand = tuple((2, 1, 2))
    suite.run_test(gen_all_holds(hand), set([(), (1,), (2,), (1, 2), (2, 1), (2, 2), (2, 1, 2)]), "Test #4:")

    hand = tuple([6, 2, 3])
    suite.run_test(gen_all_holds(hand), set([(), (6,), (2,), (6, 2), (3,), (6, 3), (2, 3), (6, 2, 3)]), "Test #5:")

    suite.report_results()





