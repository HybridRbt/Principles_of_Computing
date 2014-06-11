__author__ = 'jeredyang'

# val1 = [1, 2, 3]
# val2 = val1[1:]
# val1[2] = 4
#
# print val2[1]
#
# a = dict(None)
# print a


def appendsums(lst):
    """
    Repeatedly append the sum of the current last three elements of lst to lst. loop for 25 times
    """
    for times in range(0, 25):
        new_add = sum(lst[len(lst) - 3:])
        lst.append(new_add)

    return lst

sum_three = [0, 1, 2]
appendsums(sum_three)
print sum_three[10]