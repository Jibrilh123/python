import math

def rectangle():
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    area = length * width
    perimeter = 2 * (length + width)
    print(f"Area: {area}, Perimeter: {perimeter}")

def square():
    side = float(input("Enter side length: "))
    area = side ** 2
    perimeter = 4 * side
    print(f"area: {area}, Perimeter: {perimeter}")

def circle():
    radius = float(input("Emter radius: "))
    area = 3.14 * radius ** 2
    circumfrence = 2 * 3.14 * radius
    print(f"Area : {area} Perimeter: {circumfrence}")

def triangle():
    base = float(input("Enter side base: "))
    height = float(input("Enter side height: "))
    side = float(input("Enter third side"))
    area = 1/2 * base * height
    perimeter = base + height + side
    print(f"Area: {area}, Perimeter {perimeter}")

def pentagon():
    side = float(input("Emter side lenght: "))
    area = (1/4) * ((5 * (5 + 2 *(5 ** 0.5))) ** 0.5) * side ** 2
    perimeter = 5 * side
    print(f"Area: {area} Perimeter: {perimeter}")

def choose():
    while True:
        print("\nChoose a shape:")
        print("1. Rectangle")
        print("2. Square")
        print("3. Circle")
        print("4. Triangle")
        print("5. Pentagon")
        choice = input("Enter choice: ")

        if choice == "1":
            rectangle()
        elif choice == "2":
            square()
        elif choice == "3":
            circle()
        elif choice == "4":
            triangle()
        elif choice == "5":
            pentagon()
            break
        else:
            print("invalid choice, try again.")

        