from tabulate import tabulate

update_marker = "X"  # Change the marker for the player's position

tile = ["Entrance", "Mausoleum", "Catacombs", "Secret Passage", 
   "Royal Tomb", "Graveyard Chapel"]

tiles = {
    "Enterance": {"Description": "You are at the entrance of the graveyard."},
    "Mausoleum": {"Description": "You are in the mausoleum."},
    "Catacombs": {"Description": "You are in the catacombs."},
    "Secret Passage": {"Description": "You found a secret passage!"},
    "Royal Tomb": {"Description": "You are in the royal tomb."},
    "Graveyard Chapel": {"Description": "You are in the graveyard chapel."}
}

map_layout = [
   ["Enterance", "Mausoleum", "Catacombs", "Secret Passage"],
   ["Masoleum", "Royal Tomb", "Royal Tomb", "Graveyard Chapel"],
   ["Catacombs", "Catacombs", "Graveyard Chapel", "Graveyard Chapel"]
]

max_row = 2
max_col = 3

mapfile = 'map1.txt'

def export_map(updated_map=None):
   if updated_map is None:
      map_to_export = map_layout
   else:
      map_to_export = updated_map
   with open(mapfile, 'w') as file:
      file.write(tabulate(map_to_export, tablefmt='fancy_grid'))

def read_map():
   with open(mapfile, 'r') as file:
      print(file.read())

def update_map(player_row, player_col):
   updated_map = [row[:] for row in map_layout]  # Create a copy of the map_layout
   updated_map[player_row][player_col] = f"{update_marker}"  # Update the player's position
   export_map(updated_map)  # Export the updated map to the file

__all__ = ['map_layout', 'tiles', 'update_map', 'read_map']