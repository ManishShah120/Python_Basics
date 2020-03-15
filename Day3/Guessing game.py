secret_number = 5
guess_limit = 3
guess_count=0
while guess_count<guess_limit:
    guess=int(input("Guess:"))
    guess_count += 1
    if guess == secret_number:
        print("You Won")
        break
else:
    print("You Lose")


#in python Language While statement also has an Else Staement