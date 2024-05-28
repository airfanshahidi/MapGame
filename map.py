from tabulate import tabulate

class Map:
   def __init__(self):
      # Initialize map properties and layout
      self.update_marker = "X"  # Change the marker for the player's position
      self.tiles = {
         "Entrance": {"Description": "An eerie graveyard with weathered tombstones and overgrown vegetation."},
         "Mausoleum": {"Description": "A dimly lit chamber with rows of intricately carved sarcophagi."},
         "Catacombs": {"Description": "A maze of narrow tunnels lined with ancient burial niches."},
         "Secret Passage": {"Description": "A hidden passage concealed by vines, promising untold secrets."},
         "Royal Tomb": {"Description": "A grand chamber adorned with carvings, guarding a ruler's resting place."},
         "Graveyard Chapel": {"Description": "A solemn chapel with stained-glass windows casting colors on weathered pews."}
      }
      self.map_layout = [
         ["Entrance", "Mausoleum", "Catacombs", "Secret Passage"],
         ["Mausoleum", "Royal Tomb", "Royal Tomb", "Graveyard Chapel"],
         ["Catacombs", "Catacombs", "Graveyard Chapel", "Graveyard Chapel"]
      ]
      self.max_row = 2
      self.max_col = 3
      self.mapfile = 'map1.txt'

   def export_map(self, updated_map=None):
      # Export the map layout to a file
      map_to_export = updated_map if updated_map is not None else self.map_layout
      with open(self.mapfile, 'w') as file:
         file.write(tabulate(map_to_export, tablefmt='fancy_grid'))

   def read_map(self):
      # Read and display the map layout from a file
      with open(self.mapfile, 'r') as file:
         print(file.read())

   def update_map(self, player_row, player_col):
      # Update the map layout with the player's position
      updated_map = [row[:] for row in self.map_layout]
      updated_map[player_row][player_col] = f"{self.update_marker}"
      self.export_map(updated_map)

class Tile:
   def __init__(self, description):
      # Initialize a tile with a description
      self.description = description

# Example of creating a Map object
game_map = Map()
game_map.export_map()