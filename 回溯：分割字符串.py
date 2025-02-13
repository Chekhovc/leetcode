#131分割字符串

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        path = []
        self.backtracking(s,0,path,result)

        return result

    def isvalid(self,s,startindex,endindex):
        temp = s[startindex:endindex]
        temp_lst = list(temp)
        temp_lst.reverse()
        temp = "".join(temp_lst)
        if s[startindex:endindex] == temp:
            return True
        else:
            return False
    def backtracking(self,s,startindex,path,result):
        if startindex == len(s):
            result.append(path[:])
            return

        for i in range(startindex,len(s)):
            if not self.isvalid(s,startindex,i + 1):
                continue

            path.append(s[startindex:i + 1])
            self.backtracking(s,i + 1,path,result)
            path.pop()


solution = Solution()
s = input()
print(solution.partition(s))