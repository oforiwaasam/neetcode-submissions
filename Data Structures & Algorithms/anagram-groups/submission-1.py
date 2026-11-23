class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = defaultdict(list)

        for string in strs:
            ch_list = [0] * 26
            
            for ch in string:
                ch_list[ord(ch) - ord('a')] += 1
            
            store[tuple(ch_list)].append(string)

        return list(store.values())
        