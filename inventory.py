
inventory = []
items = {
  "Chest" : {"Description" : "You find a treasure chest.",
             "Status" : "closed",
             "Location": [2, 1], 
             "Action" : ["open","inspect", "done"],
             "Requirement" : ["key", None, None]
            },
  "Key" : {"Description" : "You find a key haning on the wall.",
           "Status" : "lost",
           "Location" : [0, 1],
           "Action" : ["take", "leave"],
           "Requirement" : [None, None]
          }, 
  "Treasure" : {"Description" : "You found some.",
           "Status" : "in chest",
           "Location" : [None, None],
           "Action" : ["take", "leave"],
           "Requirement" : [None, None]
          }
      }
def KeyRandomizer():
  global items
  row_list = []
  for i in range (0, (map.max_row)+1), 1):
    row_list.append(i)
  items["Key"]["Location"] = random.choice(row_list)
  col_list = []
  for j in range(0, int(map.max_col)+1), 1):
    col_list.append(j)
  items["Key"]["Location"][1] = random.choice(col_list)

def CheckInventory():
  if inventory:
    print(f"Inventory: ")
    for item in inventory:
        print(f" - {item}")
  else:
    print("Your inventory is empty.")


def InspectRoom():
  global inventory, items
  find_object = False
  room_inventory = []
  location_description =  map.map[character.row][character.col]
  print(f"You look around the room.")
  for object in items:
      object_row = items[object]["Location"][0]
      object_col = items[object]["Location"][1]
      if object_row == character.row and object_col == character.col:
        print(f"{items[object]['Description']}")
        find_object = True
        room_inventory.append(object)
  if found_object == True:
    for item in room_inventory:
      if item == "Chest":
        ChestActions()
      elif item == "Key":
        KeyActions()
      else:
                  print(f"There are no interactive objects in this room.")
    else:
          print(f"There are no objects in this room.")
      room_inventory = []
      
      
  
