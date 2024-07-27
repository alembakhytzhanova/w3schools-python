#Python Tuple (кортеж)

#Tuple
"""
Кортежи используются для хранения нескольких элементов в одной переменной.

Кортеж — один из четырех встроенных типов данных в Python, используемых для хранения коллекций данных; остальные три — это List , Set и Dictionary , все они имеют различные качества и применение.

Кортеж — это упорядоченная и неизменяемая коллекция .

Кортежи записываются в круглых скобках.
"""

thistuple = ("apple", "banana", "cherry")
print(thistuple)

#Элементы кортежа
"""
Элементы кортежа упорядочены, неизменяемы и допускают дублирование значений.

Элементы кортежа индексируются, первый элемент имеет индекс [0], второй элемент имеет индекс [1]и т. д.

"""

#Ordered
'''
Когда мы говорим, что кортежи упорядочены, это означает, что элементы имеют определенный порядок, и этот порядок не изменится.
'''

#Unchangeable
'''
Кортежи неизменяемы, то есть мы не можем изменять, добавлять или удалять элементы после создания кортежа.

'''
#Allow Duplicates

#Поскольку кортежи индексированы, они могут иметь элементы с одинаковым значением

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print('2 tuple', thistuple)

#Tuple Length

#Чтобы определить, сколько элементов в кортеже, используйте функцию len():

thistuple = ("apple", "banana", "cherry")
print('len of tuple',len( thistuple))


#Создать кортеж с одним элементом
#Чтобы создать кортеж, содержащий только один элемент, необходимо добавить запятую после элемента, иначе Python не распознает его как кортеж.

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))



#Tuple Items - Data Types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print(tuple1)
print(tuple2)
print(tuple3)

#A tuple can contain different data types:

tuple1 = ("abc", 34, True, 40, "male")

print(tuple1)

#type()
#From Python's perspective, tuples are defined as objects with the data type 'tuple':

#<class 'tuple'>

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

#Конструктор tuple()
#Для создания кортежа также можно использовать конструктор tuple()
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

#Python Collections (Arrays)

'''
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
'''