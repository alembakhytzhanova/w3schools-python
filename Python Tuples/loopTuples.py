#Loop Through a Tuple
#Вы можете перебирать элементы кортежа, используя forцикл

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#Перебор индексных номеров
'''
Вы также можете перебирать элементы кортежа, ссылаясь на их индексный номер.

Используйте функции range()и len()для создания подходящей итерации.
'''
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print('range and len',thistuple[i])


#Использование цикла While


'''
Вы можете перебирать элементы кортежа, используя while цикл.

Используйте len()функцию для определения длины кортежа, затем начните с 0 и пройдитесь по элементам кортежа, ссылаясь на их индексы.

Не забудьте увеличить индекс на 1 после каждой итерации.

'''

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print('while loop', thistuple[i])
  i = i + 1
