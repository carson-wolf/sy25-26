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
    if choice == "1":
        print(line_up)