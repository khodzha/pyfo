from enum import IntEnum

class Rank(IntEnum):
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

    @classmethod
    def from_str(cls, s):
        table = {
            '6':  cls.SIX,
            '7':  cls.SEVEN,
            '8':  cls.EIGHT,
            '9':  cls.NINE,
            'T': cls.TEN,
            'J':  cls.JACK,
            'Q':  cls.QUEEN,
            'K':  cls.KING,
            'A':  cls.ACE,
        }

        return table[s]

    def __repr__(self):
        table = {
            Rank.SIX:   '6',
            Rank.SEVEN: '7',
            Rank.EIGHT: '8',
            Rank.NINE:  '9',
            Rank.TEN:   'T',
            Rank.JACK:  'J',
            Rank.QUEEN: 'Q',
            Rank.KING:  'K',
            Rank.ACE:   'A',
        }
        return table[self]


    def __str__(self):
        return self.__repr__()
