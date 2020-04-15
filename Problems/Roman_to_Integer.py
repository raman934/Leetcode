# Runtime : 56 ms
# Memory Usage : 13.2 MB
class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        n = len(s)
        def roman(ch):
            if ch == 'I':
                return 1
            elif ch == 'V':
                return 5
            elif ch == 'X':
                return 10
            elif ch == 'L':
                return 50
            elif ch == 'C':
                return 100
            elif ch == 'D':
                return 500
            elif ch == 'M':
                return 1000
        for i in range(n-1):
            j = i+1
            if s[i] != s[j]:
                if s[i] == 'I' and (s[j] == 'V' or s[j] == 'X'):
                    res -= 1
                elif s[i] == 'X' and (s[j] == 'L' or s[j] == 'C'):
                    res -= 10
                elif s[i] == 'C' and (s[j] == 'D' or s[j] == 'M'):
                    res -= 100
                else:
                    res += roman(s[i])
            else:
                res += roman(s[i])
        res += roman(s[n-1])
        return res
