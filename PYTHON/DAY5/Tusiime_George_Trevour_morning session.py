# Control Flow Statements in Python
# If Statement:
# The if statement allows you to execute a code block if a certain condition is true. 
#It provides the ability to make decisions in your code based on different conditions. 
#You can use elif to check additional conditions, and else to specify a code block when none of the conditions  are true.

# For Loop:
# The for loop is used to iterate over a sequence or iterable object. 
#It allows you to execute a code block for each item in the sequence. 
#This loop is useful when you want to perform a repetitive task for a specific number of times or go 
#through each element in a collection.

# While Loop:
# The while loop executes a code block as long as a certain condition remains true. 
#It repeatedly checks the condition before each iteration. 
#It is helpful when you need to perform a task until a specific condition is met or 
#until a certain event occurs.

# Break Statement:
# The break statement is used to exit a loop prematurely. 
#When a break statement is encountered, the loop is immediately terminated, 
#even if the loop condition is still true. 
#It is often used to stop the execution of a loop based on a certain condition.

# Continue Statement:
# The continue statement allows you to skip the current iteration of a loop and move to the next iteration. 
#When the continue statement is encountered, the remaining code in the loop for 
#the current iteration is skipped, and the loop proceeds with the next iteration.

# Pass Statement:
# The pass statement is a placeholder that does nothing. 
#It is used when a statement is required syntactically but you don't want to perform any action. 
#It is commonly used as a placeholder for future code or when an empty block is needed.

# Try-Except Statement:
# The try-except statement is used to handle exceptions (errors) that may occur during the execution of code. 
#The try block contains the code that may raise an exception. 
#If an exception occurs, it is caught by the corresponding except block, allowing you to handle the exception gracefully. 
#The else block is executed if no exceptions are raised, and the finally block is always executed, 
#regardless of whether an exception occurred or not.

# ## Exercise 1
# ## Prompting  a student to enter their mental health rating

# Prompt the student to enter their mental health rating
rating = int(input("Please enter your mental health rating (from 1 to 10): "))


if rating < 1 or rating > 10:
    print("Invalid rating. Please enter a number between 1 and 10.")
else:
    if rating >= 8:
        print("Great! You're doing well.")
    elif rating >= 6:
        print("You're doing okay, but there's room for improvement.")
    else:
        print("Make sure to take care of yourself and seek medical support very fast.")
