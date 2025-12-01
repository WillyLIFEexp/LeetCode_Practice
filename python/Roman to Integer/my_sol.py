class Solution:
    def romanToInt(self, s: str) -> int:
        r_dict = {
            'I': 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000
        }
        lst_char = None
        rslt = 0
        for i, char in enumerate(s[::-1]):
            if lst_char:
                if char == "I" and lst_char in ["V", "X"]:
                    rslt -= r_dict[char]
                elif char == "X" and lst_char in ["L", "C"]:
                    rslt -= r_dict[char]
                elif char == "C" and lst_char in ["D", "M"]:
                    rslt -= r_dict[char]
                else:
                    rslt += r_dict[char]
            else:
                rslt += r_dict[char]
            lst_char = char
        return rslt
