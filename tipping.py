def totalCal(billAmount, tip):
    total = billAmount*(1+0.01*tip)
    total = round(total,2)
    print(f"Please pay ${total} this is your payable amount")
pay = int(input("Please enter the amount to be paid:"))
tip = int(input("Please enter your desired tip:"))
totalCal(pay,tip) 
