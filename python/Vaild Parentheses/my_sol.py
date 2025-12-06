class Solution:
    def isValid(self, s: str) -> bool:
        placeholder = []
        check_dict = {
            ")":"(",
            "}":"{",
            "]":"[",
            }
        # If the string is less than 1, then should return False
        if len(s) <= 1:
            return False

        for b in s:
            if b not in check_dict.keys():
                placeholder.append(b)
            elif placeholder and placeholder.pop() == check_dict.get(b):
                pass
            else:
                return False
        return True if len(placeholder) == 0 else False

