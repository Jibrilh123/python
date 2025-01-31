n = int(input("Enter the number of rows you want your pattern to be: "))

for i in range (n):
    for j in range (i+1):
        print("* \t", end="")
        
    print()    