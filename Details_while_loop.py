# password = str()
# while password != "hello":
#     password = input("password: ")
# print("Welcome in")


# This program will verify your username and password
# name = input("What is your UserName: ")
# password = input("What is your Password: ")
#
# input1 = None
# input2 = None
#
# while input1 != name:
#     input1 = input("Please enter your current username: ")
# while input2 != password:
#     input2 = input("Please enter your password: ")
# print("Welcome back to your system")

a = 0
b = 1
count = 0
while count != 5:
    count = count + 1
    print(a, b)
    a = a + b
    b = a + b