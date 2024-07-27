#Удалить элементы набора

#Чтобы удалить элемент из набора, используйте метод remove(), или discard().

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

#Примечание: если удаляемый элемент не существует, remove()возникнет ошибка.

#Удалить «банан» можно следующим способом discard() :
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print("banana", thisset)

#Примечание: если удаляемый элемент не существует, ошибка НЕdiscard() ​​возникнет .


#Вы также можете использовать этот pop()метод для удаления элемента, но этот метод удалит случайный элемент, поэтому вы не можете быть уверены, какой именно элемент будет удален.
#Возвращаемым значением метода pop()является удаленный элемент.

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print("pop method", thisset)
'''
наборы не упорядочены , поэтому при использовании этого pop()метода вы не знаете, какой элемент будет удален.
'''

#Метод clear() очищает набор:

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print("clear", thisset)


#Ключевое delслово полностью удалит набор:

thisset = {"apple", "banana", "cherry"}

del thisset

print("del", thisset)