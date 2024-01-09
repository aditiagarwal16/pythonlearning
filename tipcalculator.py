print("Welcome to the tip calculator")

total_bill = float(input("What was the total bill? "))

tip_per = int(input ("What percentage tip would you like to give? 10, 12, or 15"))

people = int(input ("How many people to split the bill? "))

person_to_pay = (total_bill * ( 1 + (tip_per / 100))) / people

print(round(person_to_pay, 2 ))



