import sys
import map
import inventory
import character
import message

main_menu = ["explore", "search", "view map", "view inventory"]
# Directions choices for a sub menu
direction_menu = ["north", "south", "east", "west"]

def SetUpGame():
    '''This fuction will call all the the nessesary setup functions.'''
    inventory.HideKey()    
    map.ExportMap()

def Movement():
    '''This function will allow the player to move around the map.'''  
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
            print(f"{message.messages['Quit']} ")
            sys.exit()
        else:
            print(f"{message.messages['Error']}")
            orientating = True


def MainMenu():
    '''When the game is activated these are all the players inital
       actions that are possible. This is the games main menu.'''
    thinking = True
    while thinking:
        print("   Choose one of the following options: ")
        # loop through all main menu options and print to the screen
        for options in main_menu:
            print(f"   -{options.capitalize()}")
        mainChoice = input("   Choice: ").lower()
        if mainChoice == main_menu[0]: # walk
            Movement()
            thinking = False
        elif mainChoice == main_menu[1]: # look
            inventory.InspectRoom()
            thinking = False
        elif mainChoice == main_menu[2]: # view map
            map.ReadMap()
            thinking = False
        elif mainChoice == main_menu[3]: # view inventory
            inventory.ViewInventory()
            thinking = False
        elif mainChoice == "cheat":
            print(inventory.items["Key"]["Location"])
        elif mainChoice == "quit":
            print(f"{message.messages['Quit']} ")
            sys.exit()
        else:
            print(f"{message.messages['Error']}") 

print("Welcome to the Graveyard!\n")
print("Goal is to find and open a treasure chest.")
print("Type Quit at any time to quit the game.\n")
SetUpGame()
while True:
    location_description =  map.map[character.row][character.col]
    for tile_option in map.tiles:
      if tile_option == location_description:
        print(f"{map.tiles[tile_option]['Description']}")
    MainMenu()