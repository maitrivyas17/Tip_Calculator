# Calculate your split :p
print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, 0r 15? "))
people = int(input("How many people to split the bill? "))
tip_cal = float(total_bill* (tip/100))
split = round((total_bill + tip_cal) / people, 2)#round function because we can two digits after decimal for split
print (f"Each person's split is: ${split}")
