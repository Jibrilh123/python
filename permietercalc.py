def square (a):
    return a*4

def triangle (a,b,c):
    return a+b+c

def rectangle (l,w):
    return 2*(l+w)

def circle (r):
    return 2*3.14*r

print ("Please enter your operation:")
print("a. square")
print("b. triangle")
print("c. rectangle")
print("d. circle")

choice = input("Please enter your choice:")

if choice == 'a':
    num = int(input("Enter length of side"))
    print(square(num))

elif choice == 'b':
    num1 = int(input("Enter one side:"))  
    num2 = int(input("Enter other side:")) 
    num3 = int(input("Enter other side:"))   
    print(triangle(num1,num2,num3))

elif choice == 'c':
    num = int(input("Enter length:"))
    num1 = int(input("Enter width:"))
    print(rectangle(num,num1))

elif choice == 'd':
    num = int(input("Enter radius:"))
    print(circle(num))    
   



    