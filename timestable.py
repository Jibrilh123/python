valid = False

while not valid:
    try:
        n = int(input("Enter a number: "))
        valid = True
    except ValueError:
        print("Number is invalid, Please enter a valid number")

print(f"Multiplication for {n}:")
for i in range (1,16):
    print(f"{n} x {i} = {n * i}")

            


