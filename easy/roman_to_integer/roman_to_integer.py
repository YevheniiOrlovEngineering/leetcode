from utils.task import Task


class RomanToInteger(Task):
    """Given a roman numeral, convert it to an integer."""
    __task_num = 13
    __symbols = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    def solve(self, s: str) -> int:
        res, i = 0, 0
        while i != len(s):
            cur_sym_str = s[i]
            cur_sym_int = self.__symbols[cur_sym_str]

            if cur_sym_str == "I" or cur_sym_str == "X" or cur_sym_str == "C":
                if i != len(s) - 1 and self.__symbols[s[i+1]] > cur_sym_int:
                    res += self.__symbols[s[i+1]] - cur_sym_int
                    i += 2
                    continue
            res += cur_sym_int
            i += 1

        return res

    def solve_optimal(self, s: str) -> int:
        n = len(s)
        num = self.__symbols[s[n - 1]]
        for i in range(n - 2, -1, -1):
            if self.__symbols[s[i]] >= self.__symbols[s[i + 1]]:
                num += self.__symbols[s[i]]
            else:
                num -= self.__symbols[s[i]]
        return num

    @property
    def task_num(self) -> int:
        return self.__task_num
