date = "march 4 2026"
while True:
    option = input("would yoy like to add a entry, read your diary, or delete it, answer in add, read, delete: ")
    if option == "add":
        with open("diary.txt", "a") as d:
            count = 0
            entry = input("what would you like to add: ")
            d.write(date +  " " + entry + "\n")
            entry.split()
            for i in entry:
                count += 1
            print(f"your entry has been added to your diary and you added {count} characters")
    elif option == "read":
        with open("diary.txt", "r") as d:
            print(d.read())
    elif option == "delete":
        sure = input("are you sure you want to delete your diary, answer in yes or no: ")
        if sure == "yes":
            print("your diary has been deleted")
            with open("diary.txt", "w") as d:
                d.write("")
        else:
            print("ok, your diary will not be deleted")
    else:
        print("invalid option, please try again")