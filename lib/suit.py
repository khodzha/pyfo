from enum import Enum

class Suit(Enum):
    HEARTS = 1
    DIAMONDS = 2
    CLUBS = 3
    SPADES = 4

    @classmethod
    def from_str(cls, s):
        table = {
            'H': cls.HEARTS,
            'D': cls.DIAMONDS,
            'C': cls.CLUBS,
            'S': cls.SPADES,
        }
        return table[s.upper()]

    def __repr__(self):
        table = {
            Suit.HEARTS: 'H',
            Suit.DIAMONDS: 'D',
            Suit.CLUBS: 'C',
            Suit.SPADES: 'S'
        }
        return table[self]


    def __str__(self):
        return self.__repr__()
