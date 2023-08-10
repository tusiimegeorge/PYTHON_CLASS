"""# // return the quotient without the remainder


Comparison Operators
== equal to
!= not equal to
> greater than
>= greater than or equal to
<= less than or equal to

Logical Operators
Logical AND 'and' 
Logical OR 'or'
Logical NOT 'not'

Assignment Operators
Assign value: '='
Add value: '+'
Add and assign: '+='
Subtract and assign: '-='
Divide and assign: '/='
Modulus and assign: '%='
Exponentiate and assign: '**='

Membership Operators
In: 'in' - checks if a value exists in a sequence
Not in: 'not in' - checks if a value does not exist in a sequence


Identity Operators
Is: 'is' operator: checks if two values are not the same

"""




print(2**5)
print(3+5)
print(12%3)
print(12/3)
print(12//3)
print(12*3)
print(12-3)
print(12+3)
a = 5
print(a)

#Comparison Operators
a = 23.5
b = 15
c = 9

#Greater than
if (b > a):
    print("a is greater than b")
else:
    print("a is less than b")
    print(b > a)

#Less than
if (c < a):
    print("c is less than a")

#Greater than or equal to
if (a >= b):
    print("a is greater than or equal to b")

#Less than or equal to
if (c <= a):
    print("c is less than or equal to a")

#Equal to
if (a == b):
    print("a is equal to b")

#Not equal to
if (a != b):
    print("a is not equal to b")

#Examples with Logical Operators
a = True
b = False

#Logical AND
print(a and b)

#Logical OR
print(a or b)

#Logical NOT
print(not a)




#print(a += b)

#Identity operators
x = 12 
y = 12

print(x != y)

"""
Bitwise AND ('&'): performs bitwise AND operation between the correspoding bits of two operands
Bitwise OR ('|'): performs bitwise OR operation between the correspoding bits of two operands
Bitwise XOR ('^'): performs bitwise XOR operation between the correspoding bits of two operands
Bitwise NOT ('~'): performs bitwise NOT operation on a single operand
Bitwise left shift ('<<'): performs bitwise left shift operation on a single operand
Bitwise right shift ('>>'): performs bitwise right shift operation on a single operand
"""

#Examples on Bitwise Operators
a = 12 #in binary notation 12 is 1212
b = 20 #in binary notation 20 is 12120

#Bitwise AND
print(a & b)

#Bitwise OR
print(a | b)

#Bitwise XOR
print(a ^ b)

#Bitwise NOT
print(~a)

#Bitwise left shift
print(a << 2)

#Bitwise right shift
print(a >> 2)

#Simple Calculator application

#tkinter learn

#Assignment: create a simple calculator program with a GUI interface.
#Make your title of the calculator program with window with your name eg 'Tusiime George Trevour' simple calculator



import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
window = tk.Tk()
window.title("Tusiime George Trevour Simple Calculator")

# Create the entry field
entry = tk.Entry(window, width=25, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=12, pady=12)

# Create the number buttons
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '00', '+']
]

for i in range(len(buttons)):
    for j in range(len(buttons[i])):
        button = tk.Button(window, text=buttons[i][j], padx=40, pady=20,
                           command=lambda number=buttons[i][j]: button_click(number))
        button.grid(row=i+1, column=j, padx=5, pady=5)

# Create the clear button
button_clear = tk.Button(window, text="Clear", padx=30, pady=20, command=button_clear)
button_clear.grid(row=len(buttons)+1, column=0, padx=5, pady=5)

# Create the equal button
button_equal = tk.Button(window, text="=", padx=40, pady=20, command=button_equal)
button_equal.grid(row=len(buttons)+1, column=1, columnspan=2, padx=5, pady=5)

# Start the main event loop
window.mainloop()










