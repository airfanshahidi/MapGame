from tabulate import tabulate

update_marker = "X"  # Change the marker for the player's position

tile = ["Enterance", "Mausoleum", "Catacombs", "Secret Passage", 
   "Royal Tomb", "Graveyard Chapel"]

tiles = {
  "Enterance": {"Description": """An eerie graveyard with
weathered tombstones and overgrown vegetation."""},

  "Mausoleum": {"Description": """A dimly lit chamber with
rows of intricately carved sarcophagi."""},

  "Catacombs": {"Description": """A maze of narrow tunnels
lined with ancient burial niches."""},

  "Secret Passage": {"Description": """A hidden passage concealed
by vines, promising untold secrets."""},

  "Royal Tomb": {"Description": """A grand chamber adorned with
carvings, guarding a ruler's resting place."""},

  "Graveyard Chapel": {"Description": """A solemn chapel with
stained-glass windows casting colors on weathered pews."""}
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