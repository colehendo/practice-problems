from typing import List, Dict, Union


class BalancedStringAssessment:
    stack = []

    def check_string_is_balanced(
        self,
        input_string: str,
    ) -> bool:
        """
        :param input_string: phone number entered
        :return: a boolean value reflecting if input_string is balanced or not
        """

        stack = []
        single_direction_symbols = {
            "[": "]",
            "(": ")",
            "{": "}"
        }
        dual_direction_symbols = "'\""
        opening_symbols = single_direction_symbols.keys()
        closing_symbols = single_direction_symbols.values()

        for char in input_string:
            if char in opening_symbols:
                stack.append(single_direction_symbols[char])
            elif char in dual_direction_symbols:
                if char not in stack:
                    stack.append(char)
                else:
                    matching_char = stack.pop()
                    if matching_char != char:
                        return False
            elif char in closing_symbols:
                if not stack:
                    return False
                matching_char = stack.pop()
                if matching_char != char:
                    return False

        if stack:
            return False

        return True


class TestPhoneNumberAssessment:
    def __init__(self):
        self.balanced_string_assessment = BalancedStringAssessment()

    @staticmethod
    def get_tests() -> List[Dict[str, Union[str, bool]]]:
        tests = [
            {
                "input_string": "[a]{b}(c)",
                "expected_result": True,
            },
            {
                "input_string": "[(ab){c}]",
                "expected_result": True,
            },
            {
                "input_string": "([a)]",
                "expected_result": False,
            },
            {
                "input_string": "(([b])",
                "expected_result": False,
            },
            {
                "input_string": "b)",
                "expected_result": False,
            },
            {
                "input_string": "{c",
                "expected_result": False,
            },
            {
                "input_string": "abc",
                "expected_result": True,
            },
            {
                "input_string": "",
                "expected_result": True,
            },
            {
                "input_string": "[]{}()",
                "expected_result": True,
            },
            {
                "input_string": "'abc'",
                "expected_result": True,
            },
            {
                "input_string": '"\'abc\'"',
                "expected_result": True,
            },
            {
                "input_string": '\'"abc\'"',
                "expected_result": False,
            },
            {
                "input_string": "['a']'{\"b\"}(c)'",
                "expected_result": True,
            },
            {
                "input_string": "['a']\"{\"b\"}(c)\"",
                "expected_result": False,
            },
        ]

        return tests

    def run_individual_test(
        self, index: int, test: Dict[str, Union[str, bool]]
    ) -> bool:
        string_is_balanced_result = (
            self.balanced_string_assessment.check_string_is_balanced(
                test["input_string"]
            )
        )

        test_passed = (
            string_is_balanced_result == test["expected_result"]
            if type(string_is_balanced_result) == bool
            else False
        )

        if not test_passed:
            print(f"Test {str(index + 1)} failed!")
            print(f"Input string: {test['input_string']}")
            print(f"Resulting output: {str(string_is_balanced_result)}")
            print(f"Expected output: {str(test['expected_result'])}\n")

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
