set1 = {"Tom","Peter","John"}
set2 = {1,2,3,4}

print(set1)
print(set2)

print(len(set1))
print(len(set2))

for item in set1:
    print(item)
for item in set2:
    print(item)

set1.add("Trevour")
print(set1)
set2.add(5)
print(set2)

set1.remove("John")
print(set1)
set2.remove(4)
print(set2)

set1.update(set2)
print(set1)
set2.update(set1)
print(set2)