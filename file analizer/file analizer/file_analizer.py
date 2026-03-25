import glob

# Get all .txt files in the directory

files = glob.glob("server_dump/*.txt") 
W_l = []
O_l = []
E_l = []
warn = 0
ok = 0
error = 0

for file in files:
    with open(file, "r") as f:
        new = f.read()
        if "WARN" in new:
            warn += 1
            W_l.append(file)
        elif "OK" in new:
            ok += 1
            O_l.append(file)
        elif "ERROR" in new:
            error += 1
            E_l.append(file)
print(f"there are {warn} warn statuses")
print(f"there are {ok} ok statuses")
print(f"there are {error} error statuses")
an = input("what do you want to see? (warn/ok/error)")
if an == "warn":
    for i in W_l:
        print(i)
elif an == "ok":
    for i in O_l:
        print(i)
elif an == "error":
    for i in E_l:
        print(i)