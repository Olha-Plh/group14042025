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
purchase_plan.pop()  # відобразили останній доданий елемент
purchase_plan.pop(0)  # відобразили перший доданий елемент


if "cake" in purchase_plan:
    purchase_plan.remove("cake")

if "abc" in "abcde":
    print(32323232)


# example_while (for the task 4.3)

# цикл while показує, що ми аналізуємо щось, що може працювати безкінечно.
# якщо буде while True: (і потім print () ) - то це означає, що правда, що число не = 0, не пустий список, результат
# якоїсь умови, де відповідь буде True - буде йти по колу і друкувати відповідь постійно

TARGET_COUNTER = 3

# Якщо потрібно, щоб на потрібному значенні зупинилось, тоді:
flag = True
counter = 0  # якщо потрібно, щоб while відпрацював 1000 разів

while flag:
    print(111)
    counter += 1  # кожен раз додавати одиницю
    # якщо хочемо зробити вибірку (все, що зверху вказано робимо, а що ниже не виконуємо, поки
    # не виконаємо умову (тобто йдемо на наступ цикл) (тобто, буде тільки 2 рази в нашому прикладі відображати результат)):
    if counter == 2:
        continue
    # звичайне продовження до стрічки 65, якщо не потрібно нічого:
    if counter == TARGET_COUNTER:
        flag = False
        print("bye")
    # якщо потрібно вийти з циклу і закінчити роботу, тоді після рядка 65 - це:
    if counter >= TARGET_COUNTER:
        break

# example_random (for the task 4.3)
# random  - числове рандомне значення

import random

random.seed("jdhjs")  # кажемо "бери за основу це"
print(random.randint(1, 56))  # обери від 1 до 56 рандомне число
print(random.random())  # обери рандомне число до 1 ( 1 не входить, 0 входить)
print(random.random() * 10000000000)  # обери рандомне число з десятими після коми

choices = [55, 678, 1289]  # вибір з цих трьох чисел
print(random.choice(choices))


# example_range(for the task 4.3)
for elem in range(10):
    print(elem)


pass
