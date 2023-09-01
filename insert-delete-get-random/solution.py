from random import choice
from collections import defaultdict


class RandomizedSet:
    def __init__(self):
        self.items = []
        self.item_positions = defaultdict()

    def insert(self, val: int) -> bool:
        if val in self.item_positions:
            return False

        self.items.append(val)
        self.item_positions[val] = len(self.items) - 1

        return True

    def remove(self, val: int) -> bool:
        if not val in self.item_positions:
            return False

        val_position = self.item_positions.pop(val)
        last_item = self.items.pop()

        if val_position < len(self.items):
            self.items[val_position] = last_item
            self.item_positions[last_item] = val_position

        return True

    def get_random(self) -> int:
        return choice(self.items)
