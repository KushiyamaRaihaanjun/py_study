from typing import List
# 7*
# Definition for a binary tree node
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        depth = 0
        stack = [(root, 1)]

        while(stack):  # stackに中身がある間
            root, length = stack.pop()  # pop
            if not root:
                return 0
            if(length > depth):  # 現在の長さがdepthより長い
                depth = length  # depth更新
            if(root.right):  # rootの右側にノードがある
                stack.append((root.right, length+1))  # 長さを加えたものをstackに
            if(root.left):  # rightと同様
                stack.append((root.left, length+1))
        return depth


# obj_ans = Solution()
# print(obj_ans.maxDepth(root=[3, 9, 20, None, None, 15, 7]))
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 8*
'''
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        depth = 0
        stack = [(root, 1)]
        deepest = {}
        while(stack):  # stackに中身がある間
            root, length = stack.pop()  # pop
            if not root:
                return 0
            if(length > depth):  # 現在の長さがdepthより長い
                depth = length  # depth更新
            if(root.right):  # rootの右側にノードがある
                stack.append((root.right, length+1))  # 長さを加えたものをstackに
                deepest[root.right.val] = length+1
            if(root.left):  # rightと同様
                stack.append((root.left, length+1))
                deepest[root.left.val] = length+1
        sorted(deepest.items(), key=lambda x: x[1])
        ans = 0
        mx = 0
        f = True
        for r, dep in deepest.items():
            if(f == True):
                mx = dep
                f = False
            if(dep == mx):
                ans += r

        return ans
'''
# 8-ans*

'''
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        ans = {}
        count = 0
        self.dfs(root, ans, count)

        return ans[max(ans)]

    def dfs(self, node, ans, count):
        if(node):
            if(node.left):
                self.dfs(node.left, ans, count+1)
            if(node.right):
                self.dfs(node.right, ans, count+1)
            if(count not in ans):
                ans[count] = node.val
            else:
                ans[count] += node.val
'''
# 9*
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if(root is None):
            return TreeNode(val)
        if(root.val > val):
            root.left = self.insertIntoBST(root.left, val)
        elif(root.val < val):
            root.right = self.insertIntoBST(root.right, val)
        return root
'''
# 10o
'''
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        candies_mx_num = max(candies)
        ans = []
        for val in candies:
            if(val + extraCandies >= candies_mx_num):
                ans.append(True)
            else:
                ans.append(False)
        return ans


#ans_obj = Solution()
#print(ans_obj.kidsWithCandies(candies=[12, 1, 12], extraCandies=10))
'''
# 11*
# 12*
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1 and not root2:
            return None
        if not root1:
            return root2
        if not root2:
            return root1
        if root1 and root2:
            ans = TreeNode(root1.val+root2.val)
            ans.left = self.mergeTrees(root1.left, root2.left)
            ans.right = self.mergeTrees(root1.right, root2.right)
            return ans
# 13*
# 14


'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic_num = {}
        for num in nums:
            dic_num[num] = 0
        for num in nums:
            dic_num[num] += 1
        for key, val in dic_num.items():
            if(val == 1):
                return key


obj_ans = Solution()
print(obj_ans.singleNumber(nums=[4, 4, 2]))
'''

'''
# o15 


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s = s.reverse()


#obj_ans = Solution()
#ans_str = ["h", "e", "l", "l", "o"]
#obj_ans.reverseString(ans_str)
#print(ans_str)
'''
# 16.o

'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans_dict = {}
        for num in nums:
            ans_dict[num] = 0
        for num in nums:
            ans_dict[num] += 1
        ans = -1
        val = -1
        for key in ans_dict.keys():
            if(val < ans_dict[key]):
                val = ans_dict[key]
                ans = key
        return ans


ans_obj = Solution()
print(ans_obj.majorityElement([3, 2, 3]))
'''

# 17.x


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if(len(nums) == 1):
            return nums[0]
        sums = [0]*(len(nums)+1)
        sum = 0
        sums[0] = nums[0]
        for i in range(len(nums)):
            sums[i] = sums[i-1] + nums[i]
        ans = -1
        for i in range(len(sums)):
            for j in range(i+1, len(sums)):
                ans = max(sums[j]-sums[i], ans)
        return ans


ans_obj = Solution()
print(ans_obj.maxSubArray([5, 4, -1, 7, 8]))
