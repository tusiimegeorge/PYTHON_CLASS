#Individual Assignment
#Exercise1 (Lists)
#1. Create a list with 5 items (names of people) and write a python program to output the 2nd item.

# List of names
names = ["Tusiime", "Kalema", "Kasasa", "Katende", "Kyomu"]

# Output the 2nd item
print(names[1])

#2. Write a python program to change the value of the first item to a new value
# Change the value of the first item
names[0] = "Namugga"

# Print the modified list
print("Modified list:", names)


#3. Write a python program to add a sixth item to the list
# List of names
names = ["Tusiime", "Kalema", "Kasasa", "Katende", "Kyomu"]

# Add a sixth item to the list
names.append("Muhwezi")

# Print the modified list
print("Modified list:", names)

#4. Write a python program to add “Bathel” as the 3rd item in your list

# Add "Bathel" as the 3rd item in the list
names.insert(2, "Bathel")

# Print the modified list
print("Modified list:", names)
#5. Write a python program to remove the 4th item from the list

# Remove the 4th item from the list
del names[3]

# Print the modified list
print("Modified list:", names)


#6. Use negative indexing to print the last item in your list

# Print the last item in the list using negative indexing
print("Last item:", names[-1])

#7. Create a new list with 7 items and use a range of indexes to print the 3rd, 4th and 5th items.

# New list with 7 items
items = ["Cow ", "Goat", "Cat", "Hen", "Sheep", "Pig", "Dog"]

# Print the 3rd, 4th, and 5th items using index range
print("3rd item:", items[2])
print("4th item:", items[3])
print("5th item:", items[4])

#8. Write a list of countries and make a copy of it.

# Original list of countries
countries = ["Uganda", "Rwanda", "Kenya", "Tanzania", "Burundi"]

# Making a copy of the list using the slice operator
countries_copy = countries[:]

# Print the original list
print("Original list of countries:", countries)

# Print the copied list
print("Copied list of countries:", countries_copy)

#9. Write a python program to loop through the list of countries

# Loop through the list of countries
for country in countries:
    print(country)

#10. Write a list of animal names and sort them in both descending and ascending order.

# List of animal names
animal_names = ["Lion", "Elephant", "Giraffe", "Horse", "Cheater"]

# Sort the animal names in ascending order
ascending_order = sorted(animal_names)

# Sort the animal names in descending order
descending_order = sorted(animal_names, reverse=True)

# Print the sorted lists
print("Ascending order:", ascending_order)
print("Descending order:", descending_order)

#11. Using the list above, write a python program to output only animal names with the letter  ‘a’ in them

# Iterate through the animal names
for name in animal_names:
    if 'a' in name.lower():
        print(name)

#12. Write two lists, one containing your first names and the other your second names. Join the two lists.

# First names list
first_names = ["Trevour", "Martin", "Livingstone", "Brian"]

# Second names list
second_names = ["Tusiime", "Kalema", "Kasasa", "Katende"]

# Join the two lists
full_names = []
for first, second in zip(first_names, second_names):
    full_names.append(first + " " + second)

# Print the full names
for name in full_names:
    print(name)

#Exercise2 (Tuples)

#1. Consider the tuple below;
#x = (“samsung”, “iphone”, “tecno”, “redmi”)
#Write a python program to output your favorite phone brand.

# Tuple of phone brands
x = ("samsung", "iphone", "tecno", "redmi")

# Output your favorite phone brand
favorite_brand = x[1]
print("Favorite phone brand:", favorite_brand)

#2. Use negative indexing to print the 2nd last item in your tuple.

# Print the second-to-last item using negative indexing
second_last_item = x[-2]
print("Second-to-last item:", second_last_item)

#3. Using the phones list above, write a python program to update “iphone” to “itel”

# Tuple of phone brands
x = ("samsung", "iphone", "tecno", "redmi")

# Convert the tuple to a list
phone_list = list(x)

# Update "iphone" to "itel"
phone_list[1] = "itel"

# Convert the list back to a tuple
updated_tuple = tuple(phone_list)

# Print the updated tuple
print("Updated tuple of phone brands:", updated_tuple)

#4. Write a python program to add “Huawei” to your tuple.

# Tuple of phone brands
x = ("samsung", "iphone", "tecno", "redmi")

# Add "Huawei" to the tuple
updated_tuple = x + ("Huawei",)

# Print the updated tuple
print("Updated tuple of phone brands:", updated_tuple)

#5. Write a python program to loop through the tuple above.

# Loop through the tuple
for brand in x:
    print(brand)

#6. Write a python program to remove/delete the first item in your tuple.

# Convert the tuple to a list
phone_list = list(x)

