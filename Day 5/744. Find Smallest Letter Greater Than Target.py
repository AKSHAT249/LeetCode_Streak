class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        target_ascii_value = ord(target)

        for character in letters:
            current_ascii_value = ord(character)
            if current_ascii_value>target_ascii_value:
                return character
        return letters[0]
