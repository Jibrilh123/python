print("Enter marks as per you scored: ")
math = int(input("Enter marks for maths: "))
english = int(input("Enter marks for english: "))
science = int(input(" Enter marks for science: "))
language = int(input(" Enter marks for arabic: "))

sum = math+english+science+language

print("Sum of all the subjects are: ")

percent = (sum/400)*100

print(end="% marks= ")
print(percent)

