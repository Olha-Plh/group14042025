# my_list = "0, 1, 0, 12, 3"
# my_list = "0"
# my_list = "1, 0, 13, 0, 0, 0, 5"
my_list = "9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0"

my_list = my_list.split(",")
my_list = [int(num.strip()) for num in my_list]

zeros = []
not_zeros = []

for number in my_list:
    if number == 0:
        zeros.append(number)
    else:
        not_zeros.append(number)
result = not_zeros + zeros
print(result)

pass
