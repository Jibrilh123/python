class A:
    def __init__(self, A):
        self.A = A 
    def __lt__(self, other):
        if(self.A<other.A):
            return "ob1 is less than ob2"
        else:
            return "ob2 is less than ob1"
        
    def __eq__(self, other):
        if(self.A == other.A):
            return "Both are equal"
        else:
            return "Not equal"
        
ob1 = A(2)
ob2 = A(3)
print("Passed values :", ob1.A, ob2.A)
print(ob1 < ob2)
        
