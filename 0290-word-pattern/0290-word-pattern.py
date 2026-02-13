class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hashmap = {}
        parts = s.split(" ")

        if len(parts) != len(pattern):
            return False
        for char in range(len(parts)):
            p_char = pattern[char]
            word = parts[char]
            if p_char not in hashmap:
                if word in hashmap.values():
                    return False
                else:
                    hashmap[p_char] = word
            else:
                if hashmap[p_char] != word:
                    return False
        return True