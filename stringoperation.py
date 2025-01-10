name = "pennguin"
age = 16
is_student = True
weight = 48.6

# printing the different type of data type
print("Name : " ,name)
print(" Data type of name is", type(name))

print("Age : ",age)
print("Data Type of Age is :", type(age))

print("is_student : ", is_student)
print(" Data Type of is_student :" ,type(is_student))

print("weight: ", weight)
print("Data Type of weight is :", type(weight))

print("\n After Type Casting....")
age = str(age)
print(age)
print("Data Type of age is", type(age))
weight = int(weight)
print(weight)
print("Data type of weight is", type(weight))