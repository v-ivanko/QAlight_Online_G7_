a = int(input("\nВведите 1 значение: "))
b = int(input("Введите 2 значение: "))
v = int(input("Введите 3 значение: "))

if a > b:
    print('Свершилось!')
elif a < b:
    print('Да ну!')
else:
    print('А если так?')
    if a + v > b - v:
        print('Свершилось!')
    elif a + v < b - v:
        print('Да ну!')