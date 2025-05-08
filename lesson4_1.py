some_list = [55, 666] * 6
some_string = "133xjbjxk"
list_from_string = list(some_string)

elements_in_some_string = len(some_string)
elements_in_some_list = len(list_from_string)

slice_data = list_from_string[0:]

# All
list_with_data = [22, 555, 66, 55]
all_true = all(list_with_data)  # перевірка, чи всі елементи правдоподібні
at_least_one = any(list_with_data)  # перевірка, чи хоч один елемент істинний

maximum = max(some_list)
minimum = min(some_list)
summa = sum(some_list)
summa1 = sum(some_list, start=10)  # start - мінімальньна сума

some_str_list = ["ddhbshdddddwh", "dunxiki", "kokl"]
max_str = max(some_str_list, key=len)  # key -функція для визначення довжини
min_str = min(some_str_list, key=len)
pass
