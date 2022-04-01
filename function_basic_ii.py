# 1. Countdown -
def countDown(num):
    newList = []
    for down in range(num, 0, -1):
        newList.append(down)
    print(newList)

countDown(7)

# 2. Print and Return -
def printAndReturn(val1, val2):
    list = [val1, val2]
    print(list[0])
    return list[1]

a = printAndReturn(2,4)
print(a)

# 3. First Plus Length -
def firstAndLen(list):
    first = list[0]
    length = len(list)
    return str(first) + " and " + str(length)

b = firstAndLen([1,3,4,7,8])
print(b)

# 4. Values Greater than Second -
def greaterThanSec(x):
    sum = 0
    newList = []
    for value in range(len(x)):
        if(x[value] > x[1]):
            sum += 1
            newList.append(x[value])
    print(sum)
    return newList

c = greaterThanSec([1,2,4,1,6,7])
print(c)

# 5. This Length, That Value -
def lengthValue(size, value):
    list = []
    list += size * [value]
    return list

d = lengthValue(4,7)
print(d)