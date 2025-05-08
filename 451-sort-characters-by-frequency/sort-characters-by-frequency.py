class Solution:
    def frequencySort(self, s: str) -> str:
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        sorted_chars = sorted(char_count.items(), key=lambda item: item[1], reverse=True)

        result = ""
        for char, count in sorted_chars:
            result += char * count

        return result