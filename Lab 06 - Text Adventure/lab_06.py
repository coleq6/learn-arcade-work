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

    room_list = []

    # create the living room (room0)

    room = Room("You are in the living room", None, 1, None, None)
    room_list.append(room)

    # create the entry room (room1)

    room = Room("You are in the entry room", 4, 2, None, 0)
    room_list.append(room)

    #create the kitchen/dining room (room2)

    room = Room("You are in the kitchen/dining room", None, None, None, 1)
    room_list.append(room)

    #create the library (room3)

    room = Room("You are in the library", None, 4, None, None)
    room_list.append(room)

    #create the hall (room4)

    room = Room("You are in the hall", None, 5, 1, 3)
    room_list.append(room)

    #create the bedroom (room5)

    room = Room("You are in the bedroom", 6, None, None, 4)
    room_list.append(room)

    # create the bathroom (room6)

    room = Room("You are in the bathroom", None, None, 5, None)
    room_list.append(room)

    # starts you in the living room

    current_room = 0

    #print description of room you're in

    done = False

    while not done:
        print()
        print(room_list[current_room].description)

    #---ask the user what they want to do---

        user_input = input("What direction? ")

        #if they want to go north

        if user_input.upper == "n" or "north":
            next_room = room_list[current_room].north
            if next_room is None:
                print("You can't go that way")
            else:
                current_room = next_room
                return current_room

        #if they want to go east

        elif user_input.upper == "e" or "east":
            next_room = room_list[current_room].east
            if next_room is None:
                print("You can't go that way")
            else:
                current_room = next_room
                return current_room

        #if they want to go south

        elif user_input.upper == "s" or "south":
            next_room = room_list[current_room].south
            if next_room is None:
                print("You can't go that way")
            else:
                current_room = next_room
                return current_room

        #if they want to go west

        elif user_input.upper == "w" or "west":
            next_room = room_list[current_room].west
            if next_room is None:
                print("You can't go that way")
            else:
                current_room = next_room
                return current_room

        else:
            print("I don't understand")


main()