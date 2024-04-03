"""
File: list_node.py
"""


class ListNode:
    """链表节点类"""

    def __init__(self, val: int):
        self.val: int = val
        self.next: ListNode | None = None # 指向后继节点的引用
        self.prev: ListNode | None = None # 指向前驱节点的引用




