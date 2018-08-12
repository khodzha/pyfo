import pytest
from lib.game import Game
from lib.card import Card
from lib.suit import Suit
from lib.rank import Rank

class TestGame:
    @staticmethod
    def prepare_test(trump, player_card, ai_card):
        game = Game()
        game.trump = trump
        game.player.hand = [player_card]
        game.ai.hand = [ai_card]
        game.set_first_turn()
        return game

    def test_starting_player(self):
        game = TestGame.prepare_test(trump=Card(Suit.CLUBS, Rank.SIX), player_card=Card(Suit.CLUBS, Rank.SEVEN), ai_card=Card(Suit.CLUBS, Rank.EIGHT))
        assert game.turn == 'player'

    def test_starting_player2(self):
        game = TestGame.prepare_test(trump=Card(Suit.CLUBS, Rank.SIX), player_card=Card(Suit.CLUBS, Rank.JACK), ai_card=Card(Suit.HEARTS, Rank.EIGHT))
        assert game.turn == 'player'

    def test_starting_ai(self):
        game = TestGame.prepare_test(trump=Card(Suit.CLUBS, Rank.SIX), player_card=Card(Suit.CLUBS, Rank.JACK), ai_card=Card(Suit.CLUBS, Rank.EIGHT))
        assert game.turn == 'ai'


    def test_fill_hand(self):
        game = Game()

        old_len = len(game.deck)
        game.player.hand = game.player.hand[:1]
        print(game.player.missing_cards)
        game.fill_hand(game.player)
        new_len = len(game.deck)
        assert old_len - 5 == new_len
        assert len(game.player.hand) == 6

    def test_failing_defense_pushes_attack_cards_into_defender_hand(self):
        game = Game()
        game.turn = 'player'

        game.attack_cards = [Card(Suit.CLUBS, Rank.JACK)]
        game.defender.hand = []

        game.defend()
        assert game.defender.hand[0] == Card(Suit.CLUBS, Rank.JACK)

    def test_check_draw_conditions(self):
        game = Game()
        game.defender.hand = []
        game.attacker.hand = []
        assert game.check_win_conditions() == (True, None)

    def test_check_win_conditions(self):
        game = Game()
        game.defender.hand = []
        game.attacker.hand = [Card(Suit.CLUBS, Rank.JACK)]
        assert game.check_win_conditions() == (True, game.defender)

    def test_switch_turn_after_successful_defense(self):
        game = Game()
        turn = game.turn
        game.switch_turn(defense_success=True)
        assert game.turn != turn


    def test_switch_turn_after_failed_defense(self):
        game = Game()
        turn = game.turn
        game.switch_turn(defense_success=False)
        assert game.turn == turn
