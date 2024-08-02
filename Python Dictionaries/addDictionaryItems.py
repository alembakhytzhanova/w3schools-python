#Python - Add Dictionary Items

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)


#Update Dictionary
'''
Метод update()обновит словарь элементами из указанного аргумента. Если элемент не существует, он будет добавлен.

Аргумент должен быть словарем или итерируемым объектом с парами ключ:значение.
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

print(thisdict)
