command=""
started = False
while True:
    command = input(">").lower()
    if command == "start":
        if started:
            print("Car is already Started")
        else:
            started = True
            print("Car Started.....")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started  =  False
            print("Car Stopped.....")
    elif command == "help":
        print("""Start -  To Start the car
Stop - TO Stop the car
Quit - To Exit""")
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that")