import pytest
from lib.ai_player import AIPlayer
from lib.game import Game
from lib.card import Card
from lib.suit import Suit
from lib.rank import Rank

class TestAIPlayer:
    def test_attack_with_all_cards_with_lowest_value(self):
        hand = [Card(Suit.CLUBS, Rank.SEVEN), Card(Suit.HEARTS, Rank.SEVEN), Card(Suit.SPADES, Rank.SEVEN), Card(Suit.HEARTS, Rank.JACK), Card(Suit.CLUBS, Rank.JACK), Card(Suit.SPADES, Rank.JACK)]
        game = Game()
        game.trump = Card(Suit.SPADES, Rank.SIX)
        p = AIPlayer(hand=hand, game=game)

        attack = p.attack()
        assert len(attack) == 2
        assert attack[0].rank == attack[1].rank == Rank.SEVEN
        assert len(p.hand) == 4

    def test_defense_when_cant_beat_attack(self):
        hand = [Card(Suit.CLUBS, Rank.SEVEN), Card(Suit.HEARTS, Rank.SEVEN), Card(Suit.SPADES, Rank.SEVEN), Card(Suit.HEARTS, Rank.JACK), Card(Suit.CLUBS, Rank.JACK), Card(Suit.SPADES, Rank.JACK)]
        game = Game()
        game.trump = Card(Suit.DIAMONDS, Rank.SIX)
        game.attack_cards = [Card(Suit.CLUBS, Rank.ACE)]
        p = AIPlayer(hand=hand, game=game)

        assert p.defend() == None

    def test_successful_defense(self):
        hand = [Card(Suit.CLUBS, Rank.KING), Card(Suit.HEARTS, Rank.SIX),
            Card(Suit.SPADES, Rank.ACE), Card(Suit.CLUBS, Rank.ACE),
            Card(Suit.HEARTS, Rank.ACE), Card(Suit.SPADES, Rank.JACK)
        ]
        game = Game()
        game.trump = Card(Suit.DIAMONDS, Rank.SIX)
        game.attack_cards = [Card(Suit.CLUBS, Rank.QUEEN), Card(Suit.HEARTS, Rank.QUEEN)]
        p = AIPlayer(hand=hand, game=game)

        assert p.defend() == [Card(Suit.CLUBS, Rank.KING), Card(Suit.HEARTS, Rank.ACE)]
