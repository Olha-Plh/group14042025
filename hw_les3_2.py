# def move_last_to_first(lst):
#     """Переносить останній елемент списку на початок.
#
#     Args:
#         lst (list): Список элементов.
#
#     Returns:
#         list: Новый список с последним элементом, перемещенным на первое место.
#     """
#     # Если список пустой или состоит из одного элемента, возвращаем его как есть
#     if not lst or len(lst) == 1:
#         return lst
#
#     # Переносим последний элемент на первое место
#     last_element = lst.pop()
#     lst.insert(0, last_element)
#
#     return lst
#
#
# # Проверки
# list1 = [12, 3, 4, 10]
# result1 = move_last_to_first(list1.copy())
# print(f"{list1} => {result1}")
#
# list2 = [1]
# result2 = move_last_to_first(list2.copy())
# print(f"{list2} => {result2}")
#
# list3 = []
# result3 = move_last_to_first(list3.copy())
# print(f"{list3} => {result3}")
#
# list4 = [12, 3, 4, 10, 8]
# result4 = move_last_to_first(list4.copy())
# print(f"{list4} => {result4}")


# my_list = [12, 3, 4, 10]
# my_list = [1]
my_list = []
# my_list = [12, 3, 4, 10, 8]
if my_list:
    last_elem1 = my_list.pop()
    my_list.insert(0, last_elem1)

print(my_list)

pass
