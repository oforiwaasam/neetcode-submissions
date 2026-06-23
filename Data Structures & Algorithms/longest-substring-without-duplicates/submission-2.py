class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        windowStart, windowEnd = 0, 1
        substr = s[windowStart]
        max_length = 1

        while windowEnd < len(s):
            ch = s[windowEnd]
            if ch not in substr:
                substr += s[windowEnd]
            else:
                substr = substr[substr.find(ch) + 1:] + s[windowEnd]
            windowEnd += 1
            max_length = max(max_length, len(substr))
        return max_length