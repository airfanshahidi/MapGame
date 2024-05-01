import sys  # Import the sys module for system-specific operations (e.g., exiting the program)
import inventory  # Import the inventory module for managing the player's inventory
import character  # Import the character module for managing the player's character
import message  # Import the message module for displaying messages to the player
import map  # Import the map module for managing the game map
from map import map_layout, tiles  # Import the map_layout and tiles from the map module

main_menu = ["explore", "search", "view map", "view inventory"]  # List of options for the main menu
direction_menu = ["north", "south", "east", "west"]  # List of directions for movement

def SetUpGame():
    # Set the starting position of the character
    character.row = 0
    character.col = 0
    map.export_map()  # Export the initial map to a file

def print_location_description():
    # Get the current location from the map layout
    location = map.map_layout[character.row][character.col]
    # Get the description for the current location from the tiles dictionary
    description = tiles.get(location, {}).get("Description", f"Invalid location: {location}")
    print(f"location_description: {location}")
    print(description)

def Movement():
    orientating = True
    while orientating:
        print("   Choose a direction: ")
        # Print the available directions based on the character's current position
        if not character.row == 0:
            print(f"   -{direction_menu[0].capitalize()}")
        if not character.row == map.max_row:
            print(f"   -{direction_menu[1].capitalize()}")
        if not character.col == map.max_col:
            print(f"   -{direction_menu[2].capitalize()}")
        if not character.col == 0:
            print(f"   -{direction_menu[3].capitalize()}")
        orientating = False
        dirchoice = input("   Choice: ").lower()
        # Move the character based on the chosen direction
        if dirchoice == direction_menu[0] and character.row > 0:
            character.row -= 1
        elif dirchoice == direction_menu[1] and character.row < map.max_row:
            character.row += 1
        elif dirchoice == direction_menu[2] and character.col < map.max_col:
            character.col += 1
        elif dirchoice == direction_menu[3] and character.col > 0:
            character.col -= 1
        elif dirchoice == "quit":
            print(f"{message.message['Quit']} ")
            sys.exit()  # Exit the program if the user chooses to quit
        else:
            print(f"{message.message['Error']}")
            orientating = True  # If the input is invalid, ask for direction again
    map.update_map(character.row, character.col)  # Update the map with the character's new position
    print_location_description()  # Print the description of the new location

def MainMenu():
    thinking = True
    while thinking:
        print("   Choose one of the following options: ")
        for options in main_menu:
            print(f"   -{options.capitalize()}")
        mainChoice = input("   Choice: ").lower()
        # Perform different actions based on the chosen main menu option
        if mainChoice == main_menu[0]:
            Movement()
            thinking = False
        elif mainChoice == main_menu[1]:
            inventory.InspectRoom()
            print_location_description()
            thinking = False
        elif mainChoice == main_menu[2]:
            map.update_map(character.row, character.col)
            map.read_map()
            thinking = False
        elif mainChoice == main_menu[3]:
            inventory.ViewInventory()
            thinking = False
        elif mainChoice == "cheat":
            print(inventory.items["Key"]["Location"])  # Cheat code to print the location of the key
        elif mainChoice == "quit":
            print(f"{message.message['Quit']} ")
            sys.exit()  # Exit the program if the user chooses to quit
        else:
            print(f"{message.message['Error']}")

print("Welcome to the Graveyard!\n")
print("Goal is to find and open a treasure chest.")
print("Type Quit at any time to quit the game.\n")
SetUpGame()  # Set up the game
while True:
    # Print the description of the current location
    location_description = map.map_layout[character.row][character.col]
    print(f"location_description: {location_description}")
    for tile_option in map.tiles:
        if tile_option == location_description:
            print(f"{map.tiles.get(tile_option, 'Invalid tile type')['Description']}")
    MainMenu()  # Display the main menu