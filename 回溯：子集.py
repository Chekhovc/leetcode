#78子集 —— 没有重复元素
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        path = []
        result = []
        self.backtracking(nums,0,path,result)
        return result

    def backtracking(self,nums,startindex,path,result):
        result.append(path[:])

        if startindex == len(nums):   #可以不写
            return

        for i in range(startindex,len(nums)):
            path.append(nums[i])
            self.backtracking(nums,i + 1,path,result)
            path.pop()


#90子集 —— 数组里有重复元素
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        path = []
        result = []

        self.backtracking(nums,0,path,result)
        return result

    def backtracking(self,nums,startindex,path,result):
        result.append(path[:])

        if startindex == len(nums):   #可以不写
            return

        for i in range(startindex,len(nums)):
            if i > startindex and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            self.backtracking(nums,i + 1,path,result)
            path.pop()
