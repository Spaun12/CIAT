#Zork type game

# A simple text-based adventure game just because

#!!! Need to figure out how to add random events 
# like, trap, monster, tool, puzzle positive or negative etc. 
# Also need to have random outcome based on choice options given to the player.

# Define the different rooms in the game
rooms = {
    "outside": {
        "description": "You are outside of a large, imposing castle. There is a heavy iron gate to the east, and a forest to the west.",
        "exits": {"east": "gate", "west": "forest"}
    },
    "gate": {
        "description": "You are at the gate of the castle. There is a door to the north, and you can see the outside to the south.",
        "exits": {"north": "door", "south": "outside"}
    },
    "door": {
        "description": "You are at the door of the castle. The door is locked. There is a keyhole.",
        "exits": {"south": "gate"}
    },
    "forest": {
        "description": "You are in a dense forest. There are trees all around you, and you can hear the sound of a stream nearby.",
        "exits": {"east": "outside"}
    }
}

# Define the initial state of the game
current_room = "outside"

while True:
    # Print the description of the current room
    print(rooms[current_room]["description"])
    print("Exits: ", end="")
    # Print the exits from the current room
    for exit in rooms[current_room]["exits"]:
        print(exit, end=", ")
    print()
    # Get the player's next move
    move = input("Where do you want to go? ")
    # Check if the move is valid
    if move in rooms[current_room]["exits"]:
        current_room = rooms[current_room]["exits"][move]
    else:
        print("You can't go that way.")
