number1 = int(input('Enter a four-digit integer from the keyboard:'))

print(number1 // 1000)
print((number1 // 100) % 10)
print((number1 // 10) % 10)
print(number1 % 10)

pass

# second version
number2 = int(input('Enter a four-digit integer from the keyboard:'))
a, number2 = divmod(number2, 1000)
print(a)
a, number2 = divmod(number2, 100)
print(a)
a, number2 = divmod(number2, 10)
print(a)
print(number2)

pass