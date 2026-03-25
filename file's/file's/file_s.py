file = open("quotes.txt", "r")
for line in file:
    parts = line.split("-")  # Split the line into quote and author
    quote = parts[0]  # Take the first part (the quote)
    quote = quote.replace('"', '').strip()  # Remove quotation marks and extra spaces
    print(quote)  # Print the cleaned quote
file.close()