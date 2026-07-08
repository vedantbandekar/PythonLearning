
# nested loop = A loop within another loop (outer, inner)
#           outer loop:
#                inner loop:

# -------------------------------------------------

for x in range(1, 10):
    print(x, end=" ")

# -------------------------------------------------

for x in range (3):
    for y in range(1, 10): #inner loop
        print(y, end="")
    print()  #print new line (outer loop)

# -------------------------------------------------

rows = int(input("Enter number of rows: "))
column = int(input("Enter number of columns: "))
symbol = input("Enter a symbol: ")

for x in range(rows):
    for y in range(column):
        print(symbol, end="")
    print()