# Remove the first item from the list
del phone_list[0]

# Convert the list back to a tuple
updated_tuple = tuple(phone_list)

# Print the updated tuple
print("Updated tuple of phone brands:", updated_tuple)

#7. Using the tuple() constructor, create a tuple of the cities in Uganda.

# Tuple of cities in Uganda
ug_cities = tuple(["Kampala", "FortPortal", "Mbale", "Mbarara", "Arua"])

# Print the tuple of cities in Uganda
print("Tuple of cities in Uganda:", ug_cities)

#8. Write a python program to unpack your tuple.

# Tuple of phone brands
ug_cities = ("Kampala", "FortPortal", "Mbale", "Mbarara","Arua")

# Unpack the tuple
city1, city2, city3, city4, city5 = ug_cities

# Print the unpacked values
print("City 1:", city1)
print("City 2:", city2)
print("City 3:", city3)
print("City 4:", city4)
print("City 5:", city5)

#9. Use a range of indexes to print the 2nd, 3rd and 4th cities in your tuple above.

# Tuple of cities in Uganda
ug_cities = ("Kampala", "FortPortal", "Mbale", "Mbarara","Arua")


# Print the 2nd, 3rd, and 4th cities using index range
print("2nd city:", ug_cities[1])
print("3rd city:", ug_cities[2])
print("4th city:", ug_cities[3])

#10. Write two tuples, one containing your first names and the other your second names. Join the two tuples.

# First names tuple
first_names = ("Trevour", "Martin", "Livingstone", "Brian")

# Second names tuple
second_names = ("Tusiime", "Kalema", "Kasasa", "Katende")

# Join the two tuples
full_names = first_names + second_names

# Print the full names tuple
print("Full names tuple:", full_names)

#11. Create a tuple of colors and multiply it by 3.

# Tuple of colors
colors = ("red", "blue", "green")

# Multiply the tuple by 3
multiplied_colors = colors * 3

# Print the multiplied tuple
print("Multiplied colors tuple:", multiplied_colors)

#12. Return the number of times 8 appears in this tuple thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

# Tuple of numbers
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

# Count the number of occurrences of 8 in the tuple
count = thistuple.count(8)

# Print the count
print("Number of times 8 appears:", count)

#Exercise3 (Sets)
#1. Use the set() constructor to create a set of 3 of your favorite beverages.

# Set of favorite beverages
favorite_beverages = set(["coffee", "wine", "juice"])

# Print the set of favorite beverages
print("Set of favorite beverages:", favorite_beverages)

#2. Use the correct method to add 2 more items to the beverages set.

# Set of favorite beverages
favorite_beverages = {"coffee", "tea", "juice"}

# Add two more items to the set
favorite_beverages.add("beer")
favorite_beverages.add("soda")

# Print the updated set of favorite beverages
print("Updated set of favorite beverages:", favorite_beverages)

#3. Given the set below; mySet = {“oven”, “kettle”, “microwave”, “refrigerator”} Check if microwave is present in the set.

# Set of appliances
mySet = {"oven", "kettle", "microwave", "refrigerator"}

# Check if "microwave" is present in the set
if "microwave" in mySet:
    print("Microwave is present in the set")
else:
    print("Microwave is not present in the set")


#4. Write a python program to remove “kettle” from the set above.

# Set of appliances
mySet = {"oven", "kettle", "microwave", "refrigerator"}

# Remove "kettle" from the set
mySet.remove("kettle")

# Print the updated set
print("Updated set:", mySet)

#5. Write a python program to loop through the set above.

# Loop through the set
for item in mySet:
    print(item)

#6. Write a set of 4 items and a list of two items. Write a python program to add elements in the list to elements in the set.

# Set of items
mySet = {"apple", "banana", "orange", "grape"}

# List of items
myList = ["lemon", "mango"]

# Add elements from list to set
mySet.update(myList)

# Print the updated set
print("Updated set:", mySet)

#7. Write two sets, one containing your ages and the other your first names. Join the two sets.


# First names set
first_names = {"Trevour", "Martin", "Livingstone", "Brian"}

# ages set
ages = {20, 21, 22, 22}

# Join the two sets
names_ages = first_names.union(ages)

# Print the Names and ages set
print("Names and ages set:", names_ages)

#Exercise4 (Strings)
#1. Declare two variables, an integer and a string and use the correct method to concatenate the two variables.

# Integer variable
myNumber = 42

# String variable
myString = "The answer is"

# Concatenate the variables
result = myString + " " + str(myNumber)

# Print the result
print("Concatenated string:", result)

#2. Consider the example below; txt = “ Hello, Uganda! ” Output the string without spaces at the beginning, in the middle and at the end.

