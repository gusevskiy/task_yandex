'''Опишите словами алгоритм решения задачи

Ввод: натуральное число n
Вывод: количество простых чисел строго меньше n

Решение должно быть вычислительно-эффективным'''   
'''
# enter number
n = int(input('n '))
lst = []
# let's go through the numbers
for i in range(2, n+1):
    # let's go through the numbers from 2 to the current one
    for j in range(2, i):
        # if number is divisible without remainder then it is not simple
        if i % j == 0:
            break
    else:
        lst.append(i)
print(lst)'''
'''        
# enter number
n = int(input('n '))
lst = []
# let's go through the numbers
for i in range(2, n+1):
    # let's go through the numbers from list (lst) 
    for j in lst:
        # if number is divisible without remainder then it is not simple
        if i % j == 0:
            break
    else:
        lst.append(i)
print(lst)'''

# Решето Эратосфена

n = int(input('n '))
a = list(range(n+1))
a[1] = 0
lst = []

i = 2
while i <= n:
    if a[i] != 0:
        lst.append(a[i])
        for j in range(i, n+1, i):
            a[j] = 0
    i += 1
print(lst)

# my decision свое сделать не смог
'''
n = int(input('n '))

we = list(range(2, n))
print(we)

i = 2
for i in we:
    if i % 2 == 0:
        we.remove(i)

print([2] + we)'''

        

