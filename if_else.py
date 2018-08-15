# This program will calculate the value of a number .
#
# n = int(input("Number? "))
# if n < 0:
#     print("The absolute value of", n, "is", -n)
# else:
#     print("The absolute value of", n , "is", n)


# name = input("Your name is : ")
# if name == "Arpita":
#     print("That is a nice name.")
# elif name == "Apu":
#     print("That is funny name.")
# elif name == "Jannat":
#     print("This is beautiful name.")
# else:
#     print("You have a nice name.")

# input("Enter the number: ")
number = 10
guess = 0
count = 0

print("Guess the number!")
while guess != number:
    guess = int(input("Enter the Number : "))
    count = count + 1
    if guess == number:
        print("You are right!")
    elif guess < number:
        print("It's bigger")
    elif guess > number:
        print("It's lower")
        if count > 3:
            print("You are expired. Don't try again")
        else:
            print("Good Job")


