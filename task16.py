#Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

def masgen(n):
 
    for i in range(1,10):
        mlist.append(i)
 
 
 
    print(mlist)
    print(mlist.count(n))
 
if __name__ == '__main__':
 
    mlist=[]
    n=int(input())
    masgen(n)