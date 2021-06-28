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


# ans_obj = Solution()
# print(ans_obj.kidsWithCandies(candies=[12, 1, 12], extraCandies=10))
'''
# 11*
# 12*
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
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
'''
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


# obj_ans = Solution()
# ans_str = ["h", "e", "l", "l", "o"]
# obj_ans.reverseString(ans_str)
# print(ans_str)
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
# 計算量でアウト
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if(len(nums) == 1):
            return nums[0]
        sums = [0]*(len(nums)+1)
        sum = 0
        sums[0] = 0
        for i in range(len(nums)):
            sums[i+1] = sums[i] + nums[i]
        ans = -100000000000000000000
        for i in range(len(sums)):
            for j in range(i+1, len(sums)):
                ans = max(sums[j]-sums[i], ans)
        return ans


ans_obj = Solution()
print(ans_obj.maxSubArray([5, 4, -1, 7, 8]))
'''
# 18正解

'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        temp = 0
        max_num = max(nums)
        for i in range(len(nums)):
            temp += nums[i]
            if temp >= 0:
                max_num = max(max_num, temp)
            else:
                temp = 0
        return max_num
# Runtime: 60 ms, faster than 93.50% of Python3 online submissions for Maximum Subarray.
# Memory Usage: 14.5 MB, less than 5.69% of Python3 online submissions for Maximum Subarray.
'''
# 19

# 正解
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices_cp = prices.copy()
        prices_cp.sort(reverse=True)
        ans = -1
        if(prices_cp == prices):
            return 0
        else:
            minimum = 1000000
            ans = -1
            for price in prices:
                now = price
                if(now-minimum > 0):
                    ans = max(ans, now-minimum)
                minimum = min(minimum, price)
        return ans
'''
# 20(mid)
# 21

'''
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        num_dict = {}
        for num in range(len(nums)+1):
            num_dict[num] = 0
        for num in nums:
            num_dict[num] += 1
        ans_list = []
        for key in num_dict.keys():
            if(num_dict[key] == 0 and key > 0):
                ans_list.append(key)
        return ans_list
'''
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


'''
# イテレートできない
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        node_dict = {}
        for h in head:
            node_dict[h.val] = 0
        for h in head:
            node_dict[h.val] += 1
            if(node_dict[h.next] == 1):
                return True
        return False
'''

'''
# 答え
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        hashmap = {}
        while(head != None):
            if(head in hashmap):
                return True
            hashmap[head] = head
            head = head.next
        return False
'''

# 23
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 23...x
'''
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        ans = []
        def dfs(self, node, ans):
            if(node):
                if(node.right):
                    self.dfs(node.right)
                if(node.left):
                    self.dfs(node.left)
                ans.append(node.val)
        dfs(self,root,ans)
        return ans

ans_obj = Solution()
nodes = TreeNode([2,1,3])
print(ans_obj.invertTree(nodes))
'''
# 解答
'''
class Solution:
    def invertTree(self,root: TreeNode) -> TreeNode:
        if not root:
            return None
        right =self.invertTree(root.right)
        left = self.invertTree(root.left)
        root.left = right
        root.right = left
        return root
'''
# 24 x
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 解答
'''
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp = ans = Listnode(0)
        while(l1 or l2):
            if(l1 and l2):
                if(l1.val < l2.val):
                    ans.next = l1
                    l1 = l1.next
                else:
                    ans.next = l2
                    l2 = l2.next
            elif l1:
                ans.next = l1
                l1 = l1.next
            elif l2:
                ans.next = l2
                l2 = l2.next
            ans = ans.next
        return temp.next
'''
# 25
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        a = []
        a[0] = 1
        a[1] = 2
        for i in range(2,n):
            a[i] = a[i-1] + a[i-2]
        return a[n-1]
'''

# 26
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 問題文がよくわからなかった
'''
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        l = []

        def inorder(root):
            if(root == None):
                return
            if(root.left):
                inorder(root.left)
            l.append(root.val)

            if(root.right):
                inorder(root.right)
        inorder(root)
        return l
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 27 x

'''
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.dfs(root, root)

    # self.何とかにする場合は，関数定義を別に書く？
    def dfs(self, left, right):
        if(left and right):
            return left.val == right.val and self.dfs(left.left, right.right) and self.dfs(left.right, right.left)
        else:
            return left == right
'''

# 28 x

'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        pre = cur = 0
        for i in nums:
            pre, cur = cur, max(pre+i, cur)
        return cur
'''
# 29
# 30.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        cnt = 0
        first = 0
        list_first = []
        list_cp = []
        while head:
            list_first.append(head.val)
            list_cp.append(head.val)
            head = head.next
        list_cp = list_cp.reverse()
        print(list_cp)
        print(list_first)
        if(list_cp == list_first):
            return True
        else:
            return False
