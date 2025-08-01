print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, 15? "))
final_bill = bill * (1+ tip / 100)
people = int(input("How many people to split the bill? "))
bill_per_person = final_bill / people
print(f"Each person should pay: ${round(bill_per_person,2)}")

