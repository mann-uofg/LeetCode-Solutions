class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hashTable = {}
        balloon = {'b': 1, 'a': 1, 'l': 2, 'o': 2, 'n': 1}
        total = 0

        for char in text:
            hashTable[char] = hashTable.get(char, 0) + 1
        b_count = hashTable.get('b', 0)
        a_count = hashTable.get('a', 0)
        l_count = hashTable.get('l', 0) // 2
        o_count = hashTable.get('o', 0) // 2
        n_count = hashTable.get('n', 0)

        return min(b_count, a_count, l_count, o_count, n_count)