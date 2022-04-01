N = input();
word = input("Please input the word: ")

while N.isnumeric() != True or 0 > int(N) or int(N) > 100:
    print("please input a number between 0 and 100")
    N = input("LENGTH ")

while word.isnumeric() == True or 1 > len(word) or len(word) > 50:
    print("please input a string between 1 and 50 characters")
    word = input("THE WORD ")

result = (word + "\n") * int(N)
print(result)