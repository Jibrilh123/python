row = int(input("Enter the number of patterns you want: "))

num = 1
print("Floyds triangle \n") 
for i in range (1,row+1):
    for j in range (1,i+1):
        print(num,end="")
        num = num+1
    print()    
