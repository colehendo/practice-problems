from functools import cached_property
from typing import List, Dict, Union


class PhoneNumberAssessment:
    @cached_property
    def keypad_map(self) -> Dict[str, str]:
        keypad = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        return keypad

    @cached_property
    def possible_phone_numbers(self) -> List[str]:
        return self.keypad_map.keys()

    def compile_all_possible_letters(self, phone_number: str) -> str:
        """
        :param phone_number: phone number entered
        :return: all letters which correspond to a number in the phone number
        """

        possible_letters = ""

        for number in phone_number:
            possible_letters += self.keypad_map[number]

        return possible_letters

    def list_words_matching_phone_number(
        self, phone_number: str, input_words: List[str]
    ) -> List[str]:
        """
        :param phone_number: phone number entered
        :param input_words: list of words
        :return: list of words in input_words where each letter of that word
                 corresponds to a number in the phone number
        """

        words_matching_phone_number = []
        phone_number = "".join(
            num for num in set(phone_number) if num in self.possible_phone_numbers
        )
        all_possible_letters = self.compile_all_possible_letters(phone_number)

        for word in input_words:
            if all(letter.lower() in all_possible_letters for letter in word):
                words_matching_phone_number.append(word)

        return words_matching_phone_number


class TestPhoneNumberAssessment:
    def __init__(self):
        self.phone_number_assessment = PhoneNumberAssessment()

    @staticmethod
    def get_tests() -> List[Dict[str, Union[str, List[str]]]]:
        tests = [
            {
                "phone_number": "36",
                "input_words": ["foo"],
                "expected_output_words": ["foo"],
            },
            {
                "phone_number": "2367",
                "input_words": ["foo", "bar", "baz"],
                "expected_output_words": ["foo", "bar"],
            },
            {
                "phone_number": "012367",
                "input_words": ["foo", "bar", "baz"],
                "expected_output_words": ["foo", "bar"],
            },
            {
                "phone_number": "!a2367Z?",
                "input_words": ["foo", "bar", "baz"],
                "expected_output_words": ["foo", "bar"],
            },
            {
                "phone_number": "2367",
                "input_words": ["foo", "f00", "bAr", "ba$r"],
                "expected_output_words": ["foo", "bAr"],
            },
            {
                "phone_number": "4589",
                "input_words": ["foo", "bar", "baz"],
                "expected_output_words": [],
            },
            {"phone_number": "4589", "input_words": [], "expected_output_words": []},
        ]

        return tests

    def run_individual_test(
        self, index: int, test: Dict[str, Union[str, List[str]]]
    ) -> bool:
        resulting_output_words = (
            self.phone_number_assessment.list_words_matching_phone_number(
                test["phone_number"], test["input_words"]
            )
        )
        test_passed = resulting_output_words == test["expected_output_words"]

        if not test_passed:
            print(f"Test {str(index + 1)} failed!")
            print(f"Phone number: {test['phone_number']}")
            print(f"Input words: {test['input_words']}")
            print(f"Resulting output words: {resulting_output_words}")
            print(f"Expected output words: {test['expected_output_words']}\n")

        return test_passed

    def test_phone_number_assessment_solution(self):
        tests = self.get_tests()
        all_tests_passed = all(
            self.run_individual_test(index, test) for index, test in enumerate(tests)
        )
        if all_tests_passed:
            print("Congrats, all tests passed!")


if __name__ == "__main__":
    TestPhoneNumberAssessment().test_phone_number_assessment_solution()
