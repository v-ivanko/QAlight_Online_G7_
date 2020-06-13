s = input("\nВведите предложение: ")
m = input("Введите символ: ")
count = 0

for i in range(0, len(s), 1):
        if m == s[i]:
            count += 1
print("\nКоличество символов в предложении: ", count)
