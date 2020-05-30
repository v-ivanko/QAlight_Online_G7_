from random import randrange

def list(length, max):
    list=[]
    for i in range(0,length):
        list.append(randrange(max))
    return list

def DialogList():
    print("Длина списка:")
    length = int(input())
    print("Максимальное значение:")
    max = int(input())

    print(list(length, max))

DialogList()