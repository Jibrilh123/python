units = int(input("Enter number of units you consumed: "))

if(units<50):
    amount = units * 2.60
    surgecharge = 25
elif (units<=100):
    amount= 130+((units-50)*3.25)
    surgecharge = 35
elif (units<=200):
    amount = 130+162.50+((units-100)*5.26)
    surgecharge= 45
else:
    amount = 130+162+.50+526+((units-200)*8.45)
    surgecharge = 75
total = amount + surgecharge
print("\n Electricty bill = =%.2f" %total)                