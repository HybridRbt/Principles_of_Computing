import poc_wrangler as pw

# test for remove_dup
def test1():
    list_of_list = ['', 'a', 'bcdef', 'abbbbbbcddddde']
    for index in range(len(list_of_list)):
        print list_of_list[index]
        print pw.remove_duplicates(list_of_list[index])


# test for intersect
def test2():
    l1 = 'abccde'
    l2 = 'bcccdeef'

    print str(l1) + '\n' + str(l2)
    print pw.intersect(l1, l2)


# test for intersect
def test21():
    l1 = ''
    l2 = 'bcccdeef'

    print str(l1) + '\n' + str(l2)
    print pw.intersect(l1, l2)


# test for intersect
def test22():
    l1 = 'a'
    l2 = 'bcccdeef'

    print str(l1) + '\n' + str(l2)
    print pw.intersect(l1, l2)


# test for merge
def test3():
    l1 = '12345'
    l2 = '35789'

    print str(l1) + '\n' + str(l2)
    print pw.merge(l1, l2)

# test for merge
def test31():
    l1 = ''
    l2 = '35789'

    print str(l1) + '\n' + str(l2)
    print pw.merge(l1, l2)

# test for merge
def test32():
    l1 = ''
    l2 = ''

    print str(l1) + '\n' + str(l2)
    print pw.merge(l1, l2)

# test for merge_sort
def test33():
    l1 = '456816327810'

    print l1
    print pw.merge_sort(l1)


# test for gen_all_strings
def test34():
    l1 = 'aab'

    print l1
    print sorted(pw.gen_all_strings(l1))


test34()
print sorted(["", "b", "a", "ab", "ba", "a", "ab", "ba", "aa", "aa", "aab", "aab", "aba", "aba", "baa", "baa"])



