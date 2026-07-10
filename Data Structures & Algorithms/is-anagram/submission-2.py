class Solution:
    def isAnagram(self, s: str, t):
        
        if len(s) != len(t):
            return False

        s_dict = self.create_dict(s)
        t_dict = self.create_dict(t)

        for ch in s_dict.keys():
            if ch not in t_dict:
                return False
            elif ch in t_dict:
                if s_dict[ch] != t_dict[ch]:
                    return False
        return True

    def create_dict(self, word):

        word_dict = {}

        for ch in word:
            if ch in word_dict:
                word_dict[ch] += 1
            else:
                word_dict[ch] = 1
        return word_dict
        