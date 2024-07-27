#Sets

#set используются для хранения нескольких элементов в одной переменной.
'''
Set — один из 4 встроенных типов данных в Python, используемых для хранения коллекций данных; остальные 3 — это List , Tuple и Dictionary , все они имеют разные качества и применение.

Set — это неупорядоченная , неизменяемая* и неиндексированная коллекция .
элементы Set не подлежат изменению, но вы можете удалять элементы и добавлять новые элементы.

'''
thisset = {"apple", "banana", "cherry"}
print(thisset)

#Set Items
#Элементы set неупорядочены, неизменяемы и не допускают дублирования значений.


#Unordered
'''
Неупорядоченность означает, что элементы в наборе не имеют определенного порядка.

Элементы набора могут появляться в разном порядке каждый раз, когда вы их используете, и на них нельзя ссылаться по индексу или ключу.

'''
#Unchangeable
#Элементы набора неизменяемы, то есть мы не можем изменить элементы после создания набора



#Duplicates Not Allowed
#В наборах не может быть двух предметов с одинаковым значением.
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

#True и 1считается одним и тем же значением:
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

#False и 0считается одним и тем же значением:
thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)


#Get the Length of a Set
#Чтобы определить, сколько элементов в наборе, используйте функцию len() .
thisset = {"apple", "banana", "cherry"}

print(len(thisset))


#Set Items - Data Types

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print('set1',set1)
print('set2',set2)
print('set3',set3)


#Набор может содержать различные типы данных:

set1 = {"abc", 34, True, 40, "male"}

print(set1)

#type()
myset = {"apple", "banana", "cherry"}
print(type(myset))

#The set() Constructor

#Для создания набора также можно использовать конструктор set() 

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)