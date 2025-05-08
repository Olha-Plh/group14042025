some_string = "I live in Odessa since 2004"
other_result = some_string.split("i")
other_result_visual = ["I", "live", "in", "Odessa", "since", "2004"]

empty_list = []

if empty_list:
    print(5555555)

not_empty_list = ["4544", 5544, 5.5, True, False, [55], empty_list]
if not_empty_list:  # отримуємо, тому що є хоч 1 елемент
    print(222222)

fifth_elem = not_empty_list[4]  # 5 елемент
# big_elem = not_empty_list[40]
fifth_letter = some_string[4]  # 4 індекс по порядку
len_list = len(not_empty_list)
len_list2 = len(empty_list)
len_string = len(some_string)

##########
purchase_plan = ["banana"]

# add 1 elem
purchase_plan.append("salt")
purchase_plan.append("salt")
purchase_plan.append("2")

# merge by another list
sister_plan = ["bread", "milk"]
purchase_plan.extend(sister_plan)

purchase_plan.sort()
purchase_plan.sort(reverse=True)
purchase_plan.sort(key=len, reverse=True)  # число 2 перемістили в кінець з середини

# delete item
purchase_plan.remove("salt")

# delete by index
last_elem = purchase_plan.pop()
purchase_plan.pop()  # відобразили останній доданий елемент
purchase_plan.pop(0)  # відобразили перший доданий елемент

purchase_plan.insert(1, 55555555)

if "cake" in purchase_plan:
    purchase_plan.remove("cake")

if "abc" in "abcde":
    print(32323232)

pass
