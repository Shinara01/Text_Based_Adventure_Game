class Item(object):

    def __init__ (self, item_name, item_description):
        self.name = item_name
        self.description = item_description
        self.value = None
        
    def set_name(self, item_name):
        self.name = item_name
    
    def get_name(self):
        return self.name
    
    def print_name(self):
        print(self.name)

    def set_description(self, item_description):
        self.description = item_description
    
    def get_description(self):
        return self.description
    
    def print_description(self):
        print(self.description)
    
    def set_value(self, item_value):
        self.value = item_value
    
    def get_value(self):
        return self.value
    
    def print_value(self):
        print(f"The dagger is worth {self.value} gold coin(s).")
        
    

    