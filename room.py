class Room:
    
    number_of_rooms = 0
    
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None
        
        Room.number_of_rooms += 1
        
    def set_desc(self, room_desc):
        self.description = room_desc
        
    def get_desc(self):
        return self.description
    
    def describe(self):
        print(self.description)
        
    def set_name(self, room_name):
        self.name = room_name
        
    def get_name(self):
        return self.name
    
    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
        #print( self.name + " linked rooms :" + repr(self.linked_rooms) )
    
    def get_details(self):
        print(self.name + ": " + self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("The " + room.get_name() + " is " + direction + ".")
            
    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("It's just a wall...")
            return self
        
    def set_char(self, char):
        self.character = char
        
    def get_char(self):
        return self.character
    
    def set_item(self, item):
        self.item = item
        
    def get_item(self):
        return self.item
