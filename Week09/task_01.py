## define parent class

import random


class Card(object):
    suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10','Jack', 'Queen', 'King', 'Ace']

    def __init__ (self,number, suit):
        self.number = number
        self.suit = suit
        self.name = str()

    def __str__(self):
        return Card.values[self.number] + ' of ' + Card.suits[self.suit]


deck = []     #deck as a list
# deck = {}       #deck as a dictionary with card as key and place in deck as value


##build deck with loop
def build_deck():
    for n in range(4):
        for s in range(13):
            # deck.append((Card(s,n), random.randint(0,51)))                #deck as a list
            randint = randomint()
            deck.append((random.randint(0,10000), (Card(s,n))))
            # deck[Card(s,n)] = random.randint(0,51)      #deck as a dictionary with card as key and place in deck as value

build_deck()
deck.sort()

# print (deck[5].number, deck[5].suit, deck[5])
print (len(deck))

for (p,c) in deck:
    print (str(p) + " is position for "+ str(c))


# for card,v in deck.items():
#     print ("in position number " + str(v) + " is card " +str(card))
