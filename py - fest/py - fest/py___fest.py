print("---Py-Fest 2026 stage manager!")
print("1.view lineup & Total time")
print("2.add a new band")
print("3.move first band to the end")
print("4.remove a band by name")
print("5.move band to a specific position")
print("6.exit")
choice = input("select an option (1-6): ")
line_up = [
    ("code Play", "indie", 30),
    ("the pythonistas", "rock", 45),
    ("syntax error", "metal", 60),
    ]
while True:
    time = sum(band[2] for band in line_up)
    if choice == "1":
        print(line_up)
        print(f"total time is {time}")
        choice = input("select an option (1-6): ")
    elif choice == "2":
        name = input("enter the name of the band you want to add")
        genera = input("enter the genera of the band to add")
        time = int(input("enter the time of the band your adding"))
        new = (name, genera, time)
        line_up.append(new)
        choice = input("select an option (1-6): ")
    elif choice == "3":
        moved = line_up.pop
        line_up.append(moved)
        print("moved sucsefully")
        choice = input("select an option (1-6): ")