"""
# Definition for a Node
"""


class NaryTreeNode:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
