class Room:
    """
    this is a class that defines the room
    """
    def __init__(self, description, north, east, south, west):
        """this is the method that sets up the variables"""
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west


def main():

    print()
    print("You awake in an unknown building severely confused as to where you are and what happened to you.\nFinding yourself in a musty, slightly decrepit living room, it's imperative that you find your way out! ")

    room_list = []

    # create the living room (room0)

    room = Room("You are in the living room.\nThere are barred windows on the two walls facing the outside and a door to the east", None, 1, None, None)
    room_list.append(room)

    # create the entry room (room1)

    room = Room("You are in the entry room.\nYou see a small hole surrounded by slightly crumbling wall to the south.\nThere are also doors to the north and east as well as the one you just came from.", 4, 2, 6, 0)
    room_list.append(room)

    #create the kitchen/dining room (room2)

    room = Room("You are in the kitchen.\nThere are cabinets missing doors and cutlery everywhere.\nAll of the windows are boarded.\nA fridge looms from the north of the room.", 7, None, None, 1)
    room_list.append(room)

    #create the library (room3)

    room = Room("You are in the library.\nSeveral large bookshelves are spread throughout the room\nOne of the shelves to the west seems to hold an out of place journal.", None, 4, None, 8)

    room_list.append(room)

    #create the hall (room4)

    room = Room("You are in a hall.\nThere are dirty, cracked portraits speckled about the walls.\n There are doors to the east, west, and back where you came.", None, 5, 1, 3)
    room_list.append(room)

    #create the bedroom (room5)

    room = Room("You are in the bedroom. There is a bed that looks to be in the best shape out of everything in the house to the east (maybe you should leave that for the end).\nThe carpet in the room is dingy and covered in tracked in dirt, and the TV in the corner has been smashed.", 7, 9, None, 4)
    room_list.append(room)

    #create the hole event (room 6)

    room = Room("You try and peak your head out of the hole.\nAll of a sudden, you spot a dangerous looking beast cross the lawn in front of the house!\nTo avoid it's attention, retreat north back into the room!", 1, None, None, None)
    room_list.append(room)

    #create the fridge event (room 7)

    room = Room("As you open the fridge, a putrid smell pours out and assaults your nostrils.\nOpening it further reveals chunks of unidentifiable rotten meat and a few bones strewn about its inner shelves.\nTurning back to the south is the only way.", None, None, 2, None)
    room_list.append(room)

    #create the book event (room 8)

    room = Room("Picking up the journal and blowing the dust off of it, you flip through it's pages.\nInside is detailed the story of someone who seemed to be in a similar situation to yours.\nThey also woke up without any idea what was going on, and subsisted in the house for several days.\nThe final entry describes them hearing activity towards the front of the house as they hunker down with a weapon.\nPut the book down and remain in the library by going east.", None, 3, None, None)
    room_list.append(room)

    #create the bed event (room 9)

    room = Room("", None, None, None, None)
    room_list.append(room)

    # starts you in the living room

    current_room = 0

    done = False

    while not done:

        # print description of room you're in

        print()
        print(room_list[current_room].description)

    #---ask the user what they want to do---

        user_input = input("Which direction? ")

        #if they want to quit

        if user_input.lower() == "q" or user_input.lower() == "quit":
            done = True

        #if they want to go north

        elif user_input.lower() == "n" or user_input.lower() == "north":
            next_room = room_list[current_room].north
            if next_room is None:
                print("You can't go that way!")
            else:
                current_room = next_room

        #if they want to go east

        elif user_input.lower() == "e" or user_input.lower() == "east":
            next_room = room_list[current_room].east
            if next_room is None:
                print("You can't go that way!")
            else:
                current_room = next_room

        #if they want to go south

        elif user_input.lower() == "s" or user_input.lower() == "south":
            next_room = room_list[current_room].south
            if next_room is None:
                print("You can't go that way!")
            else:
                current_room = next_room

        #if they want to go west

        elif user_input.lower() == "w" or user_input.lower() == "west":
            next_room = room_list[current_room].west
            if next_room is None:
                print("You can't go that way!")
            else:
                current_room = next_room

        else:
            print("I don't understand.")

        if current_room == 9:
            print()
            print("As you gently slide into the sheets and place your head on the pillow, even in this strange situation, you slowly drift off to sleep.\nYou awake in a start.\nIn fear and suspicion over how quickly you fell asleep, you look around the room.\nIt's your own bedroom back in your house.\nIt was all just a dream!")
            done = True
main()