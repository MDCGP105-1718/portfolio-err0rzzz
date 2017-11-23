


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
        item_return =[]
        for i in self.items:
            item_return.append(i.item_name)
        return ("room name = " + str(self.room_name) + "\n" + "description = " + str(self.description) + "\n" + 'Items = ' + str(item_return) + "\n" + 'Exits = ' + ', '.join(self.exits))

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

tavernInventory = [beer, unhelpful_ally]
# tavernInventory = []
# tavernInventory.append(beer) #['beer', 'unhelpful_ally']
tavernExits = {}
tavern = Room('Tavern', "A dirty, musky tavern", tavernInventory, tavernExits)

#townSquare
squareInventory = [rabble, knight, well]
squareExits = {}
townSquare = Room('The Town Square', "The town square has seen better days, but still does it's job.", squareInventory, squareExits)

#stable
stableInventory = [hay, more_hay, horse, unwell_horse, stable_hand]
stableExits = {}
stable = Room('a stable', "the stable is a tad rundown but still houses two horses", stableInventory, stableExits)

#house
houseInventory = [desk, chest]
houseExits = {}
house = Room('a ransacked house', "this house has been robbed without mercy" , houseInventory, houseExits)

#alley
alleyInventory = [old_barrel]
alleyExits = {}
alley = Room('a dimly lit alleyway', "this alleyway is an L shape and leads between the residential district and the town gate" , alleyInventory, alleyExits)

#gate
gateInventory = [drunken_guard, broken_drawbridge]
gateExits = {}
gate = Room('the cities main gateway', "this gate is the closest thing to a 'last line of defence' that the city has." , gateInventory, gateExits)

fieldInventory = [threatening_snake, ambigious_mushrooms, ugly_statue]
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

#################
## class tests ##
#################
# can be used to test any Room or Item
print ("\n")
print(stable.test_output())
print ("\n")
print(unhelpful_ally.test_item())
print ("\n")
print ("\n")


##################################
## set up main game paramaters ###
##################################

isgameover = False



#define starting room
current_room = tavern
command_list = ['look','go north','go south','go west','go east']

####################
### main game loop##
####################

while isgameover == False: # sets game loop condition


## sets up variables to be used in current room
    viable_exits = []
    for direction in current_room.exits:
        viable_exits.append(direction)

    current_room_items = []
    current_room_items_names = []
    for item in current_room.items:
        current_room_items.append(item)

    print ("\nyou find yourself in a "+ current_room.room_name +"\n")

    playercommand = input ()
    playercommand = playercommand.lower()

##basic quit commands

    if playercommand == "end":
        isgameover = True
    if playercommand == "quit":
        isgameover = True
    if playercommand == "exit":
        isgameover = True

    if playercommand == "look":
        print ("\nyou look arround yourself and see " + current_room.description + " there are exits to the " + str(current_room.room_name) + " on the " + str(viable_exits))
        print ("the things of note that you can see are " + str(current_room_items))

    if playercommand not in command_list:
        print ('the peasant does not know that command, the commands he knows are: ' + str(command_list))

##############
## movement ##
##############
#checks if the requested direction is a viable direction, if so takes the key from the exits dictionary in the current room at sets it as the new current_room
#then it resets the viable exits as empty for the new room.

    if playercommand == 'go south':
        if 'south' in viable_exits:
            current_room = current_room.exits['south']
            viable_exits = []
        else:
            print ("you can't go that way.")

    if playercommand == 'go west':
        if 'west' in viable_exits:
            current_room = current_room.exits['west']
            viable_exits = []
        else:
            print ("you can't go that way.")

    if playercommand == 'go north':
        if 'north' in viable_exits:
            current_room = current_room.exits['north']
            viable_exits = []
        else:
            print ("you can't go that way.")

    if playercommand == 'go east':
        if 'east' in viable_exits:
            current_room = current_room.exits['east']
            viable_exits = []
        else:
            print ("you can't go that way.")
