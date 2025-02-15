def circle (r):
    return 3.142 * r **2

def rectangle (w,l):
    return w * l

def square (a):
    return a **2

def triangle (b,h):
    return 1/2 * b * h

print("Enter your shape:")
print("a. circle")
print("b. rectangle")
print("c. square")
print("d. triangle")

choice = input("Please enter your choice:")

if choice == 'a':
    num1 = int(input("enter a value:"))
    print(circle(num1))

elif choice == 'b':
    num1 = int(input("enter a value:"))
    num2 = int(input("enter a value:"))
    print(rectangle(num1,num2))

elif choice == 'c':
    num1 = int(input("enter a value:"))
    print(square(num1))

elif choice == 'd':
    num1 = int(input("enter a value:"))
    num2 = int(input("enter a value:"))
    print(triangle(num1,num2))    

