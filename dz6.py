
# n = input("Введите имя файла ")
# s = open("home_work.txt", "w", encoding="utf-8")
# s.write(n)
# s.close()

# s = open("home_work.txt", encoding="utf-8")
# print(s.read())
# s.close



import csv
from random import randint

A = []
for i in range(20):
    A.append(randint(-40,30))
with open("hw6.csv", "w", encoding="utf-8") as file:
    fieldnames = ["Положительные числа", "Отрицательные числа"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for i in A:
        if i > 0:
            writer.writerow({'Положительные числа': i})
        else:
            writer.writerow({'Отрицательные числа': i})


