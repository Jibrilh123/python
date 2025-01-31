n = int(input("Enter your number of patterns: "))

num = 1

for i in range (1,n+1):
    for j in range (1, i+1):
        print(num*2,end="\t")
        num = num+1
    print()    

