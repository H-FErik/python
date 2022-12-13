#Feladat-method



#Set add()
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)

#Set clear()
fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)

#Set copy()
fruits = {"apple", "banana", "cherry"}
x = fruits.copy()
print(x)

#Set difference()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)

#Set difference_update()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print(x)

#Set discard()
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)

#Set intersection()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

#Set intersection_update()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

#Set isdisjoint()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z)

#Set issubset()
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)

#Set issuperset()
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)

#Set pop()
fruits = {"apple", "banana", "cherry"}
fruits.pop()
print(fruits)

#Set remove()
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)

#symmetric_difference()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)

#symmetric_difference_update()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

#Set union()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y)
print(z)

#Set update()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y)
print(x)