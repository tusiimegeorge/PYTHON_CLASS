#DATA types
#Floats,Strings,Char,Boolean,Int,Decimal(Double)
#Data types are used to define values and variables
w =40
print(type(w))
name="Tusiime_George_Trevour_afternoon.py"
print(type(name))
z = 2j
print(type(z))

#LISTS
#They are used to store many items in single variable and they are in an ordered way
#Lists are ordered,changeable,allows for duplicate values
Afternon=["Trevour","Martin","Trevor"]
print(Afternon)
Afternon=["Trevour","Martin","Trevor","Trevor","Trevor"]
print(Afternon)
print(len(Afternon))
#List type
print(type(Afternon))
#Access List items (we use indexes)
print(Afternon[2])
print(Afternon[4])
#Negative indexing
print(Afternon[-2])
print(Afternon[-3])
print(Afternon[-4])
#Accessing a range of items in a list
print(Afternon[2:4])
print(Afternon[:4])
print(Afternon[2:])
#Add list items using append
Afternon.append("George")
print(Afternon)
#Add list items using the insert method
Afternon.insert(2,"Livingstone")
print(Afternon)
#Removing list items
Afternon.remove("Trevor")
print(Afternon)
#Removing list items using pop() method
Afternon.pop(4)
print(Afternon)

#Tuples
#They are used to store items in a single variable 
#they are ordered, they are unchangeable ,allow duplicate values

phone=("sumsung","tecno","iphone")
print(phone)

#Exercise
#use the len() method
print(len(phone))
#Tuple showing different data types
Tuple1 = ("cat","dog","fish")
Tuple2 = (1,2,3,4)
print(Tuple1)
print(Tuple2)
print(type(Tuple1))

#How to access tuples
#Add items to a tuple
Tuple2 = (1,2,3,4)
p=list(Tuple2)
p.append(5)
Tuple2=tuple(p)
print(Tuple2)
#Therefore all list operations can be performed on tuples after changing it to list 
c=list(Tuple1)
c.pop(1)
Tuple1=tuple(c)
print(Tuple1)
#Adding two tuples together
Tuple1 +=Tuple2
print(Tuple1)
print(Tuple2)
Newtuple= Tuple1+Tuple2
print(Newtuple)
 #For loop in tuples
for a in Newtuple:
    print(a)

#Sets are unchangeable  but you can remove and add items
set1 = {"rice","posho","beans"}
print(set1)
#Duplicates in sets
set1 = {"rice","posho","beans","posho","beans"}
print(set1)
#Length of a set
print(len(set1))
#type of a set
print(type(set1))
#Accessing items in set

for a in set1:
    print(a)
set2 = {3,4,5,6,7}
d=list(set1)
e=list(set2)
f=d+e
set3 = set(f)
print(set3)