from typing import Dict, List


class Solution:
    @property
    def phone_map(self) -> Dict[str, List[str]]:
        nums_to_letters = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        return nums_to_letters

    def letter_combinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        letter_combos = [""]

        for digit in digits:
            letter_combos = [
                combo + letter
                for letter in self.phone_map[digit]
                for combo in letter_combos
            ]

        return letter_combos
