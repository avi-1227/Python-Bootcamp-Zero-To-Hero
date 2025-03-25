# I have learned in day-02 concept about Data Types, Numbers, Operations, Type Conversion, f-Strings 

# len() - To count number of characters in string not number
# Primite Data Type - 
# 1. Strings 
# 2. Integers 
# 3. Floats 
# 4. Booleans  

###################################### 

# Tip Calculator

print('Welcome to the tip calculator!')
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
tip_as_percent = tip/100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill/people
final_amount = round(bill_per_person, 2)
print(f'Each person have to pay bill ${final_amount}')
