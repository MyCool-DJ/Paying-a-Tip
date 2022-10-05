#day 10 if my first 100days of code challenge 
print("Hi, I am your AI teller")
bill = int(input("What is your total bill? "))
tip = int(input("Enter the amount you want to tip, 15%, 18%, or 20%? "))
splitting = int(input("And how many people are we splitting that between? "))
tip_amount = (tip / 100) * bill
grand_total = tip_amount + bill
print("Your grand total is,", grand_total)
print("Thank you")