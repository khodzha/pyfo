from lib.rank import Rank
from lib.suit import Suit

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return "%s%s" % (str(self.rank)[0], str(self.suit)[0], )

    def __eq__(self, other):
        return self.suit == other.suit and self.rank == other.rank

    def value(self, trump_suit):
        if trump_suit == self.suit:
            return self.rank * 100
        else:
            return self.rank

    @classmethod
    def from_str(cls, str):
        rank = Rank.from_str(str[:-1])
        suit = Suit.from_str(str[-1])
        return cls(suit, rank)

    def greater(self, other, trump_suit):
        if other.suit == self.suit:
            return self.rank > other.rank
        elif self.suit == trump_suit or other.suit == trump_suit:
            return self.suit == trump_suit
        else:
            return False
