from room import Room
from character import Enemy, Friend
from rpginfo import RPGInfo
from item import item

castle = RPGInfo("The Hero's Castle")
castle.welcome()
RPGInfo.info()
RPGInfo.author = "Sri"

kitchen = Room("Kitchen")
ballroom = Room("Ballroom")
dining_hall = Room("Dining Hall")

kitchen.set_desc("A wide and cluttered room with rats scurrying")
kitchen.link_room(dining_hall, "South")

ballroom.set_desc("A spacious elegant room but covered in dust")
ballroom.link_room(dining_hall, "East")

dining_hall.set_desc("A cold large room with rotting drapes lining the walls")
dining_hall.link_room(kitchen, "North")
dining_hall.link_room(ballroom, "West")

dining_hall.get_details()
kitchen.get_details()
ballroom.get_details()

dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Aaarrggh")
dave.set_weakness("Blade")
dining_hall.set_char(dave)

eric = Friend("Eric", "A chipper skeleton")
eric.set_conversation("Howdy!")
eric.set_fav_gift("cheese")
ballroom.set_char(eric)

blade = item("Blade")
blade.set_desc("A rusty kitchen knife but it will do.")
kitchen.set_item(blade)

current_room = kitchen
survive = True
backpack = []
viewbackpack = []
print("There are " + str(Room.number_of_rooms) + " to explore.")

while survive == True:
  print("\n")
  current_room.get_details()
  inhab = current_room.get_char()
  equip = current_room.get_item()
  if inhab is not None:
    inhab.describe()
  if equip is not None:
    equip.describe()
  command = input(">")
  if command in ["North", "East", "South", "West"]:
    current_room = current_room.move(command)
  elif command == "talk":
    if inhab is None:
      print("There's no-one there..")
    else:
      inhab.talk()
  elif command == "fight":
    if inhab is None:
      print("There's no-one there..")
    else:
      for item in viewbackpack:
        print(item)
      weapon = input("What are you fighting with?")
      if weapon in viewbackpack:
        survive = inhab.fight(weapon)
        if survive == False:
          print("You lose.")
          RPGInfo.credits()
      else:
        print("You don't have that...")
  elif command == "gift":
    if inhab is None:
      print("There's no-one there..")
    else:
      present = input("What are you gifting?")
      inhab.gift(present)
  elif command == "equip":
    if equip is None:
      print("There's no items here...")
    else:
      backpack.append(current_room.item)
      viewbackpack.append(current_room.item.get_name())
      current_room.set_item(None)