number1 = int(input('Enter a four-digit integer from the keyboard:'))


digit1 = number1 % 10
digit2 = (number1 // 10) % 10
digit3 = (number1 // 100) % 10
digit4 = (number1 // 1000) % 10
digit5 = (number1 // 10000)
reversed_number =digit1 * 10000 + digit2 * 1000 + digit3 * 100 + digit4 * 10 + digit5


pass