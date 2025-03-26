# Tip Calculator

bill = (float(input("Welcome to the tip calculator!\nWhat is your total bill: $")))
tip = (int(input("How much would you like to tip? (10, 15, 20): ")))
people = (int(input("How many people to split to bill? ")))

total_tip = tip / 100 * bill
total_amount = bill + total_tip
each_pay =  total_amount / people


print (f'Each person ought to pay: ${each_pay}')