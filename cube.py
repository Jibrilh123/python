def cube(num):
    return num**3
def check(num):
    if num % 3 ==0:
        return cube(num)
    else:
        return False
print(check(8))
print(check(9))