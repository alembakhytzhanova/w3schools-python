#Доступ к элементам кортежа
#Доступ к элементам кортежа можно получить, обратившись к индексному номеру внутри квадратных скобок:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

'''
Отрицательная индексация
Отрицательная индексация означает начало с конца.

-1 относится к последнему элементу, -2 относится к предпоследнему элементу и т. д.
'''
thistuple = ("apple", "banana", "cherry")
print("negetive indexing", thistuple[-1])

'''
Вы можете задать диапазон индексов, указав, где начинается и где заканчивается диапазон.

При указании диапазона возвращаемым значением будет новый кортеж с указанными элементами.
'''
#1
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print('range index', thistuple[2:5])

#2
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

#3
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

#Диапазон отрицательных индексов
#Укажите отрицательные индексы, если вы хотите начать поиск с конца кортежа

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print('negative indexing range', thistuple[-4:-1])

#Проверить, существует ли элемент
#Чтобы определить, присутствует ли указанный элемент в кортеже, используйте inключевое слово:

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")