#Copy Lists

#Copy a List

"""
Вы не можете скопировать список, просто набрав list2 = list1, поскольку: list2будет только ссылкой на list1, а изменения, внесенные в , list1автоматически будут также внесены в list2.

Есть несколько способов сделать копию, один из которых — использовать встроенный метод List copy().

ПримерПолучите свой собственный
"""

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#Другой способ сделать копию — использовать встроенный метод list().

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print("2", mylist)