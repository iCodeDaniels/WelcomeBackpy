 # DICTIONARY
customer = {
     "name": "John Smith",
     "age": 30,
     "it's verified": True

}
print(customer.get("it's verified"))


# EMOJI FACE CONVERTER
message = input("> ")
words = message.split(' ')
emojis = {
     ":)": "LOL",
     ":(": "SMH"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)


# DEFINE A SIMPLE FUNCTION
def greet_user(first_name, last_name):
    print(f"Hey there, {first_name} {last_name}")
    print("Welcome aboard")

greet_user("Daniel", "Wilson")
# greet_user("Williams")
# greet_user("Martins")


# DICTIONARY
airport_information = {
    "Name": "Ifeoluwa Daniel Akinloye",
    "Airline": "Fly Emirates",
    "Boarding_gate": "Gate:45B",
    "Boarding_time": "9:55pm",
    "Slip": "Slip2"
}

print(airport_information.get("Name"))
print(airport_information.get("Airline"))
print(airport_information.get("Boarding_gate"))
print(airport_information.get("Boarding_time"))
print(airport_information.get("Slip"))


def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "LOL",
        ":(": "SMH"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input("> ")
print(emoji_converter(message))


# EXCEPTIONS FOR ERRORS
try:
    age = int(input("How old are you?: "))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
     print("Age can not be 0")
except ValueError:
    print("Invalid value")


class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")

point1 =Point()
point1.x = 10
point1.draw()
print(point1.x)