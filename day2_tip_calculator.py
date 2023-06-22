print("Welcome to the tip Calculator")
bill = float(input("What was the total bill? Rs"))
people = int(input("How many people to split the bill? "))
perc = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

tip = (bill*perc)/100

final_amount = bill + tip

pay = final_amount / people

print(f"Each person should pay: Rs{pay}")                  