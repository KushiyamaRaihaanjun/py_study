# 7
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


# 8
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
