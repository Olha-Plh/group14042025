from pprint import pprint

# відображення красивого коду, а не списку-колбаси

some_list = [55, 666] * 6
some_string = ",dfngkf8dgfgikhdfkighfdikgf"
products = ["banana", "vodka", "milk", "bread", "vodka"]

for item in some_string:
    print(item)

for product in products:

    if product == "milk":
        break  # зупинися

    if product == "vodka":
        continue  # не перевіряй далі

    print(product)
    print(product)  # двічі відображається при запуску в циклі (4 відступи)
    if product == "vodka":
        print("No booze today")

print(8888888)

people = [
    ["Alex", "Bush", "Odesa", 35, True, 12131],
    ["Alex", "Bush", "Kyiv, Lobanovskoho str", 65, False, 36738],
    ["Petr", "Bray", "Odesa", 35, True, 46736],
    ["Alex", "Bush", "Kyiv", 65, False, 36738],
    ["Alex", "Bush", "KYIV", 35, False, 366772],
    ["Petr", "Bray", "Odesa", 35, True, 267822],
    ["Alex", "Bush", "Kyiv", 65, False, 27271],
    ["Olga", "Butterfly", "", 22, False, 132452],
]

# all married people
# not married from Kyiv
# average age of married people
# 3 Alex below 22
all_married_people = []
not_married_from_city = []
city = "Kyiv"

total_age = 0
people_married = 0
########
for person in people:
    # person: ['Alex', 'Bush', 'Odesa', 35, True, 12131]
    name, surname, address, age, is_married, inn = person

    # is_married = person[4]
    # address = person[2].lower()
    # address = address.lower() #якщо б декілька раз використовували місто, то швидше було б привести до нижнього регістру і шукати
    if is_married:
        # print(person)
        all_married_people.append(person)
    if not is_married and city.lower() in address.lower():
        not_married_from_city.append(person)

if all_married_people:
    ages = []  # 1 варіант
    for married_person in all_married_people:
        age = married_person[3]
        total_age += age

        ages.append(age)  # 1 варіант

    print(f"Average age of married = {total_age/len(all_married_people)}")
    print(f"Average age of married = {sum(ages)/len(all_married_people)}")  # 1 варіант
else:
    print("No married - no age")
print("all married")
pprint(all_married_people)
print(f"not married from {city}")
pprint(not_married_from_city)


###########

# all_married_people = []
# for person in people:
#     is_married = person[4]
#     # if person[4] is True:
#     if is_married:
#         print(person)
#         all_married_people.append(person)
#
# # not married from Kyiv
# not_married_from_city = []
# city = "Kyiv"
# for person in people:
#     is_married = person[4]
#     # if person[4] is True:
#     address = person[2].lower()
#     # if not is_married and city == 'Kyiv':
#     if not is_married and city.lower() in address:
#         not_married_from_city.append(person)


pass
