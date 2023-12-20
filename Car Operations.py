# CAR GAME USING WHILE LOOP
command = ""
started = False

while command != "quit":
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started for a while")
        else:
            started = True
        print("The car is started already")
    elif command == "stop":
        if not started:
            print("The car stopped a while ago")
        else:
            started = False
        print("The car has stopped")
    elif command == "help":
        print('''
Start ---- Press the start button to turn on the car
Stop ---- Press the stop button to put off the car
Quit ---- Fully switching off the car
        ''')
        break
    else:
        print("I don't understand your input")