from org.chiyi.modules.list_node import ListNode


def insert(n0: ListNode, P: ListNode):
    """在链表的节点n0之后插入节点P"""
    n1 = n0.next
    P.next = n1
    n0.next = P


def remove(n0: ListNode):
    """删除链表的节点n0之后的首个节点"""
    if not n0.next:
        return
    # n0 -> P -> n1
    P = n0.next
    n0.next = P.next


def access(head: ListNode, index: int) -> ListNode | None:
    """访问链表中索引为index的节点"""
    for _ in range(index):
        if not head:
            return None
        head = head.next
    return head


def find(head: ListNode, target: int) -> int:
    """在链表中查找值为target的首个节点"""
    index = 0
    while head:
        if head.val == target:
            return index
        head = head.next
        index += 1
    return -1
