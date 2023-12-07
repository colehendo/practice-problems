from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        all_anagrams = []
        removed_words = []

        for word_index, word in enumerate(strs):
            if word in removed_words:
                    continue

            anagram_list = [word]
            removed_words.append(word)

            for comparison_word in strs[word_index + 1 :]:
                if len(word) != len(comparison_word):
                    continue

                list_word = list(word)
                list_word.sort()

                list_comparison_word = list(comparison_word)
                list_comparison_word.sort()

                sorted_word = "".join(list_word)
                sorted_comparison_word = "".join(list_comparison_word)

                if sorted_word == sorted_comparison_word:
                    anagram_list.append(comparison_word)
                    removed_words.append(comparison_word)

            all_anagrams.append(anagram_list)

        return all_anagrams
