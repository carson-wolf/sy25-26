a = int(input("enter a number: "))
b = int(input("enter a number: "))

c = int(input("enter a number: "))
d = int(input("enter a number: "))

e = int(input("enter a number: "))
f = int(input("enter a number: "))

l = int(input("enter a number: "))
m = int(input("enter a number: "))

r = int(input("enter a number: "))
s = int(input("enter a number: "))

t1 =(a, b)
t2 =(c, d)
t3 =(e, f)
t4 =(l, m)
t5 =(r, s)

l1 = [t1, t2, t3, t4, t5]
print(l1)

for i in range(len(l1) - 1):
    x1, y1 = l1[i]
    x2, y2 = l1[i + 1]
    print(x2, y2)