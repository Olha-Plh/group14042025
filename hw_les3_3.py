from itertools import batched

my_list = [1, 2, 3, 4, 5, 6]
# my_list = [1, 2, 3]
# my_list = [1, 2, 3, 4, 5]
# my_list = [1]
# my_list = []
for batch in batched("123456", 6):
    print(batch)

some_list = [1, 2, 3, 4, 5, 6]
some_list = [1, 2, 3]
some_list = [1, 2, 3, 4, 5]
some_list = [1]
some_list = []
some_string = some_list
list_from_string = list(some_string)
slice_data = list_from_string[0:]

if len(some_list) == 0:
    result = [[], []]  # нічого не робити
elif len(some_list) % 2 == 0:  # чотна кількість
    half = len(some_list) // 2
    result = [some_list[:half], some_list[half:]]
else:  # якщо не чотна кількість
    half = len(some_list) // 2 + 1
    result = [some_list[:half], some_list[half:]]


pass
