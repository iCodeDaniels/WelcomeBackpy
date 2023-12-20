# A CERTAIN AMOUNT OF CHARACTERS
# name = input("What is your full name?: ")
#
# if len(name) < 3:
#     print("The name must be at least 3 characters long")
# elif len(name) > 50:
#     print("The name must be a maximum of 50 characters")
# else:
#     print("A valid name")


hihest_temperature = 35.5
lowest_tempetature = 25.0
print("Please in your details")
details1 = str(input("Your name: "))
details2 = int(input("Your age: "))
details3 = float(input("Input your temperature: "))

if details3 >= hihest_temperature:
    print("You temperature is really high!!")
elif details3 < lowest_tempetature:
    print("You might need to see a doctor!!")
elif details3 >= lowest_tempetature and details3 <= hihest_temperature:
    print("You have a good temperature...")

# WEIGHT CONVERTER
# weight = int(input("Weight: "))
# unit = input("(L)bs of (k)g: ")
# if unit.upper() == 'L':
#     converted_weight = weight * 0.45
#     print(f"You are {converted_weight} kilos")
# else:
#     converted_weight2 = weight / 0.45
#     print(f"Your weight is {converted_weight2} (L)bs")
#
# WHILE LOOP
# i = 1
# while i <= 5:
#     print(i)
#     i = i + 2
# print("Done")


# GUESSING GAME
# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input("What is your guess: "))
#     guess_count += 1
#     if guess == secret_number:
#         print("You Win")
#         break
# else:
#     print("You lose")


# FOR LOOP
# prices = [10, 20, 30]
#
# total = 0
# for price in prices:
#     total += price
# print(f"Total: {total}")

# BASICS OF LIST
names = ['Daniel', 'Akinloye', 'Ifeoluwa', 'Damilola']
names[0] = 'Damian'.upper()
print(names)

# 2D OBJECTS
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for numbers in row:
        print(numbers)
# print(matrix[1][2])[