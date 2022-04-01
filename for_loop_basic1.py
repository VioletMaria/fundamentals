# # 1.
# for x in range(151):
#     print(x)

# # 2.
# for multiples in range(5,1001,5):
#     print(multiples)

# # 3.
# for int in range(1,101):
#     if(int%5 == 0):
#         print("Coding")
#     if(int%10 == 0):
#         print("Coding Dojo")

# # 4.
# sum = 0
# for odd in range(1,500001,2):
#     sum += odd

# print(sum)

# # 5.
# pos = 2018
# while(pos > 0):
#     print(pos)
#     pos -= 4

# # 6.
# lowNum = 5
# highNum = 25
# mult = 3
# for r in range(lowNum, highNum+1):
#     if(r%mult == 0):
#         print(r)

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))

def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)