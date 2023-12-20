# IF STATEMENT OF A HOUSE PRICE
# print("Welcome to Daniels Estate where luxury meets your price friendly")
# full_name = input("What is your name?: ")
# starting_price_of_house = 1000000
# good_credit = False
#
# if good_credit:
#     down_payment = 0.1 * starting_price_of_house
# else:
#     down_payment = 0.2 * starting_price_of_house
# print(f"Your down payment: ${down_payment}")


# APPLICATION FOR LOAN
print("WALLSTREET MICRO FINANCE BANK")
occupation = input("What do you do for a living?: ")
# monthly_income = int(input("How much do you earn per month?: "))
criminal_record = False
good_credit = True

if good_credit and not criminal_record:
    print("You are Eligible for a loan of up to $60000")
else:
    print("You are not eligible for a loan at this moment")


#Comparison Operators
temp = float(input("What is the room temperature today?: "))

if temp > 34.5 and temp <40:
    print("It's a hot day")
else:
    print("Byeee")
