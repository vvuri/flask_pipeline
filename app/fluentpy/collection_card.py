# Work with collections
# Run test:
# $ pytest .\collection_card.py

import collections
import pytest

Card = collections.namedtuple('Card', {'rank', 'suit'})


class FrenchDesk:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades clubs diamonds hearts'.split(' ')

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards(item)


def test_one_card():
    beet_card = Card('7', 'diamonds')
    print(beet_card)


def test_list_comp():
    symbol = '$€®¤'
    codes = [ord(x) for x in symbol]
    assert codes == [36, 8364, 174, 164]

