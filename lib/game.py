from random import shuffle, randint
from lib.card import Card
from lib.suit import Suit
from lib.rank import Rank
from lib.deck import Deck, HAND_SIZE
from lib.player import Player
from lib.ai_player import AIPlayer

class Game:
    def __init__(self):
        deck = Deck.shuffle()
        self.trump = deck[-1]

        hand1 = deck[:HAND_SIZE]
        deck = deck[HAND_SIZE:]

        hand2 = deck[:HAND_SIZE]

        self.deck = deck[HAND_SIZE:]
        self.ai = AIPlayer(self, hand1)
        self.player = Player(self, hand2)
        self.set_first_turn()

    def set_first_turn(self):
        player_trump = self.player.lowest_trump_card()
        ai_trump = self.ai.lowest_trump_card()

        if player_trump and ai_trump:
            if player_trump.greater(ai_trump, self.trump_suit):
                self.turn = 'ai'
            else:
                self.turn = 'player'
        elif player_trump:
            self.turn = 'player'
        elif ai_trump:
            self.turn = 'ai'
        else:
            if randint(0, 1) == 0:
                self.turn = 'ai'
            else:
                self.turn = 'player'

    @property
    def trump_suit(self):
        return self.trump.suit

    @property
    def attacker(self):
        if self.turn == 'ai':
            return self.ai
        else:
            return self.player

    @property
    def defender(self):
        if self.turn == 'ai':
            return self.player
        else:
            return self.ai

    def attack(self):
        self.attack_cards = self.attacker.attack()
        print('Attacking cards: %s' % self.attack_cards)

    def defend(self):
        defend_cards = self.defender.defend()
        if self.defender.is_ai():
            print('Defending cards: %s' % defend_cards)

        if defend_cards:
            return True
        else:
            self.defender.push_cards(self.attack_cards)
            return False

    def finish_turn(self, defense_success):
        self.attack_cards = []
        self.fill_hand(self.attacker)
        self.fill_hand(self.defender)
        result = self.check_win_conditions()
        self.switch_turn(defense_success=defense_success)

        return result

    def check_win_conditions(self):
        if self.attacker.missing_cards == HAND_SIZE and self.defender.missing_cards == HAND_SIZE:
            return (True, None)
        elif self.attacker.missing_cards == HAND_SIZE:
            return (True, self.attacker)
        elif self.defender.missing_cards == HAND_SIZE:
            return (True, self.defender)
        else:
            return (False, None)

    def switch_turn(self, defense_success):
        if defense_success:
            if self.turn == 'ai':
                self.turn = 'player'
            else:
                self.turn = 'ai'

    def fill_hand(self, player):
        missing_cards = player.missing_cards
        if missing_cards > 0:
            player.push_cards(self.deck[:missing_cards])
            self.deck = self.deck[missing_cards:]

    def main_loop(self):
        while True:
            defense_result = self.make_turn()
            (game_finished, winner) = self.finish_turn(defense_success=defense_result)
            if game_finished:
                if winner:
                    print('%s won!' % winner.name)
                else:
                    print('Draw!')
                break

    def make_turn(self):
        print('Trump: %s' % self.trump)
        print('Current turn: %s' % self.turn.upper())
        print('Your hand %s' % self.player.hand)
        self.attack()
        defense_result = self.defend()
        return defense_result
