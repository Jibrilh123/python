a = int(input("Enter a 3 digit number: "))
sum = 0
temp = a
while temp>0:
    num = temp%10
    sum = sum+num**3
    temp = temp//10

if sum== a:
    print("Your number is an armstrong number")
else:
    print("Your number is not an armstrong number")            
