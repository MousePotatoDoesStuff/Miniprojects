from typing import List


class Solution:
    def __init__(self):
        self.board = []
        self.empties = []
        self.log = []

    def getEmpty(self):
        empties = []
        for i, E in enumerate(self.board):
            for j, e in enumerate(E):
                if e == ".":
                    empties.append((i, j))
        self.empties = empties

    def getValid(self, vi, vj):
        S = set('123456789')
        E=self.board[vi]
        S -= set(E)
        S -= set([E[vj] for E in self.board])
        MS = set()
        a = vi - vi % 3
        b = vj - vj % 3
        for i in range(3):
            MS |= set(self.board[a + i][b:][:3])
        S -= MS
        S = list(S)
        S.sort(reverse=True)
        return S

    def backLog(self):
        while self.log and not self.log[-1][-1]:
            ind, _ = self.log.pop()
            i, j = self.empties[ind]
            self.board[i][j] = '.'
        return

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.getEmpty()
        if not self.empties:
            return
        E = self.empties[0]
        L = self.getValid(*E)
        self.log = [(0, L)]
        while self.log:
            cur, curL = self.log[-1]
            ci, cj = self.empties[cur]
            self.board[ci][cj] = curL.pop()
            if cur + 1 == len(self.empties):
                return
            nexL = self.getValid(*(self.empties[cur + 1]))
            self.log.append((cur + 1, nexL))
            self.backLog()
        return


def main():
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    sol = Solution()
    sol.solveSudoku(board)
    for L in board:
        print("".join(L))
    return


if __name__ == "__main__":
    main()
