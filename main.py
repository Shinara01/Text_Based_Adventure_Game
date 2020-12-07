from room import Room
from item import Item

#Create the rooms
kitchen = Room("Kitchen", "A dank and dirty place buzzing with flies.")
ballroom = Room("Ballroom", "A large room with ornate golden decorations on each wall.")
dining_hall = Room("Dining Hall", "A vast room with a shiny wooden floor; huge candlesticks guard the entrance.")

kitchen.link_room(dining_hall, "South")
dining_hall.link_room(kitchen, "North")
dining_hall.link_room(ballroom, "West")
ballroom.link_room(dining_hall, "East")

#Create the items
dagger = Item("Dagger", "A rusty looking dagger with a faded black hilt") 

#Move between rooms
current_room = kitchen

while True:
    
    print("\n")
    current_room.get_room_details()
    instruction = input("Where would you like to go? ").capitalize()
    current_room = current_room.move(instruction)
