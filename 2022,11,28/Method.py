#Method

#add() Method
fruits = {"apple", "banana", "cherry"}

fruits.add("orange")

print(fruits)

#clear() Method
fruits = {"apple", "banana", "cherry"}

fruits.clear()

print(fruits)

#copy() Method
fruits = {"apple", "banana", "cherry"}

x = fruits.copy()

print(x)

#difference() Method
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y)

print(z)

#difference_update() Method
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.difference_update(y)

print(x)

#discard() Method
fruits = {"apple", "banana", "cherry"}

fruits.discard("banana")

print(fruits)

#intersection() Method
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

#ntersection_update() Method
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

#isdisjoint() Method
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}

z = x.isdisjoint(y)

print(z)

#issubset() Method
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)

print(z)

#issuperset() Method
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}

z = x.issuperset(y)

print(z)

#pop() Method
fruits = {"apple", "banana", "cherry"}

fruits.pop()

print(fruits)

#remove() Method
fruits = {"apple", "banana", "cherry"}

fruits.remove("banana")

print(fruits)

#symmetric_difference() Method
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)

#union() Method
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.union(y)

print(z)

#update() Method
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.update(y)

print(x)