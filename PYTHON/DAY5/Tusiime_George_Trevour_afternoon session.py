# Python Dictionaries
# Dictionaries in Python are a collection of key-value pairs, defined using curly braces {}. 
#Each key-value pair is separated by a colon :. Keys are used to access their associated values, 
#and they must be unique within a dictionary.

# Key:
# A key is an immutable object, such as a string, number, or tuple, 
#that is used to identify and retrieve its associated value. 
#Keys provide a way to access specific elements within a dictionary.

# Value:
# A value can be of any data type, such as a string, number, list, or even another dictionary. 
#Values are associated with their respective keys and can be accessed using the key.

# Dictionary Syntax:
# dictionary_name = {key1: value1, key2: value2, key3: value3}
# Examples and Concepts:
# Accessing values in a dictionary using keys
# Finding the data type of a dictionary
# Determining the length of a dictionary
# Modifying values in a dictionary using keys
# Adding new key-value pairs to a dictionary
# Removing key-value pairs from a dictionary
# Looping through a dictionary using items()
# Nesting dictionaries within dictionaries


# Numbers in Python
# In Python, there are different types of numeric data:

# Integer (int): Integers are whole numbers without a decimal point. 
#They can be positive or negative, and there is no limit to their size.

# Floating-Point (float): Floating-point numbers have a decimal point and can represent fractional values. 
#They are commonly used for real numbers and calculations involving precision.

# Complex (complex): Complex numbers consist of a real part and an imaginary part. 
#They are written in the form a + bj, where a is the real part, b is the imaginary part, 
#and j represents the square root of -1.

# Examples and Concepts:
# Declaring and assigning values to integer, floating-point, and complex variables
# Performing arithmetic operations using numeric variables
# Type conversion between different numeric data types using functions like int(), float(), and complex()
# Strings in Python
# Strings in Python are sequences of characters, enclosed in either single quotes ' ' or double quotes " ". 
#They can be manipulated and accessed using various methods and operations.

# Examples and Concepts:
# Creating and assigning string values
# Formatting strings using f-strings to include variables
# Raw strings for handling backslashes and special characters
# Concatenating strings using the + operator and the join() method
# Accessing individual characters in a string using indexing
# Slicing strings to extract substrings using the : operator
# Utilizing the len() function to find the length of a string
# Iterating over characters in a string using a for loop
# Booleans in Python
# Booleans are a data type in Python that represent truth values. They can have two possible values: True or False. 
#Booleans are often used in conditional statements to control the flow of the program.

# Examples and Concepts:
# Evaluating conditions using comparison operators like <, >, ==, <=, >=, !=
# Combining conditions using logical operators like and, or, not
# Assigning boolean values based on comparisons or conditions


# Exercises:
# Use the values() method to create a list of items from a dictionary.
# Check if a specific key exists in a dictionary.
# Change and update items in a dictionary.
# Add and remove items from a dictionary.
# Demonstrate looping through a dictionary and nesting dictionaries within dictionaries.
# Determine the length of a string using the len() function.
# Iterate through each character in a string using a for loop.
# Slice a string to extract specific portions of it.
# Perform arithmetic operations with numbers and print the results.
# Use boolean values and conditions to control program flow.
# Feel free to explore and experiment with the concepts and exercises provided!


#SOLUTIONS BY TUSIIME GEORGE TREVOUR 21/U/07417/EVE
# Qn1 : Use the value() method to return a list of all values in the dictionary.

#  Using curly braces
dictionary1 = {'Tusiime': 'tvalue', 'Balaba': 'bvalue', 'Charlse': 'cvalue'}

# Using dict() function
dictionary2 = dict(Tusiime='tvalue', Balaba='bvalue', Charlse='cvalue')


print(dictionary1.values())
print(dictionary2.values())

#Qn2  : Check if a specific key exists in a dictionary.

# Using the in operator.
dictionary1 = {'Tusiime': 'tvalue', 'Balaba': 'bvalue', 'Charlse': 'cvalue'}

if 'Kalema' in dictionary1:
    print("Key exists")
else:
    print("Key does not exist")

# Using the not in operator
dictionary2 = {'Tusiime': 'tvalue', 'Balaba': 'bvalue', 'Charlse': 'cvalue'}

if 'Kalema' not in dictionary2:
    print("Key does not exist")
else:
    print("Key exists")


#Qn3  : Change and update items in a dictionary.

dict1 = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'} # new dictionary

dict1['key3'] = 'new value' # modification.

print(dict1) # modified


# Qn4 : Adding and removing dictionary items.

dict2 = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'} 


# Adding a single item
dict2 = {}  # An empty dictionary
dict2['key1'] = 'value1'  # Adds a new key-value pair
print(dict2)

# Adding multiple items at once

dict3 = {}  # An empty dictionary
dict3.update({'key1': 'value1', 'key2': 'value2'})  # Adds multiple key-value pairs
print(dict3)


# removing items 

# Using the del statement:
dict4 = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
del dict4['key2']  # Removes a specific key-value pair
print(dict4)

# Using the pop() method:
dict5 = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
dict5.pop('key2')  # Removes a specific key-value pair and returns the value
print(dict5)


#Qn5 : Looping through and nesting dictionaries

# Looping through keys.
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

for key in my_dict:
    print(key)

# Looping through values
dictx = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

for value in dictx.values():
    print(value)


# Looping through key-value pairs
dicty = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

for key, value in dicty.items():
    print(key, value)


# Nesting dictionaries and looping

dictz = {
    'person1': {'name': 'John', 'age': 30},
    'person2': {'name': 'Jane', 'age': 25},
    'person3': {'name': 'Mike', 'age': 35}
}

for person, info in dictz.items():
    print(f"Person: {person}")
    print(f"Name: {info['name']}")
    print(f"Age: {info['age']}")
    print()


#Qn6 : Determine the length of a string using the len() function.

name="Tusiime"
size = len(name)
print(size)


#Qn7 :  Iterate through each character in a string using a for loop.

for char in name:
    print(char)


#Qn8 :  Slice a string to extract specific portions of it.

string = "Coming"

# Extract a substring from index 2 to the end
substring1 = string[2:]
print(substring1)  

# Extract a substring from index 0 to 4 (excluding 4)
substring2 = string[:4]
print(substring2)  

# Extract a substring from index 3 to 5 (excluding 12)
substring3 = string[3:5]
print(substring3)  


#Qn9 :  Perform arithmetic operations with numbers and print the results.


# Addition
num1 = 1
num2 = 5
sum_result = num1 + num2
print("Sum:", sum_result)  

# Subtraction
num3 = 12
num4 = 3
sub_result = num3 - num4
print("Difference:", sub_result)  

# Multiplication
num5 = 5
num6 = 4
mul_result = num5 * num6
print("Product:", mul_result)  

# Division
num7 = 17
num8 = 2
div_result = num7 / num8
print("Quotient:", div_result)  

# Integer Division
int_div_result = num7 // num8
print("Integer Quotient:", int_div_result)  

# Modulo (Remainder)
mod_result = num7 % num8
print("Remainder:", mod_result)  


#Qn10 :  Use boolean values and conditions to control program flow.

is_sunny = True
temperature = 25

# Example 1
if is_sunny:
    print("It's a sunny day!")
else:
    print("It's not sunny.")

# Example 2
if temperature > 30:
    print("It's hot!")
elif temperature > 20:
    print("It's warm.")
else:
    print("It's cool.")

# Example 3
is_raining = True
if is_sunny and not is_raining:
    print("It's sunny and not raining.")
elif is_sunny and is_raining:
    print("It's sunny but raining.")
else:
    print("It's not sunny or raining.")
