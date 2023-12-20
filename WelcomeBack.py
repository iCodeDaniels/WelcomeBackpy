price = 20
rating = 4.9
name = 'Ifeoluwa'
is_published = False
print(price)

fullname = 'John Smith'
age = 20
is_new= True

name = input("What is your name?: ")
print("Heyo", name)

name = input("What is your name?: ")
color = input("What is your favorite color?: ")
print("Heyoo", name, "likes" , color)

birth_year = int(input("What is your year of birth? "))
age = 2023 - birth_year
print(age)

# FLOAT
weight_lbs = float(input("Input your weight: "))
weight_kg = weight_lbs * 0.45
print(weight_kg, "kg")

course = "Python's Course for 'beginners'"
print(course)

# EMAIL-LIKE or MULTIPLE LINES OF STRINGS
email_message = ''' 
Hey Akinloye, Ifeoluwa Daniel
welcome onboard to this great flight

with love
from the: Support Team
'''
print(email_message)

# INDEXING
name = "Ifeoluwa Daniel Akinloye"
print(name[:])

# FORMATTED STRINGS
first_name = "Ifeoluwa"
last_name = "Akinloye"
message = f'{first_name} {last_name} is a coder'
print(message)

# LENGTH OF CHARACTER
official_name = "Ifeoluwa Daniel Akinloye"
# print(len(official_name))
print(official_name.upper())

# MATH FUNCTION
x = 2.9
print(round(x))
print(abs(x))

import math
print(math.ceil(2.9))

# IF STATEMENT
full_name = input("What is your name? ")
body_temp = float(input("What is your body temperature? "))
weather = 35.6

if body_temp > weather:
    print('''It's a hot day for you''', full_name ,

    '''You need to see the doctor''')
else:
    print("OK! Have a good day", full_name)
print("Happy New Year")