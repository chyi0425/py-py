# coding: utf-8

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head):
        '''
        :param head: ListNode
        :return:  listNode
        '''
        ans = []
        tmp = head
        while tmp != None:
            ans.append(tmp.val)
            tmp = tmp.next

        ans.sort()
        tmp = head
        for i in ans:
            tmp.val = i
            tmp = tmp.next
        return head

    def sortList2(self, head):
        '''
        :param head: ListNode
        :return:  listNode
        '''
        if head == None or head.next == None:
            return head

        mid = self.findMiddle(head)

        right = self.sortList2(mid.next)
        mid.next = None
        left = self.sortList2(head)

        return self.merge(left, right)

    def merge(self, head1, head2):
        dummy = ListNode(0)
        head = dummy
        while head1 and head2:
            if head1.val < head2.val:
                head.next = head1
                head1 = head1.next
            else:
                head.next = head2
                head2 = head1.next
            head = head.next
        if head1:
            head.next = head1
        if head2:
            head.next = head2
        return dummy.next

    def findMiddle(self, head):
        slow, fast = head, head.next
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
        return slow
