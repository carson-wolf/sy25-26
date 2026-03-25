import json 
while True:
    mode = input("are you loading a save or making a new one enter load or new: ")
    if mode == "new":
        with open("saves.txt", "w") as file:
            name = input("what is the name of your save: ")
            invintory = []
            level = int(input("what level are you: "))
            items = int(input("how many items do you have: "))
            for i in range(items):
                item = input("what is the name of your item: ")
                invintory.append(item)
            save = {"name": name, "inventory": invintory, "level": level}
            json.dump(save, file)  
    elif mode == "load":  
        try:  
            with open("saves.txt", "r") as file:    
                save = json.load(file)  
        except FileNotFoundError:  
            print("no save found")  
            continue  
        except json.JSONDecodeError:  
            print("save file is corrupted or empty")  
            continue  
        print(f"Name: {save['name']}")  
        print(f"Inventory: {save['inventory']}")  
        print(f"Level: {save['level']}")  

    else:
        print("invalid input enter new or load")