# String with spaces
txt = " Hello, Uganda! "

# Remove spaces at the beginning, in the middle, and at the end
output = txt.strip()

# Print the output
print("Output string:", output)

#3. Write a python program to convert the value of ‘txt’ to uppercase.

# String variable
txt = "Hello, Uganda!"

# Convert the value to uppercase
uppercase_txt = txt.upper()

# Print the uppercase string
print("Uppercase string:", uppercase_txt)

#4. Write a python program to replace character ‘U’ with ‘V’ in the string above.

# String variable
txt = "Hello, Uganda!"

# Replace 'U' with 'V'
new_txt = txt.replace('U', 'V')

# Print the updated string
print("Updated string:", new_txt)

#5. Using the code below, write a python program to return a range of characters in the 2nd,3rd and 4th position.y = “I am proudly Ugandan”

# String variable
y = "I am proudly Ugandan"

# Get the range of characters in the 2nd, 3rd, and 4th positions
range_of_characters = y[1:4]

# Print the range of characters
print("Range of characters:", range_of_characters)

#6. The piece of code below will give an error when output; x = “All “Data Scientists” are cool!” Write a python program to correct it.

# Corrected string variable
x = "All \"Data Scientists\" are cool!"

# Print the corrected string
print(x)

#Exercise5 (Dictionaries)
#1. With reference to the dictionary below, write a python program to print the value of the shoe size.Add this dictionary to your .py file Shoes = {“brand” : “Nick”,“color” : “black”,“size” : 40}

# Dictionary of shoe details
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

# Print the value of the shoe size
print("Shoe size:", Shoes["size"])

#2. Write a python program to change the value “Nick” to “Adidas”
# Dictionary of shoe details
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

# Change the value "Nick" to "Adidas"
Shoes["brand"] = "Adidas"

# Print the updated dictionary
print("Updated dictionary:", Shoes)

#3. Write a python program to add a key/value pair "type”: "sneakers" to the dictionary

# Dictionary of shoe details
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

# Add the key/value pair "type": "sneakers"
Shoes["type"] = "sneakers"

# Print the updated dictionary
print("Updated dictionary:", Shoes)

#4. Write a python program to return a list of all the keys in the dictionary above.

# Dictionary of shoe details
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40,
    "type": "sneakers"
}

# Get a list of all the keys
keys_list = list(Shoes.keys())

# Print the list of keys
print("List of keys:", keys_list)

#5. Write a python program to return a list of all the values in the dictionary above.

# Dictionary of shoe details
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40,
    "type": "sneakers"
}

# Get a list of all the values
values_list = list(Shoes.values())

# Print the list of values
print("List of values:", values_list)

#6. Check if the key “size” exists in the dictionary above.

# Dictionary of shoe details
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40,
    "type": "sneakers"
}

# Check if the key "size" exists
if "size" in Shoes:
    print("The key 'size' exists in the dictionary.")
else:
    print("The key 'size' does not exist in the dictionary.")

#7. Write a python program to loop through the dictionary above.

# Dictionary of shoe details
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40,
    "type": "sneakers"
}

# Loop through the dictionary
for key, value in Shoes.items():
    print(key, ":", value)

#8. Write a python program to remove “color” from the dictionary.

# Dictionary of shoe details
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40,
    "type": "sneakers"
}

# Remove the key "color" from the dictionary
Shoes.pop("color")

# Print the updated dictionary
print("Updated dictionary:", Shoes)

#9. Write a python program to empty the dictionary above.

# Dictionary of shoe details
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40,
    "type": "sneakers"
}

# Empty the dictionary
Shoes.clear()

# Print the empty dictionary
print("Empty dictionary:", Shoes)

#10. Write a dictionary of your choice and make a copy of it.

# Original dictionary
original_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Make a copy of the dictionary
copied_dict = original_dict.copy()

# Modify the original dictionary
original_dict["age"] = 31

# Print the original dictionary and its copy
print("Original dictionary:", original_dict)
print("Copied dictionary:", copied_dict)

#11. Write a python program to show nested dictionaries

# Nested dictionaries representing a student's information
student = {
    "name": "John Doe",
    "age": 20,
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "state": "NY",
        "zipcode": "10001"
    },
    "subjects": {
        "math": 85,
        "science": 92,
        "history": 78
    }
}

# Accessing nested dictionary values
print("Student Name:", student["name"])
print("Student Age:", student["age"])
print("Student Address:", student["address"])
print("Student City:", student["address"]["city"])
print("Student Math Grade:", student["subjects"]["math"])
print("Student Science Grade:", student["subjects"]["science"])
print("Student History Grade:", student["subjects"]["history"])
