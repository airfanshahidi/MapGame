import sys
import inventory
import character
import message
import map
from map import map_layout, tiles

main_menu = ["explore", "search", "view map", "view inventory"]
direction_menu = ["north", "south", "east", "west"]

def SetUpGame():
    character.row = 0
    character.col = 0
    map.export_map()

def Movement():
    global direction_menu
    orientating = True
    while orientating:
        print("   Choose a direction: ")
        if not character.row==0:
            print(f"   -{direction_menu[0].capitalize()}")
        if not character.row==map.max_row:
            print(f"   -{direction_menu[1].capitalize()}")
        if not character.col==map.max_col:
            print(f"   -{direction_menu[2].capitalize()}")
        if not character.col==0:
            print(f"   -{direction_menu[3].capitalize()}")
        orientating = False
        dirchoice = input("   Choice: ").lower()
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
            sys.exit()
        else:
            print(f"{message.message['Error']}")
            orientating = True


def MainMenu():
    thinking = True
    while thinking:
        print("   Choose one of the following options: ")
        for options in main_menu:
            print(f"   -{options.capitalize()}")
        mainChoice = input("   Choice: ").lower()
        if mainChoice == main_menu[0]:
            Movement()
            thinking = False
        elif mainChoice == main_menu[1]:
            inventory.InspectRoom()
            thinking = False
        elif mainChoice == main_menu[2]:
            map.update_map(character.row, character.col)
            map.read_map()
            thinking = False
        elif mainChoice == main_menu[3]:
            inventory.ViewInventory()
            thinking = False
        elif mainChoice == "cheat":
            print(inventory.items["Key"]["Location"])
        elif mainChoice == "quit":
            print(f"{message.message['Quit']} ")
            sys.exit()
        else:
            print(f"{message.message['Error']}")

print("Welcome to the Graveyard!\n")
print("Goal is to find and open a treasure chest.")
print("Type Quit at any time to quit the game.\n")
SetUpGame()
while True:
    location_description =  map.map_layout[character.row][character.col]
    print(f"location_description: {location_description}")
    for tile_option in map.tiles:
        if tile_option == location_description:
            print(f"{map.tiles.get(tile_option, 'Invalid tile type')['Description']}")
    MainMenu()