from instructions import by_letter

class Room(object):

    def __init__ (self, room_name, room_description):
        self.name = room_name
        self.description = room_description
        self.linked_rooms = {}
        self.character = None
        
    def set_name(self, room_name):
        self.name = room_name
    
    def get_name(self):
        return self.name
    
    def print_name(self):
        by_letter(f"{self.name}\n")
    
    def set_description(self, room_description):
        self.description = room_description

    def get_description(self):
        return self.description
    
    def print_description(self):
        by_letter(f"{self.description}\n")

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
    
    def print_linked_rooms(self):
        by_letter(f"{self.linked_rooms.items()}\n")
    
    def get_room_details(self):
        
        self.print_name()
        by_letter("----------------\n")
        self.print_description()

        for key in self.linked_rooms:
            room = self.linked_rooms[key]
            print(f"The {room.get_name()} is to the {key}")
    
    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way!")
            return self
    
    def set_character(self, character):
        self.character = character
    
    def get_character(self):
        return self.character





    

        

