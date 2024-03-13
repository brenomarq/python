# Tip Calculator
print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $ "))
percentage_choice = float(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = float(input("How many people to split the bill? "))

percentage = 1 + (percentage_choice / 100)
splitted_bill = (bill * percentage) / people

print(f"Each person should pay: ${splitted_bill:.2f}")
