
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        sumstart = ListNode()
        sum = sumstart

        while l1 is not None:
            sum.val += l1.val + l2.val if l2 is not None else l1.val
            sum.next = ListNode()
            if sum.val > 9:
                sum.val -= 10
                sum.next.val = 1

            l1 = l1.next
            if l2 is not None:
                l2 = l2.next

            temp = sum
            sum = sum.next


        while l2 is not None:
            sum.val += l2.val
            l2 = l2.next
            
            sum.next = ListNode()
            if sum.val > 9:
                sum.val -= 10
                sum.next.val = 1
                
            temp = sum
            sum = sum.next
        
        if temp.next.val == 0:
            temp.next = None
        

        return sumstart
    
