class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result = []
        chessboard = ['.' * n for _ in range(n)]
        chessboard = list(map(list, chessboard))
        self.backtracking(n,chessboard,result,0)
        return result

    def isValid(self,n,i,chessboard,row):
        #不用检查行，直接检查列

        #检查列
        for j in range(n):
            if chessboard[j][i] == "Q":
                return False

        #检查45°和135°角
        #可以分开检查，并且不用全部遍历，只用遍历上面的，不用遍历下面的
        #两重for循环时间复杂度较大

        m, j = row - 1, i - 1
        while m >= 0 and j >= 0:
            if chessboard[m][j] == 'Q':
                return False  # 左上方向已经存在皇后，不合法
            m -= 1
            j -= 1

        # 检查 135 度角是否有皇后
        m, j = row - 1, i + 1
        while i >= 0 and j < len(chessboard):
            if chessboard[m][j] == 'Q':
                return False  # 右上方向已经存在皇后，不合法
            m -= 1
            j += 1

        return True


    def backtracking(self,n,chessboard,result,row):
        if row == n:
            chessboard = list(("".join(i) for i in chessboard))
            result.append(chessboard[:])
            return

        for i in range(0,n):
            if self.isValid(n,i,chessboard,row):
                chessboard[row][i] = "Q"
                self.backtracking(n,chessboard,result,row + 1)
                chessboard[row][i] = "."

solution = Solution()
n = int(input())
print(solution.solveNQueens(n))