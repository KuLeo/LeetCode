from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """DFS"""
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """Always return 0 when we find max depth value"""
        if not root:
            return 0
        """Add 1 for each layer"""
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


def to_binary_tree(items: list[int]) -> TreeNode:
    """Create BT from list of values."""
    n = len(items)
    if n == 0:
        return None

    def inner(index: int = 0) -> TreeNode:
        """Closure function using recursion bo build tree"""
        if n <= index or items[index] is None:
            return None

        node = TreeNode(items[index])
        node.left = inner(2 * index + 1)
        node.right = inner(2 * index + 2)
        return node

    return inner()


testC = Solution()
if testC.maxDepth(to_binary_tree([3, 9, 20, None, None, 15, 7])) == 3:
    print('test1 - Success')
else:
    print('test1 - Fail')

if testC.maxDepth(to_binary_tree([1, None, 2])) == 2:
    print('test2 - Success')
else:
    print('test2 - Fail')
