while True:
    file = input("Enter the file name: ")
    try:
        opend = open(file, 'r')
        break
    except FileNotFoundError:
        print("File not found. Please check the file name and try again.")

word = input("Enter the word to search: ")
count = 0
for line in opend:
    if word in line:
        count += 1
print("The word", word, "appears", count, "times in the file.")