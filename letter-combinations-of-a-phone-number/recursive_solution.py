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

    def generate_letter_combos(
        self, digit_index: int, digits: str, letter_combos: List[str]
    ) -> List[str]:
        letter_combos = [
            combo + letter
            for letter in self.phone_map[digits[digit_index]]
            for combo in letter_combos
        ]

        if digit_index == len(digits) - 1:
            return letter_combos
        else:
            return self.generate_letter_combos(digit_index + 1, digits, letter_combos)

    def letter_combinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        placeholder_letter_combos = [""]
        print(digits)
        final_letter_combos = self.generate_letter_combos(
            0, digits, placeholder_letter_combos
        )

        return final_letter_combos
