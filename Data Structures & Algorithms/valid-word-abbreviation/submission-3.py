class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0
        m, n = len(word), len(abbr)

        while j < n:
            if abbr[j].isdigit():
                # leading zero is invalid
                if abbr[j] == '0':
                    return False

                skip = 0
                while j < n and abbr[j].isdigit():
                    skip = skip * 10 + int(abbr[j])
                    j += 1

                i += skip
                if i > m:
                    return False
            else:
                if i >= m or word[i] != abbr[j]:
                    return False
                i += 1
                j += 1

        return i == m
