#Join Sets

'''
Присоединиться к наборам
В Python существует несколько способов объединения двух или более множеств.

Методы union()и update()объединяют все элементы из обоих наборов.

Метод intersection()сохраняет ТОЛЬКО дубликаты.

Метод difference()сохраняет элементы из первого набора, которых нет в другом наборе(ах).

Метод symmetric_difference()сохраняет все элементы, КРОМЕ дубликатов

'''


#Union
#Метод union()возвращает новый набор со всеми элементами из обоих наборов.

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print("union method",set3)


#Вы можете использовать |оператор вместо union()метода и получите тот же результат.

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print("union method |", set3)


#Присоединиться к нескольким наборам

'''
Все методы и операторы объединения можно использовать для объединения нескольких наборов.

При использовании метода просто добавьте больше наборов в скобках, разделив их запятыми:
'''

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)


#Join a Set and a Tuple

'''
Метод union()позволяет объединять набор с другими типами данных, такими как списки или кортежи.

Результатом будет set.
'''

x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print("set and tuple join",z)

#Update

'''
Метод update()вставляет все элементы из одного набора в другой.

Изменяет update()исходный набор и не возвращает новый набор.
'''
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#Intersection

'''
Сохраняйте ТОЛЬКО дубликаты

Метод intersection()вернет новый набор, содержащий только те элементы, которые присутствуют в обоих наборах.
'''

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print("intersection method" ,set3)


#Вы можете использовать &оператор вместо intersection()метода и получите тот же результат.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print("with &",set3)

'''
 оператор & позволяет объединять только наборы с наборами, а не с другими типами данных, как это можно сделать с помощью intersection()метода.
 '''
#Метод intersection_update()также сохранит ТОЛЬКО дубликаты, но он изменит исходный набор вместо того, чтобы возвращать новый набор
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)

#Значения Trueи 1 считаются одинаковыми. То же самое касается Falseи 0.

set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

print(set3)

#Difference
'''
Метод difference()вернет новый набор, который будет содержать только те элементы из первого набора, которых нет в другом наборе.
'''

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print("difference",set3)

#Вы можете использовать -оператор вместо difference()метода и получите тот же результат.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print("-",set3)

'''
Примечание: оператор - позволяет объединять
только наборы с наборами, а не с другими 
типами данных, как это можно сделать с помощью difference()метода.
Метод difference_update()также сохранит элементы из первого набора, которых нет в другом наборе, но он изменит исходный набор вместо 
того, чтобы возвращать новый набор.
'''
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print("difference_update",set1)


#Symmetric Differences

'''
Метод symmetric_difference()сохранит
только те элементы, которые НЕ присутствуют
в обоих наборах.
'''

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print("symmetrice differences",set3)

#Вы можете использовать ^оператор вместо symmetric_difference()метода и получите тот же результат

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print("symmetrice differences with ^",set3)


'''
Метод symmetric_difference_update()также сохранит
все, кроме дубликатов, но он изменит исходный набор вместо возврата нового набора
'''

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print("symmetric difference update",set1)