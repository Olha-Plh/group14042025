my_string_1 = ' I " like" Python'
print(my_string_1)

my_string_2 = """Python
    ""is""

awesome
    """
print(my_string_2)


def func():
    """
    This function is cool!
    """
    ...


print(help(func))
print(
    help(int)
)  # документована функція, яка відображає методи і всю інформацію функції

# за допомогою функції str можна з будь-якого типу даних створити рядок
digits = str(3654)  # виглядає як число, але це рядок
print(digits)  # виведе 3654
print(type(digits))  # виведе: <class 'str'>

my_string_3 = (
    "Python " + "is " + "awesome! "
)  # ставимо у кінці пробіли, щоб не склеяло все речення разом
print(my_string_3)

my_string_4 = "Go" * 10  # відображення 10 раз "Go"
print(my_string_4)

my_string_5 = "Python"  # відображення довжини стрічки (6 символів)
print(len(my_string_5))

a = ""  # булове значення з порожньої стрінги буде False
print(bool(a))

a = " "  # булове значення буде True, оскільки є 1 символ (є будь-що в середині)
print(bool(a))

# Доступ до елементів рядка за індексом
my_string = "Python is awesome"
print(my_string[0])  # виведе: P
print(my_string[-2])  # виведе: m (передостання літера)

my_string_6 = "Python is awesome"
my_string = my_string_6[:6]  # виведе: з 0 по 6, тобто - Python
my_string = my_string_6[::-1]  # виведе: задом на перед - emosewa si nohtyP
print(my_string)

my_string = my_string_6[7:9]
print(my_string)  # виведе: is
print(my_string_6[:])  # виведе від 0 і до кінця: Python is awesome

my_string_7 = "I like Python"
my_string1 = (
    my_string_7.upper()
)  # метод "upper" приведе все до верхнього регістеру, тобто виведе: I LIKE PYTHON
my_string2 = (
    my_string_7.title()
)  # метод "title" першу літеру кожного слова переводить у верхній регістр, а решта в нижній

print(my_string1)
print(my_string2)

my_string3 = (
    my_string_7.swapcase()
)  # swapcase Перекладає символи нижнього регістру у верхній, а верхнього у нижній, тому виведе: i lIKE pYTHON
print(my_string3)

my_string4 = my_string_7.lower()  # lower() Знижує регістр символів
print(my_string4)

# my_string_7  = "I Like Python"
print(
    my_string_7.ljust(20, "*")
)  # вирівнювання по лівому краю до 20 символів, додаючи *, виведе: I Like Python*******
print(
    my_string_7.rjust(20, "+")
)  # вирівнювання з правого краю до 20 символів, додаючи +, виведе: +++++++I Like Python
print(
    my_string_7.center(20, "-")
)  # вирівнювання по центру і додає - з обох сторін, виведе: ---I Like Python----


my_string5 = "I like PHP, PHP, PHP,"

# можна вказувати кілька методів поспіль
my_string_8 = my_string5.replace("PHP", "Python").replace(
    ",", "!"  # зміна знаків
)  # зміна всіх РНР на Python
print(my_string_8)  # виведе: I like Python! Python! Python!

# оригінальний рядок не змінився
print(my_string5)  # виведе: I like PHP, PHP, PHP,

# можна замінити не все, а лише певну кількість
my_string_8 = my_string5.replace("PHP", "Python", 1)  # зміна тільки перший замінимо
print(my_string_8)  # виведе: I like Python, PHP, PHP,

# якщо у рядку немає вибраного символу, то помилки все одно не буде! ("*", "//"), просто не відобразить зміни
my_string_8 = my_string5.replace("k", "//")  # замінить "k" на "//"
print(my_string_8)  # виведе: I like PHP, PHP, PHP


lst1 = (
    my_string5.split()
)  # розбиття від пробіла до пробіла, тому виведе: ['I', 'like', 'PHP,', 'PHP,', 'PHP,']
lst2 = my_string5.split(
    "i"
)  # розбиття від початку до "i" і далі на 2 відрізка, тому виведе: ['I l', 'ke PHP, PHP, PHP,']

print(lst1)
print(lst2)


pass
