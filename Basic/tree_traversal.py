# -*- coding: utf-8 -*-

# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def preorderTraversal(root):
    """
    前序遍历
    :type root: TreeNode
    :rtype: List[int]
    """
    result, curr = [], root
    while curr:
        if curr.left is None:
            result.append(curr.val)
            curr = curr.right
        else:
            node = curr.left
            while node.right and node.right != curr:
                node = node.right

            if node.right is None:
                result.append(curr.val)
                node.right = curr
                curr = curr.left
            else:
                node.right = None
                curr = curr.right

    return result

def preorderTraversalStack(root):
    """
    前序遍历，栈式方法实现
    :type root: TreeNode
    :rtype: List[int]
    """
    result, stack = [], [(root, False)]
    while stack:
        root, is_visited = stack.pop()
        if root is None:
            continue
        if is_visited:
            result.append(root.val)
        else:
            stack.append((root.right, False))
            stack.append((root.left, False))
            stack.append((root, True))
    return result

def inorderTraversal(root):
    """
    中序遍历
    :type root: TreeNode
    :rtype: List[int]
    """
    result, curr = [], root
    while curr:
        if curr.left is None:
            result.append(curr.val)
            curr = curr.right
        else:
            node = curr.left
            while node.right and node.right != curr:
                node = node.right

            if node.right is None:
                node.right = curr
                curr = curr.left
            else:
                result.append(curr.val)
                node.right = None
                curr = curr.right

    return result

def inorderTraversalStack(root):
    """
    中序遍历，栈式方法实现
    :type root: TreeNode
    :rtype: List[int]
    """
    result, stack = [], [(root, False)]
    while stack:
        root, is_visited = stack.pop()
        if root is None:
            continue
        if is_visited:
            result.append(root.val)
        else:
            stack.append((root.right, False))
            stack.append((root, True))
            stack.append((root.left, False))
    return result

def postorderTraversalStack(root):
    """
    后序遍历，栈式方法实现
    :type root: TreeNode
    :rtype: List[int]
    """
    result, stack = [], [(root, False)]
    while stack:
        root, is_visited = stack.pop()
        if root is None:
            continue
        if is_visited:
            result.append(root.val)
        else:
            stack.append((root, True))
            stack.append((root.right, False))
            stack.append((root.left, False))
    return result

def levelorderTraversal(root):
    """
    层序遍历
    :param root: TreeNode
    :return: List[List[int]]
    """
    if root is None:
        return []
    result, current = [], [root]
    while current:
        next_level, vals = [], []
        for node in current:
            vals.append(node.val)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        current = next_level
        result.append(vals)
    return result

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    result = preorderTraversal(root)
    print('preorder result:{}'.format(result))
    result = inorderTraversal(root)
    print('inorder result:{}'.format(result))
    result = postorderTraversalStack(root)
    print('postorder result:{}'.format(result))
    result = levelorderTraversal(root)
    print('levelorder result:{}'.format(result))
