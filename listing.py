# select_month = int(input("What month (1-12)? "))
# months =['January', 'February', 'March', 'April', 'May', 'June', 'July',
#          'August', 'September', 'October', 'November', 'December']
# if 1 <=select_month <= 12:
#     print("The month is",months[select_month - 1])





# demolist =["life", 42, "the universe", 6, "and", 9]
# print("demolist = ",demolist)
# demolist.append("everything")
# print("after 'everything' was appended demolist is now:")
# print(demolist)
# print("len(demolist) =", len(demolist))
# print("demolist.index(42) =",demolist.index(42))
# print("demolist[1] =",demolist[1])
# print("demolist is now: ",demolist)
# del demolist[2]
# print("After 'the universe' was removed demolist is now:")
# print(demolist)
# if "life" in demolist:
#     print("'life' was found in demolist")
# else:
#     print("'life' was not found in demolist")
# if "techtunes" in demolist:
#     print("'techtunes' was found in demolist")
# if "techtunes" not in demolist:
#     print("'techtunes' was not found in demolist")

menu_item = 0
namelist = []
while menu_item != 9:
    print("--------------------")
    print("1. Print the list")
    print("2. Add a name to the list")
    print("3. Remove a name from the list")
    print("4. Change an item in the list")
    print("9. Quit")
    menu_item = int(input("Pick an item from the menu: "))
    if menu_item == 1:
        current = 0
        if len(namelist) > 0:
            while current < len(namelist):
                print(current, ".", namelist[current])
                current = current + 1
        else:
            print("List is empty")
    elif menu_item == 2:
        name = input("Type in a name to add: ")
        namelist.append(name)
    elif menu_item == 3:
        del_name = input("What name would you like to remove: ")
        if del_name in namelist:

            item_number = namelist.index(del_name)
            del namelist[item_number]
        else:
            print(del_name, "was not found")
    elif menu_item == 4:
        old_name = input("What name would you like to change: ")
        if old_name in namelist:
            item_number = namelist.index(old_name)
            new_name = input("What is the new name: ")
            namelist[item_number] = new_name
        else:
            print(old_name, "was not found")
print("Goodbye")