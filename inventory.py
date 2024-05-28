import random
from map import Map

class Inventory:
    def __init__(self):
        # Initialize inventory and item data
        self.inventory = []
        self.items = {
            "Chest": {
                "Description": "You find a treasure chest.",
                "Status": "closed",
                "Location": [2, 1],
                "Action": ["open", "inspect", "done"],
                "Requirement": ["Key", None, None]
            },
            "Key": {
                "Description": "You find a key hanging on the wall.",
                "Status": "lost",
                "Location": [0, 1],
                "Action": ["take", "leave"],
                "Requirement": [None, None]
            },
            "Treasure": {
                "Description": "You found some.",
                "Status": "in chest",
                "Location": [None, None],
                "Action": ["take", "leave"],
                "Requirement": [None, None]
            }
        }

    def InspectRoom(self, character_row, character_col):
        # Check if any items are in the current room and interact with them
        for item_name, item_data in self.items.items():
            if item_data["Location"] == [character_row, character_col]:
                print(item_data["Description"])
                self.InteractWithItem(item_name)

    def InteractWithItem(self, item_name):
        # Handle interactions with a specific item
        item_data = self.items[item_name]
        action_taken = False

        while not action_taken:
            print(f"Available actions for {item_name}:")
            for action in item_data["Action"]:
                if item_data["Requirement"][item_data["Action"].index(action)] is None or item_data["Requirement"][item_data["Action"].index(action)] in self.inventory:
                    print(f"- {action}")

            action_choice = input("What do you want to do? ").lower()

            if action_choice in item_data["Action"]:
                # Handle specific actions based on user choice
                if action_choice == "take":
                    self.inventory.append(item_name)
                    item_data["Status"] = "in inventory"
                    item_data["Location"] = [None, None]
                    print(f"You have taken the {item_name}.")
                elif action_choice == "leave":
                    print(f"You have left the {item_name} in the room.")
                elif action_choice == "open":
                    required_item = item_data["Requirement"][item_data["Action"].index("open")]
                    if required_item in self.inventory:
                        print(f"You have opened the {item_name} using the {required_item}.")
                        item_data["Status"] = "open"
                    else:
                        print(f"You need a {required_item} to open the {item_name}.")
                elif action_choice == "inspect":
                    print(item_data["Description"])
                elif action_choice == "done":
                    print("You have finished interacting with the item.")

                action_taken = True
            else:
                print("Invalid action. Please choose a valid action.")

    def hide_key(self):
        # Randomize the location of the key on the map
        row_list = list(range(0, (int(Map().max_row) + 1)))
        self.items["Key"]["Location"][0] = random.choice(row_list)
        col_list = list(range(0, (int(Map().max_col) + 1)))
        self.items["Key"]["Location"][1] = random.choice(col_list)

    def view_inventory(self):
        # Display the player's inventory
        if self.inventory:
            print("Inventory: ")
            for item in self.inventory:
                print(f" - {item}")
        else:
            print("Your inventory is empty.")

# Example of creating an Inventory object
player_inventory = Inventory()
player_inventory.hide_key()