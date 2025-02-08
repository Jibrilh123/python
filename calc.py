def add (a,b):
    return a + b

def subtract (a,b):
    return a - b

def multiply (a,b):
    return a * b

def divide (a,b):
    return a / b

print("Please enter your operations:")
print("a. add")
print("b. Subtract")
print("c. multiply")
print("d. divide")

choice = input("Please enter choice")

num1 = int(input("enter one number:"))
num2 = int(input("enter another number:"))

if choice == 'a':
    print(add(num1,num2))

elif choice == 'b':
    print(subtract(num1,num2))

elif choice == 'c':
    print(multiply(num1,num2))

elif choice == 'd':
    print(divide(num1,num2))        
