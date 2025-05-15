# my_elem = "1, 3, 5"
my_elem = "6"
# my_elem = ''

if my_elem == "":
    print(0)
else:
    my_list = my_elem.split(",")
    my_list = [int(num) for num in my_list]

    total = 0
    for index, number in enumerate(my_list):
        if index % 2 == 0:
            total += number

    result = total * my_list[-1]
    print(result)


pass
