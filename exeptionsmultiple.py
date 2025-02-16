try:
    num1, num2 = eval(input("enter two numbers, separated by a cpmma:"))
    result = num1 / num2
    print("result is", result)

except ZeroDivisionError:
    print("Division by zero is error !!")

except SyntaxError:
    print("Comma is missing. Enter numbers separated by comma like this 1, 2")

except:
    print("Wrong input")

else:
    print("No exceptions")

finally:
    print("This will excevute no matter what")                    

