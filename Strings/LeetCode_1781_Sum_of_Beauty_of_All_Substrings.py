from collections import defaultdict
class Solution:
    def beautySum(self, s: str) -> int:
        sm = 0
        # Iterate over all possible start indices for substrings.
        for i in range(len(s)):
            freq = defaultdict(int)
            # Expand the substring from i to j, updating character frequencies.
            for j in range(i, len(s)):
                freq[s[j]] += 1
                # Beauty of the current substring is highest frequency minus lowest frequency.
                sm += max(freq.values()) - min(freq.values())
        return sm