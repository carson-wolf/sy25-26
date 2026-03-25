seeds = [1, 16, 8, 9, 5, 12, 4, 13, 6, 11, 3, 14, 7, 10, 2, 15]
winners = ['Purdue', 'FDU', 'FAU', 'Memphis', 'Duke', 'Oral Roberts', 'UVA', 'Furman', 'Kentucky', 'Pitt', 'Kansas', 'Howard', 'Texas', 'Penn St', 'UCLA', 'UNC Asheville']
count = 0
for i in seeds:
    if i >= 10:
        index = seeds.index(i)
        print(f"cinderella story: {winners[index]} win ")
        count += 1
print(count)