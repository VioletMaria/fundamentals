# 1. TASK: print "Hello World"
print("Hello World")
# 2. print "Hello Noelle!" with the name in a variable
name = "Violet"
print(f"Hello", name, "!")	# with a comma
print("Hello " + name + "!")	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 13
print(f"Hello", name, "!")	# with a comma
print("Hello " + str(name) + "!")	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
 # with .format()
fave_food1 = "spaghetti"
fave_food2 = "garlic bread"
print("I love to eat {} and {}.".format(fave_food1, fave_food2)) # with an f string
print(f"I love to eat {fave_food1} and {fave_food2}.") # with an f string

for i in range(50):
    print(i)
 

# print("Hello World!")

# x = "Hello Python"
# print(x)
# y = 42
# print(y)

# import random

# print('Welcome to Python!')

# print('This is a loop printing 5 times')
# for x in range(1, 6):
#     print(f'x is: {x}')

# weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
# day = random.choice(weekdays)

# print(f'Today is: {day}')

# if day == 'Monday':
#     print('It will be a long week!')
# elif(day == 'Friday'):
#     print('Woohoo, time for the weekend!')
# else:
#     print('Not quite there yet.')
