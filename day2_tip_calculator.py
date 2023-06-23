print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? RS."))
people = int(input("How many people to split the bill? "))
perc = int(input("What percentage tip would you like to give? 10, 12, 15"))

tip = (bill * perc)/100
amount = tip + bill
pay = amount/people

print("Each person should pay: Rs",round(pay,2))