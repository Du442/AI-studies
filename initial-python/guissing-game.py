import random

random_number = random.randint(0, 1001)

while True:
    try:
        typed_number = int(input("Enter a integer number between 1 and 1000: "))
        if typed_number > random_number:
            print("\nThe random number is less!\n")
        elif typed_number < random_number:
            print("\nThe random number is higher!\n")
        else:
            print("\nYou hit the random number, nice!!!")
            break
    except ValueError:
        print("Type a number, not a str")