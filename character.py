class Character():

    #Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
        self.weakness = None

    #Describe this character
    def get_char_details(self):
        print(f"{self.name} is here! {self.name} is a {self.description}")

    #Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    #Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    #Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True
    
class Enemy(Character):

    #Create an enemy
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
        self.enemy_bag = []
        
    def set_weakness(self, enemy_weakness):
        self.weakness = enemy_weakness
    
    def get_weakness(self):
        return self.weakness
    
    def print_weakness(self):
        print(self.weakness)
        
    def fight(self, combat_item):
        if combat_item == self.weakness:
            print(f"You fend off {self.name} with {combat_item}")
            return True
        else:
            print(f"{self.name} crushes you, puny adventurer!")
            return False

class Friend(Character):

    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.gift = None
    
    def set_gift(self, gift):
        self.gift = gift
    
    # def get_gift(self):
    #     return self.gift
    
    def give_gift(self, gamers_bag):
        
        if self.gift is not None:
            offer = input("Would you like a gift? ").lower()

            if offer == "yes":
                print(f"You have accepted {self.name}'s gift. It is {self.gift}.")
                gamers_bag.append(self.gift)
                self.gift = None
                print(f"Your bag now contains: {gamers_bag}")
            else:
                print(f"Ok. Maybe another time then...")

        else:
            print("Sorry I don't have any gifts for you at the moment.")

