from lib.player import Player

class AIPlayer(Player):
    def __init__(self, game, hand):
        super().__init__(game, hand)
        self.name = 'AI'

    def attack(self):
        lowest_rank = min(self.hand, key=lambda c: c.value(self.trump_suit)).rank
        cards = list(filter(lambda c: c.value(self.trump_suit) == lowest_rank, self.hand))
        self._remove_cards_from_hand(cards)
        return cards

    def defend(self):
        left_cards = self.hand.copy()
        higher_hand = []
        for attack_card in self.game.attack_cards:
            higher_cards = list(filter(lambda c: c.greater(attack_card, self.trump_suit), left_cards))
            if higher_cards:
                card = min(higher_cards, key=lambda c: c.value(self.trump_suit))
                higher_hand.append(card)
                left_cards.remove(card)
            else:
                return None


        self._remove_cards_from_hand(higher_hand)
        return higher_hand

    def is_ai(self):
        return True
