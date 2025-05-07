# my_list = [1, 2, 3, 4, 5, 6]
# my_list = [1, 2, 3]
my_list = [1, 2, 3, 4, 5]
# my_list = [1]
# my_list = []
if my_list:
    last_elem1 = my_list.pop()
    my_list.insert(0, last_elem1)

print(my_list)

pass
