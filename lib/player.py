from lib.card import Card
from lib.deck import HAND_SIZE

class Player:
    @staticmethod
    def processed_attack_input(prompt):
        text = input(prompt)
        str_cards = text.split()
        cards = list(map(lambda c: Card.from_str(c), str_cards))
        return cards

    @staticmethod
    def processed_defense_input(prompt):
        text = input(prompt)
        if text == 'PASS':
            return None
        str_cards = text.split()
        cards = list(map(lambda c: Card.from_str(c), str_cards))
        return cards

    def __init__(self, game, hand):
        self.game = game
        self.hand = hand
        self.name = 'PLAYER'

    def is_ai(self):
        return False

    @property
    def missing_cards(self):
        return HAND_SIZE - len(self.hand)

    @property
    def trump_suit(self):
        return self.game.trump_suit

    @property
    def attack_cards(self):
        return self.game.attack_cards

    def lowest_trump_card(self):
        trumps = list(filter(lambda card: card.suit == self.trump_suit, self.hand))
        if trumps:
            return min(trumps, key=lambda c: c.rank)
        else:
            return None

    def attack(self):
        cards = Player.processed_attack_input("Your attack, enter cards (PASS for pass): ")
        while not self.valid_attack_turn(cards):
            cards = Player.processed_attack_input("Invalid input, try again: ")

        self._remove_cards_from_hand(cards)
        return cards

    def defend(self):
        maybe_cards = Player.processed_defense_input("Your defense, enter cards: ")
        while not self.valid_defense_turn(maybe_cards):
            maybe_cards = Player.processed_defense_input("Invalid input, try again: ")

        self._remove_cards_from_hand(maybe_cards)
        return maybe_cards

    def push_cards(self, cards):
        self.hand.extend(cards)

    def valid_attack_turn(self, cards):
        all_in_hand = all(map(lambda c: c in self.hand, cards))
        same_rank = len(set(map(lambda c: c.rank, cards))) == 1
        return all_in_hand and same_rank

    def valid_defense_turn(self, cards):
        all_in_hand = all(map(lambda c: c in self.hand, cards))

        cards_zip = zip(cards, self.attack_cards)
        defense_higher_than_attack = all(map(lambda a: a[0].greater(a[1], self.trump_suit), cards_zip))
        return all_in_hand and defense_higher_than_attack

    def _remove_cards_from_hand(self, maybe_cards):
        if maybe_cards:
            self.hand = [card for card in self.hand if card not in maybe_cards]

