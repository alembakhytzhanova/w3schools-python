#Добавить элементы набора
#После создания набора вы не можете изменять его элементы, но можете добавлять новые элементы.



#Чтобы добавить один элемент в набор, используйте метод add()
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)


#Добавить наборы
#Чтобы добавить элементы из другого набора в текущий набор, используйте метод update() 

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

#Add Any Iterable
#Объект в update()методе не обязательно должен быть набором, это может быть любой итерируемый объект (кортежи, списки, словари и т. д.).

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print('newset',thisset)