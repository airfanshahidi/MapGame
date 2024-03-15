map = [
      ["Entrance", "Mausoleum", "Catacombs", "Secret Passage]"],
      ["Mausoleum", "Royal Tomb", "Graveyard Chapel", "Catacombs"],
      ["Graveyard Chapel", "Graveyard Chapel", "Graveyard Chapel", "Catacombs"],
      ["Catacombs", "Catacombs", "Catacombs", "End"]
]

current_location = [0, 0]

def main_menu():
  print("Welcome To The Tombrunner Adventure")
  print("-----------------------------------")
  print("Please choose an action.")
  print("1. Run")
  print("2. Quit")

  choice = input("Please Type The Number:   ")
  if choice not in ["1", "2"]:
    print("Wrong action, Please Choose a Correct Action..")
    main_menu()

  if choice == "1":
    run()
  if choice == "2":
    quit()

def run():
  print("You are currently in the", 
map[current_location[0]][current_location[1]])

  print("---------------------------------")
  print("Please choose a direction:")
  print("1. North")
  print("2. South")
  print("3. East")
  print("4. West")

  choice = input("Input Number:   ")

  if choice not in ["1", "2", "3", "4"]:
    print("Option Does Not Exist... Try Again")
    run()


  if choice == "1":
    move_north()
  elif choice == "2":
    move_south()
  elif choice == "3":
    move_east()
  elif choice == "4":
    move_west()

def move_north():
  

