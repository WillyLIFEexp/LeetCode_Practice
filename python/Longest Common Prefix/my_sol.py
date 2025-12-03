from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        check_word = strs[0]
        check_word_len = len(check_word)

        for s in strs[1:]:
            while check_word != s[0:check_word_len]:
                check_word_len -= 1
                if check_word_len == 0:
                    return ""

                check_word = check_word[0:check_word_len]

        return check_word
