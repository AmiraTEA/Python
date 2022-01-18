# 1) Создать переменную типа String
name = 'Amira'
print(name, ',', 'Type (name) =', type(name))
# 2) Создать переменную типа Integer
age = 50
print(age, ',', 'Type (age) =', type(age))
# 3) Создать переменную типа Float
pi = 3.1414926
print(pi, ',', 'Type (pi) =', type(pi))
# 4) Создать переменную типа Bytes
d = bytes('Hello, gues', 'UTF-8')
print(d, ',', 'Type (d) =', type(d))
# 5) Создать переменную типа List
random_list = [49, 'Luna', pi, True, (1, 2, 3)]
print(random_list, ',', 'Type (random_list) =', type(random_list))
# 6) Создать переменную типа Tuple
kortezh = ('Python', 'Java', 'JS', 'PHP')
print(kortezh, ',', 'Type (kortezh) =', type(kortezh))
# 7) Создать переменную типа Set
mnozhestvo = set(random_list)
print(mnozhestvo, ',', 'Type (mnozhestvo) =', type(mnozhestvo))
# 8) Создать переменную типа Frozen set
zamor_mnozhestvo = frozenset([1,2,3,4,5])
print(zamor_mnozhestvo, ',', 'Type (zamor_mnozhestvo) =', type(zamor_mnozhestvo))
# 9) Создать переменную типа Dict
slovari = {'Lera': 12345, 'Rita': 23456, 'Oleg': 34567}
print(slovari, ',', 'Type (slovari) =', type(slovari))
# 10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
# 11) Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.
tree_1 = 'apple'
tree_2 = "orange"
garden = tree_1 + tree_2   # конкатенация
print(garden)
# 12) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
print(tree_1, age)
# 13) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
print(tree_2 + str(age))
