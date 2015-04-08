import poc_wrangler as pw


def test1():
    list_of_list = ['', 'a', 'bcdef', 'abbbbbbcddddde']
    for index in range(len(list_of_list)):
        print list_of_list[index]
        print pw.remove_duplicates(list_of_list[index])


def test2():
    l1 = 'abccde'
    l2 = 'bcccdeef'

    print str(l1) + '\n' + str(l2)
    print pw.intersect(l1, l2)


def test21():
    l1 = ''
    l2 = 'bcccdeef'

    print str(l1) + '\n' + str(l2)
    print pw.intersect(l1, l2)


def test22():
    l1 = 'a'
    l2 = 'bcccdeef'

    print str(l1) + '\n' + str(l2)
    print pw.intersect(l1, l2)


test22()