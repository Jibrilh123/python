num = int(input("Enter your upper range: "))
num1 = int(input("Enter your lower range"))
print("Range is",num,"to ",num1)
for i in range(num,num1+1):
    if i > 1:
        for g in range (2,i):
            if (i%g)==0:
                break
        else :
            print(i)

