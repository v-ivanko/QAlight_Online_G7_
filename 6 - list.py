from random import randrange

def list(length, max):
    list=[]
    for i in range(0,length):
        list.append(randrange(max))
    return list

def DialogList():
    print("Введите значение для длины списка:")
    length = int(input())
    print("Введите значение, которое будет максимальным:")
    max = int(input())

    print(list(length, max))

DialogList()
