class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # check each row first
        for row in range(9):
            hashset = set()
            for column in range(9):
                element = board[row][column]
                if element in hashset:
                    return False
                elif element != '.':
                    hashset.add(element)

        # check each column first
        for row in range(9):
            hashset = set()
            for column in range(9):
                element = board[column][row]
                if element in hashset:
                    return False
                elif element != '.':
                    hashset.add(element)

        # check individual boxes
        boxes = [(0, 0), (0, 3), (0, 6),
                (3, 0), (3, 3), (3, 6),
                (6, 0), (6, 3), (6, 6)]

        for i, j in boxes:
            hashset = set()
            for row in range(i, i + 3):
                for column in range(j, j + 3):
                    element = board[row][column]
                    if element in hashset:
                        return False
                    elif element != '.':
                        hashset.add(element)
        return True