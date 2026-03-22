# Set a Countdown Timer

import time

while True:
    try:
        seconds = int(input("Type in the duration in seconds: "))
        if seconds < 1:
            print("Number can't be less than 1")
            continue
        break
    except ValueError:
        print("Enter a number that is 1 or more than 1 !")