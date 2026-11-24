class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        
        seen = set() 
        l, r, count, max_count = 0, 0, 0, 0
        
        while r < len(s): # 0
            if s[r] not in seen: #
                seen.add(s[r])
                count += 1
                r += 1
            else:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
                    count -= 1
            max_count = max(count, max_count)
        return max_count