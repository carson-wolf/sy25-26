w = int(input("enter the weight: "))
if w < 100:
    g = "small"
elif 100 <= w < 200:
    g = "medium"
else:
    g = "large"
print(g)

l = []
for i in range (5):
    bl = int(input("enter blemish"))
    l.append(bl)
tb = sum(l)
av = tb/5
print(f"total blemish count is {tb}")
print(f"average blemish is {av}")

pot = [0,2,5,1,0,8,3,0]
p = []
for i in pot:
    if i == 0:
        p.append(i)
per = (len(p)/len(pot)) * 100
print(per)