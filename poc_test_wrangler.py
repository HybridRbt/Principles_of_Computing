import poc_wrangler as pw

list_of_list = ['', 'a', 'bcdef', 'abbbbbbcddddde']
for index in range(len(list_of_list)):
    print list_of_list[index]
    print pw.remove_duplicates(list_of_list[index])