from room import Room
from item import Item
from character import Enemy, Friend
from time import sleep
from instructions import *

#Create the rooms
kitchen = Room("Kitchen", "A dank and dirty place buzzing with flies.")
ballroom = Room("Ballroom", "A large room with ornate golden decorations on each wall.")
dining_hall = Room("Dining Hall", "A vast room with a shiny wooden floor; huge candlesticks guard the entrance.")

#Link the rooms
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

#Create the items
dagger = Item("dagger")
cheese = Item("cheese")

#Create the characters
dave = Enemy("Dave", "a smelly zombie")
dave.set_conversation("Brains!")
dave.set_weakness("cheese")

sally = Friend("Sally", "a friendly looking skeleton")
sally.set_conversation("Hello!")
sally.set_gift(cheese)

#Bag for storing items
gamers_bag = []

#Put the characters in the rooms
ballroom.set_character(dave)
dining_hall.set_character(sally)

#Move between rooms
current_room = kitchen

#Print instructions
by_letter(opening)

#The Game
while True:
    
    sleep(1)
    print("\n")
    current_room.get_room_details()
    sleep(1)
    
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.get_char_details()

    print("\n")
    instruction = input("Input command: ").lower()

    if instruction in ["north", "south", "east", "west"]:
        current_room = current_room.move(instruction)

    elif instruction == "talk":
        sleep(1)
        inhabitant.talk()
        
        if isinstance(inhabitant, Friend):
            inhabitant.give_gift(gamers_bag)
        else:
            pass
        
    elif instruction == "fight":
        combat_item = input("What would you like to fight with? ").lower()
        sleep(1)
        print("...")
        sleep(1)

        outcome = inhabitant.fight(combat_item)
        sleep(1)
        
        if outcome == False:
            print("You are dead! Game Over")
            sleep(1)
            break
    
    elif instruction == "check bag":

        if gamers_bag == []:
            print("Your bag is currently empty.")
        else:
            print(f"Your bag contains: {gamers_bag}")
    
    elif instruction == "quit":
        print("The game will now close...")
        sleep(1)
        break


 




