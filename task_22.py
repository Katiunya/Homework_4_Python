# Задача 22: Даны два неупорядоченных набора целых чисел 
# (может быть, с повторениями). Выдать без повторений в 
# порядке возрастания все те числа, которые встречаются в 
# обоих наборах. Пользователь вводит 2 числа. n — кол-во 
# элементов первого множества. m — кол-во элементов 
# второго множества. Затем пользователь вводит сами 
# элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

n = int(input("Enter the number of elements of the first set: "))
m = int(input("Enter the number of elements of the second set: "))

first = set()
for i in range(n):
    first.add(int(input("Enter the element of the first set: ")))
second = set()    
for i in range(m):
    second.add(int(input("Enter the element of the second set: ")))

result = first & second

newResult = list(result)
#newResult.sort()
print(*newResult)