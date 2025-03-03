
import random

def main():
    # intro speech
    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down! Survive your \ndesert trek and out run the natives.")

    # variables
    miles_traveled = 0
    thirst = 0
    camel_tiredness = 0
    native_miles_traveled = -20
    canteen_amount = 3

    done = False

    # while code runs
    while not done:
        # all player options
        print("A. Drink from your canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("Q. Quit.")

        # ask player what they want to do
        user_input = input("What is your choice? ")

        # if player wants to quit
        if user_input.upper() == "Q":
            done = True
            print("OK, game over")

        # if player wants to check status
        elif user_input.upper() == "E":
            print("You've traveled", miles_traveled, "miles.")
            print("You have", canteen_amount, "swigs of your canteen left.")
            print("The natives are", miles_traveled - native_miles_traveled, "miles behind you!")

        # if player wants to stop for the night
        elif user_input.upper() == "D":
            camel_tiredness = 0
            print("The camel is happy")
            native_miles_traveled = native_miles_traveled + random.randrange(7, 15)
            print("The natives are", miles_traveled - native_miles_traveled, "miles behind you!")

         # if player wants to move full speed
        elif user_input.upper() == "C":
            miles_traveled = miles_traveled + random.randrange(10, 21)
            print("You traveled", miles_traveled, "miles.")
            thirst = thirst + 1
            camel_tiredness = camel_tiredness + random.randrange(1, 4)
            native_miles_traveled = native_miles_traveled + random.randrange(7, 15)
            if not done and random.randrange(20) == 0:
                print("You found an oasis!")
                canteen_amount = 3
                thirst = 0
                camel_tiredness = 0

         # if player wants to move moderate speed
        elif user_input.upper() == "B":
            miles_traveled = miles_traveled + random.randrange(5, 12)
            print("You've traveled", miles_traveled, "miles.")
            thirst = thirst + 1
            camel_tiredness = camel_tiredness + 1
            native_miles_traveled = native_miles_traveled + random.randrange(7, 15)
            if random.randrange(20) == 0:
                print("You found an oasis!")
                canteen_amount = 3
                thirst = 0
                camel_tiredness = 0

        # if player wants to drink
        elif user_input.upper() == "A":
            if canteen_amount == 0:
                print("Error")
            elif canteen_amount == 1 or 2 or 3:
                print("You drink some water")
                canteen_amount = canteen_amount - 1
            thirst = 0

        # if player is thirsty
        if not done and thirst == thirst > 3 and thirst <6:
            print("You are thirsty.")

         # if player dies of thirst
        elif not done and thirst >= 6:
            print("You died of thirst.")
            done = True

        # if camel tired
        if not done and camel_tiredness == camel_tiredness > 4 and camel_tiredness <8:
            print("Your camel is getting tired.")

        # if camel dies of tiredness
        elif not done and camel_tiredness >= 8:
            print("Your camel is dead.")
            done = True

        # if native catch you
        if miles_traveled <= native_miles_traveled:
            print("The natives caught you!")
            done = True

        # if natives are approaching
        elif not done and native_miles_traveled - miles_traveled > -15:
            print("The natives are getting close!")

        # if you reach the end
        if not done and miles_traveled >= 200:
            print("You won!")
            done = True





main()