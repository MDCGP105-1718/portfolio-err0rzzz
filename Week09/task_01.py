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
            deck.append((random.randint(0,52), (Card(s,n))))
            # deck[Card(s,n)] = random.randint(0,51)      #deck as a dictionary with card as key and place in deck as value

build_deck()

# print (deck[5].number, deck[5].suit, deck[5])
print (len(deck))

for (n,p) in deck:
    print (str(deck[n]) + str(deck[p]))


# for card,v in deck.items():
#     print ("in position number " + str(v) + " is card " +str(card))
