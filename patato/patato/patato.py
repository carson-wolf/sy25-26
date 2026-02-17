# sorry i didint do block code i just dont understand how to use them
crate = [
    {"weight": 120, "blemishes": 0, "is rotten": False},
    {"weight": 90, "blemishes": 2, "is rotten": False},
    {"weight": 250, "blemishes": 0, "is rotten": False},
    {"weight": 150, "blemishes": 1, "is rotten": True},
    {"weight": 80, "blemishes": 0, "is rotten": False},
    ]
large = 0
small = 0
median = 0
premium = 0
Rotten = 0
for potato in crate:
    if potato["is rotten"] == True:
        Rotten += 1
    if potato["blemishes"] == 0:
        premium += 1
    if potato["weight"] < 100:
        small += 1
    if potato["weight"] <= 200 and potato["weight"] >= 100:
        median += 1
    if potato["weight"] > 200:
        large += 1
print(f"amount of large potatos is {large}")
print(f"amount of medium potatos is {median}")
print(f"amount of small potatos is {small}")
print(f"amount of rotten potatos is {Rotten}")
print(f"amount of premium potaos is {premium}")