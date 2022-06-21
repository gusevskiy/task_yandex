
arrayY = []

a = [i for i in range(30)]


#d = [a[d:d+5] for d in range(0, len(a), 5)] # разбивает массив на части равные пяти

# l1, l2 = divmod(len(a), 6) # разделение массива на заданные ракные части
# print(l1, l2)

'''
def main(arr, n):
    tmp_arr = []
    lenght_arr = len(arr)
    lenght_sub_arr = lenght_arr // n
    rem_div = lenght_arr % n
    start = 0
    for _ in range(n):
        if rem_div:
            end = start + lenght_sub_arr + 1
            rem_div = rem_div - 1
        else:
            end = start + lenght_sub_arr
        tmp_arr.append(arr[start:end])
        start = end
    return tmp_arr
print(main(a, 3))''' # нашел решение на github

# algoritm Timsort https://habr.com/ru/company/infopulse/blog/133303/
# размер входного массива
n = len(a)
# упорядоченый подмассив во входном массиве
run = 0
# минимальный размер такого подмассива
min_run = 6
# переписал переришал код чтоб разобраться
def main(arrey, n):
    new_arr = []
    len_arr = len(arrey)
    min_run = len_arr // n
    rem_div = len_arr % n # остаток от целочисленного деления
    start = 0
    for _ in range(n):
        if rem_div: # если есть остаток то True значит надо его раскидывать те прибовлять по 1 к размеру arrey
            end = start + min_run + 1
            rem_div = rem_div - 1
        else:
            end = start + min_run
        new_arr.append(arrey[start:end])
        start = end
    return new_arr

print(main(a, 4))