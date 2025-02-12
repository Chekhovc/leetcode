# 我将每种类型的特点标注了出来，方便阅读。类型二有两种解法（去重方式）



#39组合总和 —— 无重复元素，无限制重复选取
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort()    #为后续剪枝准备，必不可少！！！
        self.dfs(candidates,target,[],result,0)
        return result

    def dfs(self,candidates,target,path,result,index):
        if index == len(candidates):
            return

        if target == 0:
            result.append(path[:])

        for i in range(index,len(candidates)):
            if target - candidates[i] < 0:   #若要剪枝 —— candidates必须有序 ！！！
                break
            path.append(candidates[i])
            self.dfs(candidates, target - candidates[i], path, result, i)   #用target - candidates[i]代替sum的记录作用; 用i当Index,可以避免重复的组合
            path.pop()

solution = Solution()
candidates = [int(i) for i in input().strip("[]") if i != ","]
target = int(input())
res = solution.combinationSum(candidates,target)
print(res)



#40组合总和Ⅱ ——  重复元素，只能选一次
#去重是关键 —— 树层去重（难点） + 树枝去重

# 解法一（利用index去重；稍微抽象）：
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        result = []
        self.dfs(candidates,target,0,[],result)
        return result

    def dfs(self,candidates,target,index,path,result):
        if target == 0:
            result.append(path[:])
            return

        for i in range(index,len(candidates)):
            if i > index and candidates[i] == candidates[i - 1]:   # i这里必须大于index,这样就避免了去掉合法组合的可能性
                continue

            if candidates[i] > target:
                break

            path.append(candidates[i])
            self.dfs(candidates,target - candidates[i],i + 1,path,result)
            path.pop()

solution = Solution()
candidates = eval(input())
target = int(input())
res = solution.combinationSum2(candidates,target)
print(res)

# 解法二（利用vis数组；便于理解）：
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        result = []
        vis = [0] * len(candidates)
        self.dfs(candidates,target,0,[],result,vis)
        return result

    def dfs(self,candidates,target,index,path,result,vis):
        if target == 0:
            result.append(path[:])
            return

        for i in range(index,len(candidates)):
            if i > 0 and candidates[i] == candidates[i - 1] and vis[i - 1] == 0:  #利用vis数组进行去重
                continue

            if candidates[i] > target:
                break

            path.append(candidates[i])
            vis[i] = 1
            self.dfs(candidates,target - candidates[i],i + 1,path,result,vis)
            path.pop()
            vis[i] = 0

solution = Solution()
candidates = eval(input())
target = int(input())
res = solution.combinationSum2(candidates,target)
print(res)



#组合总和Ⅲ —— 无重复元素，只能选一次
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def dfs(k,n,index,path,ans):
            if len(path) == k:
                if n == 0:
                    ans.append(path[:])
                return

            for i in range(index,9 - (k - len(path)) + 1):
                if i > n:
                    break
                path.append(i)
                dfs(k,n - i,i + 1,path,ans)
                path.pop()

        ans = []
        dfs(k,n,1,[],ans)
        return ans

solution = Solution()
k = int(input())
n = int(input())
result = solution.combinationSum3(k, n)
print(result)