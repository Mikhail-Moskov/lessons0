grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(list(students))
result = {}
for i in range(len(grades)):
   grades [i] = sum(grades[i]) / len(grades[i])
   result[students[i]] = grades[i]
# result = dict(zip (students, grades))
# метод zip подглядел в интернете поэтому посторался решить без него
# можно кончено и без цикла for просто перебором элементов от 0 до 4
print (result)

