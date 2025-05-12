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
    ["Alex" "Bush", "Odesa", 35, True, 12131],
    ["Petr" "Bray", "Odesa", 35, True, 46736],
    ["Alex" "Bush", "Kyiv", 65, False, 36738],
    ["Alex" "Bush", "Odesa", 35, True, 366772],
    ["Petr" "Bray", "Odesa", 35, True, 267822],
    ["Alex" "Bush", "Kyiv", 65, False, 27271],
    ["Olga" "Butterfly", "", 22, False, 132452],
]

# all married people
for person in people:
    # if person[4] is True:
    if person[4]:
        print(person)


# not married from Kyiv
# average age of married people
# 3 Alex below 22

pass
