class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        merged_list = ListNode()
        pointer = merged_list

        while l1 and l2:
            pointer.next = ListNode()
            pointer = pointer.next

            if l1.val < l2.val:
                pointer.val = l1.val
                l1 = l1.next
            else:
                pointer.val = l2.val
                l2 = l2.next

        if l1 or l2:
            pointer.next = l1 if l1 else l2

        return merged_list.next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
