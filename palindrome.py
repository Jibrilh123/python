def palindrome(r):
    e = len(r) -1
    s= 0
    while (s < e):
        if (r[s]!=r[e]):
            return False
        s = s+ 1
        e = e-1
        return True

r = (1,2,3,3,2,1)
if(palindrome(r)):
    print ("The tuple is flip flop")
else:
    print("The tuple is not Flip Flop")