from random import shuffle
from itertools import product

from lib.rank import Rank
from lib.suit import Suit
from lib.card import Card

HAND_SIZE = 6

class Deck:
    @staticmethod
    def shuffle():
        a = product(list(Suit), list(Rank))
        deck = list(map(lambda c: Card(c[0], c[1]), a))
        shuffle(deck)
        return deck
