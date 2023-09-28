class Solution:
    def make_string_lowercase(self, input_string: str) -> str:
        return input_string.lower()


    def remove_non_alphanumeric_chars(self, input_string: str) -> str:
        # List comprehension could work here, but would create an unecessary list
        alphanumeric_string = ""

        for character in input_string:
            if character.isalnum():
                alphanumeric_string += character

        return alphanumeric_string


    def clean_input_string(self, input_string: str) -> str:
        lowercase_string = self.make_string_lowercase(input_string)
        alphanumeric_string = self.remove_non_alphanumeric_chars(lowercase_string)
        return alphanumeric_string


    def check_if_string_is_palindrome(self, string_to_check: str, start_index: int, end_index: int) -> bool:
        if start_index >= end_index:
            return True
        
        if string_to_check[start_index] == string_to_check[end_index]:
            start_index += 1
            end_index -= 1

            return self.check_if_string_is_palindrome(string_to_check, start_index, end_index)

        return False


    def isPalindrome(self, input_string: str) -> bool:
        cleaned_string = self.clean_input_string(input_string)

        start_index = 0
        end_index = len(cleaned_string) - 1

        string_is_palindrome = self.check_if_string_is_palindrome(cleaned_string, start_index, end_index)

        return string_is_palindrome
 