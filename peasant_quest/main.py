
##set up the classes required for the project
#define room class
class Room(object):
    def __init__(self, room_name, description, items, exits):
        self.room_name = room_name;
        self.description = description;
        self.items = items;
        self.exits = exits;

    def add_exit(self, exit_key, exit_room):
        self.exits[exit_key] = exit_room

    def test_output(self):
        return ("room name = " + str(self.room_name) + "\n" + "description = " + str(self.description) + "\n" + 'Items = ' + ', '.join(self.items) + "\n" + 'Exits = ' + ', '.join(self.exits))

#define player class (possibly not needed)
class peasant(object):
    def __init__(self, location, status, player_inventory):
        self.location = location;
        self.status = status;
        self.player_inventory = player_inventory;

#define item class
class item(object):
    def __init__(self, item_name, item_description, current_location):
        self.item_name = item_name;
        self.item_description = item_description;
        self.current_location = current_location


#townsquare

##Roomlist
#tavern
tavernInventory = ['beer', 'unhelpful ally']
tavernExits = {}
tavern = Room('Tavern', "A dirty, musky tavern", tavernInventory, tavernExits)

squareInventory = ['rabble', 'a disgruntled Knight', 'well']
squareExits = {}
townSquare = Room('The Town Square', "The town square has seen better days, but still does it's job.", squareInventory, squareExits)

#stable
stableInventory = ['hay', 'more hay', 'horse', 'unwell horse', 'stable hand']
stableExits = {}
stable = Room('a stable', "the stable is a tad rundown but still houses two horses", squareInventory, squareExits)

#ransacked house
houseInventory = ['hay', 'more hay', 'horse', 'unwell horse', 'stable hand']
houseExits = {}
house = Room('a ransacked house', "this house has been robbed without mercy" , houseInventory, houseExits)

#alley
alleyInventory = ['old barrel']
alleyExits = {}
alley = Room('a dimly lit alleyway', "this alleyway is an L shape and leads between the residential district and the town gate" , alleyInventory, alleyExits)

#gate
gateInventory = ['drunken guard, broken drawbridge']
gateExits = {}
gate = Room('the cities main gateway', "this gate is the closest thing to a 'last line of defence' that the city has." , gateInventory, gateExits)

fieldInventory = ['threatening snake, ambigious mushrooms, ugly statue']
fieldExits = {}
field = Room('a large field', "this field surrounds the city" , fieldInventory, fieldExits)


#define all exits for all rooms, this has to be done after building the rooms so
tavern.add_exit("south", townSquare)

townSquare.add_exit("north", tavern)
townSquare.add_exit("west", house)
townSquare.add_exit("east", stable)
townSquare.add_exit("south", gate)

stable.add_exit("west", townSquare)

house.add_exit("east", townSquare)
house.add_exit("south", alley)

alley.add_exit("north", house)
alley.add_exit("east", gate)

gate.add_exit("north", townSquare)
gate.add_exit("west", house)
gate.add_exit("south", field)

#Itemlist
##manually populate with each item from each room#

print(gate.test_output())













# ## main game loop##
# current_room = tavern
#
#
# print ("you find yourself in a " + tavern(self.room_name))
