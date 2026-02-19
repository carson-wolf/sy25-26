dict = {}
print("options: [1] add to list, [2] remove from list, [3] view list, [4] exit")
while True:
    choice = int(input("enter your choice: "))
    if choice == 4:
        break
    elif choice == 1:
        item = input("enter the name of the item you are adding: ")
        quan = int(input(f"enter amount of {item} you want to add: "))
        if item in dict:
            dict[item] += quan
        else:
            dict[item] = quan
        print("options: [1] add to list, [2] remove from list, [3] view list, [4] exit")
    elif choice == 2:
        item = input("enter the name of the item you are removing: ")
        quan = int(input(f"enter amount of {item} you want to remove: "))
        if item in dict:
            if quan > dict[item]:
                print(f"you only have {dict[item]} {item} in your list")
            else:
                dict[item] -= quan
        else:
            print(f"{item} is not in your list")
        print("options: [1] add to list, [2] remove from list, [3] view list, [4] exit")
    elif choice == 3:
        for i in list(dict):
            if dict[i] <= 0:
                del dict[i]
        print("your list: ")
        for item in dict:
            print(f"{item}: {dict[item]}")
        print("options: [1] add to list, [2] remove from list, [3] view list, [4] exit")
    else:
        print("invalid choice, try again")
        print("options: [1] add to list, [2] remove from list, [3] view list, [4] exit")
