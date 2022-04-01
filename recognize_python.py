num1 = 42 # variable declaration, number
num2 = 2.3 # variable declaration, number
boolean = True # variable declaration, boolean
string = 'Hello World' # variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # initialize dictionary
fruit = ('blueberry', 'strawberry', 'banana') # initialize tuple
print(type(fruit)) # log statement, type check
print(pizza_toppings[1]) # log statement, access list value
pizza_toppings.append('Mushrooms') # add list value
print(person['name']) # log statement, prints dictionary value
person['name'] = 'George' # change dictionary value
person['eye_color'] = 'blue' # change dictionary value
print(fruit[2]) # log statement, access tuple value

if num1 > 45: # conditional, if statement
    print("It's greater") # log statement
else:   # else statement
    print("It's lower") # log statement

if len(string) < 5: # conditional, if statement, length check
    print("It's a short word!") # log statement
elif len(string) > 15: # else if statement, length check
    print("It's a long word!") # log statement
else:   # else statement
    print("Just right!") # log statement

for x in range(5): # for loop, start, increment
    print(x) # log statement, end loop
for x in range(2,5): # for loop, start, increment
    print(x) # log statement, end loop
for x in range(2,10,3): # for loop, start, increment
    print(x) # log statement, end loop
x = 0 # variable declation, number
while(x < 5): # while loop, start
    print(x) # log statement
    x += 1 # increment

pizza_toppings.pop() # delete list value
pizza_toppings.pop(1) # delete second value in list

print(person) # log statement
person.pop('eye_color') # Delete dictionary value
print(person) # log statement

for topping in pizza_toppings: # for loop, start
    if topping == 'Pepperoni': # if statement, boolean
        continue # increment
    print('After 1st if statement') # log statement
    if topping == 'Olives': # if statement, boolean
        break # end loop

def print_hello_ten_times(): # function
    for num in range(10): # for loop, start
        print('Hello') # log statement

print_hello_ten_times() # calling function

def print_hello_x_times(x): # function, parameter
    for num in range(x): # for loop, start
        print('Hello') # log statement

print_hello_x_times(4) # calling function with argument

def print_hello_x_or_ten_times(x = 10): # function, parameter
    for num in range(x): # for loop, start
        print('Hello') # log statement

print_hello_x_or_ten_times() # NameError: name x is not defined
print_hello_x_or_ten_times(4) # calling function with argument


"""
Bonus section
"""

print(num3) # NameError: name <variable name> is not defined
num3 = 72 
fruit[0] = 'cranberry' # TypeError: 'tuple' object does not support item assignment
print(person['favorite_team']) # KeyError: 'favorite_team'
print(pizza_toppings[7]) # IndexError: list index out of range
  print(boolean) #IndentationError: unexpected indent
fruit.append('raspberry') # AttributeError: 'tuple' object has no attribute 'append'
fruit.pop(1) # AttributeError: 'tuple' object has no attribute 'pop'