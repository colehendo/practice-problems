class Solution: 
    def canConstruct(self, ransom_note: str, magazine: str) -> bool:
        if not magazine:
            return False

        for magazine_character in magazine:
            if not ransom_note:
                return True

            for ransom_note_index, ransom_note_character in enumerate(ransom_note):
                if ransom_note_character == magazine_character:
                    ransom_note = ransom_note[: ransom_note_index] + ransom_note[ransom_note_index + 1 :]
                    break

        if not ransom_note:
            return True
        return False
