import random

# print("Hello World")
# age = 25

# print(type(age))

# user_name = input(" Enter your name")
# print("hello",user_name)

# num = int(input("Enter a number : "))
# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else : print("Zero")

# for i in range(1,6):
#     print("Number is : ", i)

# count = 0
# while count < 5:
#     print("Count",count)
#     count+=1

# number = int(input("Enter a Number:"))
# print("Double the number is:", number*2)

# for i in range (1,11):
#     print("Number is",i)

# number = int(input("Enter a Number:"))
# if number%2 == 0:
#     print("Number is Even")
# else: 
#     print("Number is odd")

# def greet(name):
#     print("Hello",name)

# greet("Alice")

# fruits = ["apple","banana","Mango"]
# print(fruits[0])

# person = {"name" : "Rugwed", "age" : "28"}
# print(person["name"])

number_to_guess = random.randint(1,100)
attempts = 0

print("Welcome to Number Guessing Game")
while True:
    guess = int(input("Enter a number"))
    attempts+=1

    if guess< number_to_guess:
        print("Too low")
    elif guess>number_to_guess:
        print("too High")
    else:
        print(f"Congratulations you have guessed in {attempts} Attempts")
        break