#Python - Change Dictionary Items

#Change Values
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict["year"] = 2018

print(thisdict)

#Update Dictionary
'''
Метод update()обновит словарь элементами из указанного аргумента.

Аргумент должен быть словарем или итерируемым объектом с парами ключ:значение.
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

print(thisdict)
