from random import randint, choice

# список випадкових чисел
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# обираємо від 3 до 10 рандомне число
rand_length = randint(3, 10)  # приклад з конспекту: randint(a, b)
random_numbers = []
for _ in range(rand_length):
    random_numbers.append(choice(digits))
# створення іншого списку з 3 елементів зі списку з п.1 - першим, третім і другим з кінця.
result = [random_numbers[0], random_numbers[2], random_numbers[-2]]

print(random_numbers, "==", result)
pass
