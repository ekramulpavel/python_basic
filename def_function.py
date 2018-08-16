def absolut_value(n):
    if n < 0:
        n = -n
        return n
    n = float(input("Enter the Number : "))
    print("ab value is : ", absolut_value(n))

def print_function():
    print("I am a programmer")
    print("I know programming")
def welcome(name):
    print("Welcome", name)
    print_function()
    welcome("programmer")

# def squ(x):
#     return x*x
# while 1 == 1:
#     x = float(input("enter a number : "))
#     print("result = ", squ(x))


def add(f,l):
    return f+l
def minu(a,b):
    return a-b
def intu(g,h):
    return g*h
def div(t,u):
    return t/u
def print_option():
    print("press w to + numbers")
    print("press x to - a number")
    print("press y to * numbers")
    print("press z to / 2 numbers")
    print("press e to exit")
menu_choice = "k"
print_option()
while menu_choice != "e":
    menu_choice = input("enter your choice : ")
    if menu_choice == "w":
        f = float(input("1st number: "))
        l = float(input(
            "2nd number: "))
        print("result = ", add(f,l))
        print_option()
    elif menu_choice == "x":
        a = float(input("from number: "))
        b = float(input("to number : "))
        print("result = ",minu(a,b))
        print_option()
    elif menu_choice == "y":
        g = float(input("enter 1st number: "))
        h = float(input("enter 2nd numbers : "))
        print("result = ",intu(g,h))
        print_option()
    elif menu_choice == "z":
        t = float(input("enter the number you want to devide : "))
        u = float(input("enter the number by which youn want to devide : "))
        print("result = ",div(t,u))
        print_option()
    elif menu_choice == "e":
        print("bye.........")
    else:
        print("please press a correct key")
        print_option()
