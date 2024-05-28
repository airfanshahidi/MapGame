"""
Graveyard Adventure Game by Airfan Shahidi
------------------------------------------

Welcome to the Graveyard Adventure Game!

In this text based adventure game, you will explore a haunted graveyard and uncover its secrets.

Yours is the mission to find the treasure hidden within the graveyard.

As you explore the graveyard, you will encounter various obstacles and challenges.

To play the game, you will need to use the commands provided to navigate through the graveyard.

Good luck and have fun!

"""
from character import Character
from inventory import Inventory
from map import Map
import sys

class Game:
    def __init__(self):
         # Initialize game menu options and objects
         self.main_menu = ["explore", "search", "view map", "view inventory"]
         self.direction_menu = ["north", "south", "east", "west"]
         self.character = Character()
         self.inventory = Inventory()
         self.game_map = Map()

    def SetUpGame(self):
         # Set up initial game state
         self.character.row = 0
         self.character.col = 0
         self.game_map.export_map()

    def print_location_description(self):
         # Print current location description
         location = self.game_map.map_layout[self.character.row][self.character.col]
         description = self.game_map.tiles.get(location, {}).get("Description", f"Invalid location: {location}")
         print(f"location_description: {location}")
         print(description)

    def Movement(self):
         # Handle player movement
         orientating = True
         while orientating:
            print("   Choose a direction: ")
            # Display available directions
            if not self.character.row == 0:
                print(f"   -{self.direction_menu[0].capitalize()}")
            if not self.character.row == self.game_map.max_row:
                print(f"   -{self.direction_menu[1].capitalize()}")
            if not self.character.col == self.game_map.max_col:
                print(f"   -{self.direction_menu[2].capitalize()}")
            if not self.character.col == 0:
                print(f"   -{self.direction_menu[3].capitalize()}")
            orientating = False
            dirchoice = input("   Choice: ").lower()
            # Update character position based on choice
            if dirchoice == self.direction_menu[0] and self.character.row > 0:
                self.character.row -= 1
            elif dirchoice == self.direction_menu[1] and self.character.row < self.game_map.max_row:
                self.character.row += 1
            elif dirchoice == self.direction_menu[2] and self.character.col < self.game_map.max_col:
                self.character.col += 1
            elif dirchoice == self.direction_menu[3] and self.character.col > 0:
                self.character.col -= 1
            elif dirchoice == "quit":
                print("Quitting the game...")
                sys.exit()
            else:
                print("Invalid choice. Please try again.")
                orientating = True
         self.game_map.update_map(self.character.row, self.character.col)

    def MainMenu(self):
         # Display main menu and handle choices
         thinking = True
         while thinking:
            print("   Choose one of the following options: ")
            for option in self.main_menu:
                print(f"   -{option}")
            mainChoice = input("   Choice: ")
            if mainChoice.lower() == "quit":
                thinking = False
                print("Goodbye!")
            elif mainChoice.lower() == self.main_menu[0].lower():
                self.Movement()
                thinking = False
            elif mainChoice.lower() == self.main_menu[1].lower():
                self.inventory.InspectRoom(self.character.row, self.character.col)
                self.print_location_description()
                thinking = False
            elif mainChoice.lower() == self.main_menu[2].lower():
                self.game_map.read_map()
                self.print_location_description()
                thinking = False
            elif mainChoice.lower() == self.main_menu[3].lower():
                self.inventory.view_inventory()
                thinking = False
            else:
                print("Invalid choice. Please try again.")

# Start the game
print("Welcome to the Graveyard!\n")
print("Goal is to find and open a treasure chest.")
print("Type Quit at any time to quit the game.\n")

game = Game()
game.SetUpGame()
while True:
    # Game loop
    location_description = game.game_map.map_layout[game.character.row][game.character.col]
    print(f"location_description: {location_description}")
    for tile_option in game.game_map.tiles:
         if tile_option == location_description:
            print(f"{game.game_map.tiles.get(tile_option, 'Invalid tile type')['Description']}")
    game.MainMenu()