# Define the map of the tomb
map = [
            ["Entrance", "Mausoleum", "Catacombs", "Secret Passage"],
            ["Mausoleum", "Royal Tomb", "Graveyard Chapel", "Catacombs"],
            ["Graveyard Chapel", "Graveyard Chapel", "Graveyard Chapel", "Catacombs"],
            ["Catacombs", "Catacombs", "Catacombs", "End"]
]
# Initialize the player's current location
current_location = [0, 0]
# Define the descriptions of each area in the tomb
area_descriptions = {
    "Entrance": "\nPlayer stands at the entrance of the graveyard, surrounded by crumbling tombstones and a mist. The path ahead is swollen by darkness, but your journey to steal the King’s body begins here.",
    "Mausoleum": "\nYou enter a dusty Mausoleum, its walls are lined up with overgrown plants. The air is heavy with the smell of decay. But beware, the dead may not rest here.",
    "Royal Tomb": "\nYou finally stand before the intimidating entrance to the royal tomb, its massive stone doors with carvings of the kings and warriors. As you step inside, the air grows thick with the weight of history, and you sense that you are treading on sacred ground.",
    "Graveyard Chapel": "\nIn the crumbling walls of the chapel, stained glass windows show scenes of long-forgotten saints. The faint sound of whispering echoes through the empty hall, as if the spirits themselves are watching your every move.",
    "Catacombs": "\nIn the catacombs, where the bones of the forgotten lie freely. The flickering torch lights cast long shadows across the ancient walls, and every step echoes ominously in the darkness.",
    "Secret Passage": "\nYou find yourself at a secret passage concealed behind a crumbling wall, its entrance obscured by centuries of neglect. As you explore deeper into the darkness, the passage reveals its secrets: forgotten treasures, ancient relics, and perhaps even a lockpick to unlocking the King’s tomb.",
    "End": "\nYou have reached the end of the tomb."
}
# Define the main menu function
def main_menu():
    # Print the main menu options
    print("\nWelcome To The Tombrunner Adventure")
    print("\n-----------------------------------")
    print("\nPlease choose an action.")
    print("\n1. Run")
    print("\n2. Quit")
    # Get the user's choice
    choice = input("\nPlease Type The Number:   ")
    # Validate the user's choice
    if choice not in ["1", "2"]:
        print("\nWrong action, Please Choose a Correct Action..")
        main_menu()
    # Start the game if the user chooses to run
    if choice == "1":
        run()
    # Quit the game if the user chooses to quit
    if choice == "2":
        quit()
# Define the run function
def run():
    # Print the player's current location
    print("\nYou are currently in the", map[current_location[0]][current_location[1]])
    # Print the description of the current location
    if map[current_location[0]][current_location[1]] in area_descriptions:
        print("\n" + area_descriptions[map[current_location[0]][current_location[1]]])
    # Print the available directions
    print("\n---------------------------------")
    print("\nPlease choose a direction:")
    print("\n1. North")
    print("\n2. South")
    print("\n3. East")
    print("\n4. West")
    # Get the user's choice
    choice = input("\nInput Number:   ")
    # Validate the user's choice
    if choice not in ["1", "2", "3", "4"]:
        print("\nOption Does Not Exist... Try Again")
        run()
    # Move the player in the chosen direction
    if choice == "1":
        move_north()
    elif choice == "2":
        move_south()
    elif choice == "3":
        move_east()
    elif choice == "4":
        move_west()
# Define the move_north function
def move_north():
    # Check if the player can move north
    if current_location[0] == 0:
        print("\nYou cannot move north from your current location.")
        run()
    # Move the player north
    else:
        current_location[0] -= 1
        run()
# Define the move_east function
def move_east():
    # Check if the player can move east
    if current_location[1] == len(map[0]) - 1:
        print("\nYou cannot move east from your current location.")
        run()
    # Move the player east
    else:
        current_location[1] += 1
        run()
# Define the move_west function
def move_west():
    # Check if the player can move west
    if current_location[1] == 0:
        print("\nYou cannot move west from your current location.")
        run()
    # Move the player west
    else:
        current_location[1] -= 1
        run()
# Define the move_south function
def move_south():
    # Check if the player can move south
    if current_location[0] == len(map) - 1:
        print("\nYou cannot move south from your current location")
        run()
    # Move the player south
    else:
        current_location[0] += 1
        run()
# The main function calls the main_menu function to start the game.
main_menu()