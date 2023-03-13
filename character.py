class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    # Describe this character
    def describe(self):
        print( self.name + " is here!" )
        print( self.description )

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True
    
    def gift(self, gift):
        print(self.name + " doesn't want your gift.")
        return True
    
class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
    
    def set_weakness(self, char_weakness):
        self.weakness = char_weakness
        
    def get_weakness(self):
        return self.weakness
    
    def fight(self, combat_item):
        if combat_item == self.weakness:
            print(f"You fend off {self.name} off with the {combat_item}.")
            return True
        else:
            print(f"{self.name} crushes you, puny adventurer.")
            return False
        
class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.fav_gift = None
    
    def set_fav_gift(self, fav_gift):
        self.fav_gift = fav_gift
        
    def get_fav_gift(self):
        return self.fav_gift
    
    def gift(self, gift):
        if gift == self.fav_gift:
            print(f"{self.name} loves your gift of {gift}.")
        else:
            print(f"{self.name} smiles and gives you back your gift.")
            return False
        
        
        
    
    
