countdown = 10  # Initialize countdown before the loop
while countdown > 1:
    print(countdown)
    countdown -= 1  # Decrement countdown
    response = input("Should I stop?")
    if response == "yes":
        break
    else:
        continue