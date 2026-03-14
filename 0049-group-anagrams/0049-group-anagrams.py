from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answers_dict = defaultdict(list)

        for word in strs:
            alphabet_arr = [0] * 26
            for char in word:
                alphabet_arr[ord(char) - ord('a')] += 1
            key = tuple(alphabet_arr)
            answers_dict[key].append(word)
        return list(answers_dict.values())