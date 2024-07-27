#Unpacking a Tuple

#Когда мы создаем кортеж, мы обычно присваиваем ему значения. Это называется «упаковкой» кортежа:

fruits = ("apple", "banana", "cherry")

print(fruits)

#Но в Python нам также разрешено извлекать значения обратно в переменные. Это называется «распаковкой»:

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


#Использование Астериск*

'''
Если количество переменных меньше количества значений, вы можете
 добавить *к имени переменной, и значения будут присвоены переменной в виде списка:
'''
#Если звездочка добавлена ​​к другому имени переменной, отличному от последнего, Python будет присваивать значения переменной до тех пор, пока количество оставшихся значений не совпадет с количеством оставшихся переменных
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

#2
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

