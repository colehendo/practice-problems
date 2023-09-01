This was a test I wrote to interview candidates, and my subsequent solution

Take a look at a standard phone keyboard
(example: https://lefkowitz.me/static/efd721ff0a2a7db9e7426476e5df2175/e17e5/10name-phone-pad.png).
You see that each number between 2 and 9 has 3 or 4 letters associated with it,
but each letter is associated with only 1 number (ex: a = 2, j = 5).

Given a phone number of length n and a list of words,
return a list of only the words where each letter of that word
corresponds to a number in the phone number.

Example:
    phone_number = "2367"
    input_words = ["foo", "bar", "baz"]
    output_words = ["foo", "bar"]

Constraints:
    phone_number will always be a string

Your task:
    Implement the list_words_matching_phone_number function in the PhoneNumberAssessment class
    to return the list of words matching the phone number based on the list of words inputted

    Feel free to add any other functions or classes if you'd like