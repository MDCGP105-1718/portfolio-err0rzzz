


##################
##set up classes##
##################

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

      # def add_item(self, item_name):
      #     self.items[item_name] = 1

    def test_output(self):
        return ("room name = " + str(self.room_name) + "\n" + "description = " + str(self.description) + "\n" + 'Items = <broken> ' + "\n" + 'Exits = ' + ', '.join(self.exits))

#define player class (possibly not needed)
class Peasant(object):
    def __init__(self, location, status, player_inventory):
        self.location = location;
        self.status = status;
        self.player_inventory = player_inventory;

#define item class
class Item(object):
    def __init__(self, item_name, item_description, carriable):
        self.item_name = item_name;
        self.item_description = item_description;
        self.carriable = bool(carriable);

    def test_item(self):
        return ("I'm a " + str(self.item_name) + ". My description is: " + str(self.item_description) + ". it is " + str(self.carriable) +" to say that I can be picked up.")

###############
## Item list###
###############
#sorted by room for ease

#tavernInventory = ['beer', 'unhelpful ally']
beer = Item("beer", "it's a bit stale, but still does the job", True)
unhelpful_ally = Item("unhelpful ally", "I have absoloutley no idea what possible use he could be...", True)

#squareInventory = ['rabble', 'a disgruntled Knight', 'well']
rabble = Item("rabble", "no king, hero or savior could keep this lot happy", False)
knight = Item("a disgruntled knight", "the frustration of keeping the crowd at bay has clearly taken its toll", False)
well = Item("well", "the cities primary water source, only slightly polouted", False)


#stableInventory = ['hay', 'more hay', 'horse', 'unwell horse', 'stable hand']
hay = Item("hay", "there is a large pile of hay", False)
more_hay = Item("more hay", "there is an even larger pile of hay", False)
horse = Item("horse", "a fairly healthy looking horse", False)
unwell_horse = Item("an unwell horse", "a pale, sickly looking horse", False)
stable_hand = Item("the stable hand", "a young and inexperianced stable boy", False)

#houseInventory = ['desk', 'chest', 'envelope']
desk = Item("desk", "A large wodden desk, it has been searched", False)
chest = Item("Chest", "the chest is empty", False)
envelope = Item("envelope", "a small sealed envelope bearing the wax sealing crest of the King", True)

#alleyInventory = ['old barrel']
old_barrel = Item("old Barrel", "this barrel looks like its been here a while but shows signs that its been recently moved", False)

#gateInventory = ['drunken guard, broken drawbridge']
drunken_guard = Item("Drunken guard", "this guard is an embaressment to his profession", False)
broken_drawbridge = Item("broken drawbridge", "the bridge is broken and stuck in the open position. we might as well not have a moat.", False)

#fieldInventory = ['threatening snake, ambigious mushrooms, ugly statue']
threatening_snake = Item("a threatening snake", "this snake looks like it would be very happy to bite...", False)
ambigious_mushrooms = Item("a small cluster of ambigious mushrooms", "you can't identify these and have no knowlege of mushrooms", True)
ugly_statue = Item("a large ugly statue", "the statue is of a forgotten deity so worn by age its truly unpleasant to look at", False)

############
##Roomlist##
############

#tavern
tavernInventory = []
tavernInventory.append(beer) #['beer', 'unhelpful_ally']
tavernExits = {}
tavern = Room('Tavern', "A dirty, musky tavern", tavernInventory, tavernExits)

#townSquare
squareInventory = ['rabble', 'a disgruntled Knight', 'well']
squareExits = {}
townSquare = Room('The Town Square', "The town square has seen better days, but still does it's job.", squareInventory, squareExits)

#stable
stableInventory = ['hay', 'more hay', 'horse', 'unwell horse', 'stable hand']
stableExits = {}
stable = Room('a stable', "the stable is a tad rundown but still houses two horses", squareInventory, squareExits)

#house
houseInventory = ['desk', 'chest']
houseExits = {}
house = Room('a ransacked house', "this house has been robbed without mercy" , houseInventory, houseExits)

#alley
alleyInventory = ['old barrel']
alleyExits = {}
alley = Room('a dimly lit alleyway', "this alleyway is an L shape and leads between the residential district and the town gate" , alleyInventory, alleyExits)

#gate
gateInventory = [drunken_guard, broken_drawbridge]
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

field.add_exit("north", gate)

# ## tests
# print ("\n")
# print(tavern.test_output())
# print ("\n")
# print(beer.test_item())
# print ("\n")
# print ("\n")


##################################
## set up main game paramaters ###
##################################

isgameover = False



#define starting room
curent_room = tavern

####################
### main game loop##
####################

while isgameover == False:
    print ("you find yourself in a "+ curent_room.room_name +"\n\n\n")

    playercommand = input ()

    if playercommand == "end":
        isgameover = True

    if playercommand == "look":
        print ("you look arround yourself and see " + curent_room.description + "there are exits to the current_room.""\n\n\n")
