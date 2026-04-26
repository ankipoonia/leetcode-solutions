class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # openParen tracks the number of unmatched '(' seen so far.
        # moves counts the number of ')' insertions needed when there is no matching '('.
        openParen = moves = 0
        for ch in s:
            if ch == "(":
                openParen += 1
            else:
                openParen -= 1
            # If openParen becomes negative, we have an unmatched ')' and
            # must insert an '(' before it. Reset openParen because the
            # inserted '(' balances this ')'.
            if openParen < 0:
                moves += 1
                openParen = 0
        # Any remaining unmatched '(' require corresponding ')' insertions.
        return moves + openParen