class item:
    def __init__(self,item_name):
        self.name = item_name
        self.description = None
        self.location = None
        
    def set_desc(self, item_desc):
        self.description = item_desc
        
    def get_desc(self):
        return self.description
    
    def describe(self):
        print("You see a " + self.name)
        print(self.description)
        
    def set_name(self, item_name):
        self.name = item_name
        
    def get_name(self):
        return self.name
    
    
